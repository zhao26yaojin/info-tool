DROP TABLE IF EXISTS `common_country`;
CREATE TABLE `common_country`  (
  `id` bigint(0) NOT NULL AUTO_INCREMENT COMMENT "id",
  `name` varchar(50) NOT NULL  COMMENT "名称",
  `logo` varchar(255) NULL DEFAULT NULL  COMMENT "头像",
  `source_id` varchar(255) NOT NULL  COMMENT "爬虫源数据id（去重用）",
  PRIMARY KEY (`id`) USING BTREE,
  INDEX `idx_name`(`name`) USING BTREE COMMENT '名称索引',
  UNIQUE INDEX `idx_source_id`(`source_id`) USING BTREE COMMENT '爬虫源数据id（去重用）索引'
) ENGINE = InnoDB CHARACTER SET = utf8mb3 COLLATE = utf8mb3_general_ci COMMENT = '国家表' ROW_FORMAT = Dynamic;

