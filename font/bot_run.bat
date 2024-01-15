@echo off
cd %~dp0.venv\Scripts
call activate
cd %~dp0
set API_TOKEN=6986334072:AAGMZb56UWSHBTpSWVOur8Q5KyuHiDecBGY
python main.py
pause
