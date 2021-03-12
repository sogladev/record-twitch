@echo off
if "%1"=="" (
    set duration=20000
) else (
    set duration=%1
)
K:
start "recordT_task" recordT_task.bat
timeout /t %duration%
echo %duration% seconds are over. Terminating!
taskkill /FI "WINDOWTITLE eq recordT_task*"
pause