from abc import ABC, abstractmethod

import pymysql
from pymysql.connections import Connection
from typing import List, Generic, TypeVar, Tuple, Any
from pymysql.cursors import DictCursor
from config import DB_HOST, DB_NAME, DB_PASSWORD, DB_PORT, DB_USER
from enums.opt_enum import OptEnum


T = TypeVar("T")  # 实体数据类型 (如 Country, Team)


class DbBase(ABC, Generic[T]):
    @property
    @abstractmethod
    def upsert_sql(self) -> str:
        """UPSERT 的 SQL 语句"""
        pass

    @property
    @abstractmethod
    def insert_sql(self) -> str:
        """纯 INSERT 的 SQL 语句"""
        pass

    @property
    @abstractmethod
    def select_source_ids_sql(self) -> str:
        """查询数据库现有全部/作用域内 ID 的 SQL 语句"""
        pass

    @property
    @abstractmethod
    def select_batch_source_ids_sql(self) -> str:
        """查询数据库现有全部/作用域内 ID 的 SQL 语句"""
        pass

    @property
    @abstractmethod
    def soft_delete_sql(self) -> str:
        """软删除的 SQL 语句 (UPDATE status=0 WHERE id IN %s)"""
        pass

    @property
    @abstractmethod
    def delete_sql(self) -> str:
        """物理删除的 SQL 语句 (DELETE FROM table WHERE ...)"""
        pass

    @property
    @abstractmethod
    def delete_batch_sql(self) -> str:
        """物理删除的 SQL 语句 (DELETE FROM table WHERE ...)"""
        pass

    @abstractmethod
    def to_upsert_params(self, item: T) -> Tuple:
        """将对象转换为 UPSERT 的 SQL 参数元组"""
        pass

    @abstractmethod
    def to_insert_params(self, item: T) -> Tuple:
        """将对象转换为 INSERT 的 SQL 参数元组"""
        pass

    @abstractmethod
    def get_entity_id(self, item: T) -> Any:
        """获取实体的唯一标识 ID (如 item.id)"""
        pass

    @staticmethod
    def get_connection() -> Connection:
        return pymysql.connect(
            host=DB_HOST,
            port=DB_PORT,
            user=DB_USER,
            password=DB_PASSWORD,
            database=DB_NAME,
            charset="utf8mb4",
            cursorclass=DictCursor
        )

    def save(self, results: List[T], opt: OptEnum, batch_id: str = None):
        try:
            conn = self.get_connection()

            match opt:
                case OptEnum.MERGE:
                    params = [
                        self.to_upsert_params(result)
                        for result in results
                    ]
                    with conn.cursor() as cursor:
                        cursor.executemany(self.upsert_sql, params)
                    conn.commit()

                case OptEnum.SYNC:
                    with conn.cursor() as cursor:
                        # 从数据库查出当前联赛所有的 team_id (仅查主键，速度极快)
                        if batch_id:
                            cursor.execute(self.select_batch_source_ids_sql, (batch_id,))
                        else:
                            cursor.execute(self.select_source_ids_sql)

                        existed_source_ids = {row["source_id"] for row in cursor.fetchall()}

                        # 在 Python 内存中用 set 做差集计算，获取缺失项
                        current_team_ids = {t.id for t in results}
                        missing_team_ids = existed_source_ids - current_team_ids

                        # 批量 UPSERT：更新/插入最新爬取的数据，并确保 status 为 1 (正常)
                        params = [
                            self.to_upsert_params(result)
                            for result in results
                        ]
                        cursor.executemany(self.upsert_sql, params)

                        # 批量软删除缺失数据
                        if missing_team_ids:
                            # 注意：PyMySQL 处理 IN (%s) 时需要传入 tuple
                            cursor.execute(self.delete_sql, (tuple(missing_team_ids),))

                    # 在同一个事务中统一提交，确保原子性（要么全成功，要么全回滚）
                    conn.commit()
                    print(f"同步完成！更新/插入 {len(results)} 条，软删除 {len(missing_team_ids)} 条。")

                case OptEnum.APPEND:
                    params = [
                        self.to_insert_params(result)
                        for result in results
                    ]

                    with conn.cursor() as cursor:
                        cursor.executemany(self.insert_sql, params)

                    conn.commit()

                case OptEnum.REBUILD:
                    with conn.cursor() as cursor:
                        if batch_id:
                            cursor.executemany(self.delete_batch_sql, (batch_id,))
                        else:
                            cursor.execute(self.delete_sql)

                        params = [
                            self.to_insert_params(result)
                            for result in results
                        ]

                        cursor.executemany(self.insert_sql, params)

                    conn.commit()

        except Exception as e:
            conn.rollback()
            raise
        finally:
            conn.close()