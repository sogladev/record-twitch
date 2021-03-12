@echo off
K: & cd videos/criticalrole
set CHANNEL=criticalrole
set CUR_YYYY=%date:~10,4%
set CUR_MM=%date:~4,2%
set CUR_DD=%date:~7,2%
set CUR_HH=%time:~0,2%
set FILEDATE=%CUR_YYYY%-%CUR_MM%-%CUR_DD%
set AUTH_TOKEN=v15mfub562jxtj2hapqu640vaogegt 
title Recording - %CHANNEL% %FILEDATE%
set COUNTER=1
:loop
streamlink twitch.tv/%CHANNEL% best -o "%CHANNEL%_%FILEDATE%_%COUNTER%.flv" --force -O --retry-streams 30 --retry-open 9999 --twitch-disable-hosting
timeout 30
set /A COUNTER=COUNTER+1
goto loop
