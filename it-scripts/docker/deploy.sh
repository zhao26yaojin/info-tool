#!/bin/bash
# info tool - Docker 中间件一键部署脚本
# 使用方法:
#   ./deploy.sh dev   # 启动 dev 中间件 (Nacos embedded)
#   ./deploy.sh test  # 启动 test 中间件 (Nacos + MySQL)
#   ./deploy.sh       # 默认 test
#
# 注意:
#   - 本脚本只负责中间件 (MySQL 必选, Nacos/Redis/Kafka/MinIO/imgproxy 按配置 enable), 不包含应用容器
#   - 中间件按环境共享: 容器名为 {env}-mysql / {env}-nacos ..., 同一台机器上的多个项目共用一套.
#     固定 compose project 名 ({env}-middleware) + --no-recreate, 保证已运行的共享中间件不会因
#     本项目的 compose 配置与其他项目略有差异而被重建 (重启会影响其他项目).
#   - 应用部署由 code-tool 的 Deploy Server / Deploy PC Web / Deploy Mobile Web 负责
#   - Nacos 配置推送由 Deploy Nacos 步骤通过 OpenAPI 完成

set -e

ENV="${1:-test}"
COMPOSE_FILE="docker-compose-${ENV}.yml"

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"

if [ ! -f "$SCRIPT_DIR/$COMPOSE_FILE" ]; then
    echo "Compose file not found: $COMPOSE_FILE"
    echo "Usage: $0 [dev|test]"
    exit 1
fi

echo "=============================="
echo "  info tool Middleware Deploy [$ENV]"
echo "  using $COMPOSE_FILE"
echo "=============================="

cd "$SCRIPT_DIR"

DC="docker-compose -p ${ENV}-middleware -f $COMPOSE_FILE"

# 启动中间件
echo ""
echo "Starting MySQL / minio / imgproxy ..."
$DC up -d --no-recreate mysql minio imgproxy
echo "Waiting for MySQL to be ready..."
sleep 15

echo ""
echo "Starting Nacos ..."
$DC up -d --no-recreate nacos
echo "Waiting for Nacos to be ready..."
sleep 20

# MinIO 为多项目共享, MINIO_DEFAULT_BUCKETS 只在容器首次创建时生效, 这里幂等地补建本项目 bucket
echo ""
echo "Ensuring MinIO bucket it-storage ..."
for i in $(seq 1 30); do
    if docker exec "${ENV}-minio" sh -c 'mc alias set local http://localhost:9000 "$MINIO_ROOT_USER" "$MINIO_ROOT_PASSWORD" >/dev/null 2>&1 && mc mb --ignore-existing local/it-storage'; then
        break
    fi
    if [ "$i" = "30" ]; then
        echo "Failed to create MinIO bucket it-storage"
        exit 1
    fi
    sleep 2
done

echo ""
echo "=============================="
echo "  Middleware containers started!"
echo "=============================="
echo ""
echo "Service URLs:"
echo "  - Nacos Console: http://localhost:8848/nacos"
echo ""
echo "Next steps:"
echo "  - Deploy Nacos     # 推送配置到 Nacos"
echo "  - Deploy DB       # 创建业务数据库表"
echo "  - Deploy Server    # 部署后端服务"
echo "  - Deploy PC Web    # 部署 PC 前端"
echo "  - Deploy Mobile Web # 部署移动端前端"
echo ""
echo "Useful commands:"
echo "  $DC ps       # 查看服务状态"
echo "  $DC logs -f  # 查看日志"
echo "  $DC down     # 停止所有服务 (注意: 中间件被本机所有项目共享)"
echo "  $DC down -v  # 停止并删除数据卷 (会清空所有项目的数据!)"

