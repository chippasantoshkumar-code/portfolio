@echo off
title Santhosh Kumar Chippa - Portfolio Server
echo ========================================================
echo   Santhosh Kumar Chippa - Multi-Device Portfolio Server
echo ========================================================
echo.
echo Launching server and opening your browser...
start http://localhost:8080
echo.
python serve_network.py
pause
