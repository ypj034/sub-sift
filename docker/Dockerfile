# sub-sift 本地 Docker 模式镜像
#
# 运行形态：
#   /app            运行时工作区，由 git 浅克隆填充（代码 + 数据始终与 GitHub 一致）
#   /opt/sub-sift   镜像自带副本：web/sync 工具 + git 不可用时的降级来源
#   /app/data      卷挂载（CSV / state.json / mmdb）
#   /app/output    卷挂载（订阅输出，供局域网订阅）
#
# 核心依赖共用仓库根目录的 requirements.txt，与 GitHub Actions（云模式）行为一致。
FROM python:3.11-slim

# git  : 快照同步（fetch / checkout）
# curl : --update-geo 下载 mmdb
RUN apt-get update \
 && apt-get install -y --no-install-recommends git curl ca-certificates \
 && rm -rf /var/lib/apt/lists/*

WORKDIR /app

# 核心依赖（与 Actions 共用）
COPY requirements.txt /tmp/requirements.txt
RUN pip install --no-cache-dir -r /tmp/requirements.txt && rm /tmp/requirements.txt

# web 依赖（仅本地 Docker 模式使用，Actions 不装）
COPY docker/requirements.txt /tmp/requirements-web.txt
RUN pip install --no-cache-dir -r /tmp/requirements-web.txt && rm /tmp/requirements-web.txt

# 镜像自带副本：工具脚本 + 降级可用的项目代码
COPY main.py config.yaml /opt/sub-sift/
COPY modules/ /opt/sub-sift/modules/
COPY docker/sync.py docker/web.py /opt/sub-sift/

COPY docker/entrypoint.sh /usr/local/bin/entrypoint.sh
RUN chmod +x /usr/local/bin/entrypoint.sh

# /app = 运行时 git 工作区；/opt/sub-sift = 工具与降级副本
ENV PYTHONPATH=/app:/opt/sub-sift \
    PYTHONUNBUFFERED=1 \
    TZ=UTC \
    REPO_URL=https://github.com/ypj034/sub-sift.git \
    REPO_BRANCH=main \
    SYNC_INTERVAL_HOURS=0 \
    SYNC_BUFFER_MINUTES=5 \
    SYNC_POLL_SECONDS=180 \
    SYNC_MAX_WAIT_MINUTES=120 \
    EDIT_TRIGGER_ACTIONS=true \
    WEB_PORT=8080

EXPOSE 8080
VOLUME ["/app/data", "/app/output"]

ENTRYPOINT ["/usr/local/bin/entrypoint.sh"]
