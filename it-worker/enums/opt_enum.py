import enum


class OptEnum(enum.Enum):
    MERGE = 'merge'  # 合入（新数据有旧数据没有直接insert，新数据和旧数据都有则update）
    SYNC = 'sync'  # 同步（新数据有旧数据没有直接insert，新数据和旧数据都有则update，旧数据有新数据中不存在则软删除）
    APPEND = 'append'  # 追加
    REBUILD = 'rebuild' # 覆盖（定时任务中不允许出现，删除旧数据，再insert新数据）