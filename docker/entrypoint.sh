#!/bin/sh
# sub-sift 本地 Docker 模式启动脚本
#
# 1. /app 首次启动：浅克隆仓库（代码 + 数据始终与 GitHub 一致）
#    远端不可达时降级为镜像自带副本（无同步能力，但 web 仍可启动）
# 2. data/ output/ 卷为空时从仓库恢复
# 3. 启动 web 服务（内部拉起同步线程）
set -e

REPO_URL="${REPO_URL:-https://github.com/ypj034/sub-sift.git}"
BRANCH="${REPO_BRANCH:-main}"
WEB_PORT="${WEB_PORT:-8080}"

mkdir -p /app/data /app/output

if [ ! -d /app/.git ]; then
  echo "[entrypoint] 初始化工作区: $REPO_URL ($BRANCH)"
  if git init -q /app \
     && git -C /app remote add origin "$REPO_URL" \
     && git -C /app fetch --depth=1 origin "$BRANCH" \
     && git -C /app checkout -f -B "$BRANCH" FETCH_HEAD; then
    echo "[entrypoint] 工作区就绪"
  else
    echo "[entrypoint] 无法访问远端，改用镜像自带副本（无同步能力）"
    rm -rf /app/.git
    cp -r /opt/sub-sift/. /app/
  fi
fi

# 编辑回推需要提交身份
git -C /app config user.email "sub-sift@localhost" 2>/dev/null || true
git -C /app config user.name "sub-sift" 2>/dev/null || true

# 卷为空（首次启动）时从仓库恢复数据与输出
for d in data output; do
  if [ -z "$(ls -A "/app/$d" 2>/dev/null)" ]; then
    echo "[entrypoint] $d 为空，从仓库恢复"
    git -C /app checkout -- "$d" 2>/dev/null || true
  fi
done

cd /app
exec uvicorn web:app --host 0.0.0.0 --port "$WEB_PORT"
