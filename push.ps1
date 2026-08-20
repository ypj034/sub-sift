# 默认推送策略：只推代码，不推本地跑出来的数据。
# data/ 与 output/ 由 GitHub Actions 定时维护（chore(data) 提交），
# 本地运行 main.py 仅用于验证，结果默认不推送，避免覆盖服务器数据。
# 用法: powershell -ExecutionPolicy Bypass -File push.ps1
$ErrorActionPreference = "Stop"
Set-Location $PSScriptRoot

# 丢弃本地数据/输出文件的未提交修改（恢复到最近一次提交的版本）
git restore --staged --worktree -- data/ output/

# 拉取远端（可能含 Actions 数据提交）后推送代码
git pull --rebase origin main
git push origin main
