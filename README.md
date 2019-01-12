# record-critrole
Info to record [Critical Role](https://critrole.com) on Windows or on a Ubuntu 18.04 (or similar)
system.

Your pc must be on while running either method.

## Requirements
[Twitch oauth token](https://twitchapps.com/tmi/)


[Streamlink](https://github.com/streamlink/streamlink)

Read the docs:
* For Windows click to [`releases/`](https://github.com/streamlink/streamlink/releases)

* For Ubuntu 18.04 (or similar) run `sudo pip install streamlink`

## Windows
Edit `record.bat` and change the following settings inside the script

1. Use `cd` to navigate to output folder where streamlink will be called
2. `WAIT` this is the amount of seconds until critical role airs
I use [wheniscriticalrole](http://www.wheniscriticalrole.com/) and convert to seconds and subtract
about 600 (10mins) to start recording slightly earlier.
3. `EPISODE` to name file correctly
4. `DURATION` (optional) give e.g. 5 hours in seconds to record for 5 hours and
   then shutdown pc if shutdown command is added

Run the script AND turn it off manually or it will keep recording the
channel after the episode is finished. You can run a `shutdown -s -f -t
WAIT+5*3600` to shutdown your pc after 5 hours of recording.   

You must change the `WAIT` everytime and run manually. You can setup a
scheduled task for this similar to the one below.


## Ubuntu 18.04 or similar
Modify `record.sh` and cronjob `cronjob.txt`

Change path to record.sh `/home/user/scheduled_jobs/record.sh`

Change output dir of video `/home/user/Videos/criticalrole/`

### Setup cronjob
`cronjob.txt` contains settings needed to run `record.sh` and output video to
the folder. 

`PATH` is your $PATH variable (`echo $PATH`). This is necessary to run the
`streamlink` application.

Modify `cronjob.txt` settings and paste to `cronjob -e`

`50 3 * * 5 timeout 6h sh /home/user/scheduled_jobs/record.sh >> /home/user/scheduled_jobs/record.log 2>&1`

`50 3 * * 5` see [Crontab guru](https://crontab.guru/#50_3_*_*_5). `At 03:50 on
Friday` Critical Role airs at 4:00AM local time on Friday. Change the time accordingly to your timezone. I'm aware timezones can be set `America/Los_Angeles`. Sadly, this doesn't seem to work on my pc.

`timeout 6h` stops recording after 6 hours

`>> /home/user/scheduled_jobs/record.log 2>&1` (optional) writes the stdout to log. This line can be omitted.

### Modify `record.sh`
`record.sh` set your AUTH_TOKEN or config in streamlink cfg. Set `OUTDIR` to
where you want the video saved.
