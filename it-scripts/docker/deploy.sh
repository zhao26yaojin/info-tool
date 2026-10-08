#!/bin/bash
# info tool - Docker 中间件一键部署脚本
# 使用方法:
#   ./deploy.sh dev   # 启动 dev 中间件 (Nacos embedded)
#   ./deploy.sh test  # 启动 test 中间件 (Nacos + MySQL)
#   ./deploy.sh       # 默认 test
#
# 注意:
#   - 本脚本只负责中间件 (MySQL 必选, Nacos/Redis/Kafka/MinIO/imgproxy 按配置 enable), 不包含应用容器
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

# 启动中间件
echo ""
echo "Starting MySQL / minio / imgproxy ..."
docker-compose -f "$COMPOSE_FILE" up -d mysql minio imgproxy
echo "Waiting for MySQL to be ready..."
sleep 15



echo ""
echo "=============================="
echo "  Middleware containers started!"
echo "=============================="
echo ""

echo "Next steps:"

echo "  - Deploy DB       # 创建业务数据库表"
echo "  - Deploy Server    # 部署后端服务"
echo "  - Deploy PC Web    # 部署 PC 前端"
echo "  - Deploy Mobile Web # 部署移动端前端"
echo ""
echo "Useful commands:"
echo "  docker-compose -f $COMPOSE_FILE ps       # 查看服务状态"
echo "  docker-compose -f $COMPOSE_FILE logs -f  # 查看日志"
echo "  docker-compose -f $COMPOSE_FILE down     # 停止所有服务"
echo "  docker-compose -f $COMPOSE_FILE down -v  # 停止并删除数据卷"

