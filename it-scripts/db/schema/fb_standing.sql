DROP TABLE IF EXISTS `fb_standing`;
CREATE TABLE `fb_standing`  (
  `id` bigint(0) NOT NULL AUTO_INCREMENT COMMENT "id",
  `name` varchar(50) NOT NULL  COMMENT "名称",
  `tournament_id` bigint(0) NOT NULL  COMMENT "id",
  `source_id` varchar(255) NOT NULL  COMMENT "爬虫源数据id（去重用）",
  `wins` int(0) NULL DEFAULT NULL  COMMENT "胜",
  `draws` int(0) NULL DEFAULT NULL  COMMENT "平",
  `losses` int(0) NULL DEFAULT NULL  COMMENT "负",
  `goals_for` int(0) NULL DEFAULT NULL  COMMENT "进球",
  `goals_against` int(0) NULL DEFAULT NULL  COMMENT "失球",
  `goal_difference` int(0) NULL DEFAULT NULL  COMMENT "净胜球",
  `points` int(0) NULL DEFAULT NULL  COMMENT "积分",
  PRIMARY KEY (`id`) USING BTREE,
  INDEX `idx_name`(`name`) USING BTREE COMMENT '名称索引',
  INDEX `idx_tournament_id`(`tournament_id`) USING BTREE COMMENT 'id索引',
  UNIQUE INDEX `idx_source_id`(`source_id`) USING BTREE COMMENT '爬虫源数据id（去重用）索引'
) ENGINE = InnoDB CHARACTER SET = utf8mb3 COLLATE = utf8mb3_general_ci COMMENT = '积分榜表' ROW_FORMAT = Dynamic;

