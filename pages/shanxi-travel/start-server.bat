@echo off
chcp 65001 >nul
echo ============================================
echo   旅行计划本地服务器启动中...
echo ============================================
echo.
echo 正在启动 HTTP 服务器，端口 3456...
echo 启动后请用浏览器打开：
echo   http://localhost:3456/
echo.
echo 按 Ctrl+C 停止服务器
echo.
python -m http.server 3456
