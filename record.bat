@echo off
D: & cd videos/criticalrole 
set WAIT=19800
set EPISODE=s2e40
set AUTH_TOKEN=paste_token_here
set DURATION=12600
goto endofcomment
    change parameters above^: 
	use cd to navigate to directory where to save recording
	WAIT=amount of seconds until start recording
	EPISODE=episode counter
	AUTH_TOKEN=your twitch authentication token (google how to get this)
        DURATION=duration of recording in seconds. (6=21600, 5=18000, 4.5=16200)
	insert line "shutdown -s -f -t %DURATION%" after timeout to limit recording time
:endofcomment
title Recording - Critical Role %EPISODE%
timeout /T %WAIT% /NOBREAK
set COUNTER=1
:loop
streamlink --twitch-oauth-token %AUTH_TOKEN% twitch.tv/geekandsundry best -o "criticalrole_%EPISODE%_%COUNTER%.flv" --force -O --retry-streams 30 --retry-open 9999
timeout 30
set /A COUNTER=COUNTER+1
goto loop

