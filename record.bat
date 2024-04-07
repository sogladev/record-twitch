@echo off

REM Set working directory
cd /D K:\videos\criticalrole

REM Set parameters
set WAIT=1
set DURATION=12600
set CHANNEL=criticalrole

REM Get current date
set CUR_YYYY=%date:~10,4%
set CUR_MM=%date:~4,2%  
set CUR_DD=%date:~7,2%

REM Get current time
set CUR_HH=%time:~0,2%

REM Build filename 
set FILEDATE=%CUR_YYYY%-%CUR_MM%-%CUR_DD%

REM Set title
title Recording - %CHANNEL% %FILEDATE% 

REM Wait before recording
timeout /T %WAIT% /NOBREAK

REM Start loop to record multiple files
set COUNTER=1
:loop
streamlink twitch.tv/%CHANNEL% best -o "%CHANNEL%_%FILEDATE%_%COUNTER%.flv" --force -O --retry-streams 30 --retry-open 9999 --twitch-disable-hosting
timeout 30
set /A COUNTER+=1
if %COUNTER% LEQ 10 goto loop

REM Add shutdown after recording if needed
REM shutdown -s -f -t %DURATION%

:endofcomment

