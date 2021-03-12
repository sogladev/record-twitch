@echo off
K: & cd videos/criticalrole
set WAIT=1
set DURATION=12600
set CHANNEL=criticalrole
set CUR_YYYY=%date:~10,4%
set CUR_MM=%date:~4,2%
set CUR_DD=%date:~7,2%
set CUR_HH=%time:~0,2%
set FILEDATE=%CUR_YYYY%-%CUR_MM%-%CUR_DD%
goto endofcomment
    change parameters above^: 
	use cd to navigate to directory where to save recording
	WAIT=amount of seconds until start recording
	EPISODE=episode counter
        DURATION=duration of recording in seconds. (6=21600, 5=18000, 4.5=16200)
	insert line "shutdown -s -f -t %DURATION%" after timeout to limit recording time
:endofcomment
title Recording - %CHANNEL% %FILEDATE%
timeout /T %WAIT% /NOBREAK
set COUNTER=1
:loop
streamlink twitch.tv/%CHANNEL% best -o "%CHANNEL%_%FILEDATE%_%COUNTER%.flv" --force -O --retry-streams 30 --retry-open 9999 --twitch-disable-hosting
timeout 30
set /A COUNTER=COUNTER+1
goto loop
