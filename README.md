# record-critrole
Record Twitch.tv shows on Windows, Ubuntu 18.04+ (or similar)

In essence, this is a CLI wrapper to call `streamlink`. As of writing this, it offers more reliable recordings by auto-retrying if connection is lost or the stream disconnects.

Allows you to set a duration (optional) and a time until recording (optional).

There are files with .py for both windows/linux, a linux shell .sh script + cronjob and a  windows batch .bat + scheduled task. 

Initially created to record [Critical Role](https://critrole.com). One feature is to parse the website http://wheniscriticalrole.com to see when the show airs.

## record.py

```
❯ python3 record.py --help
usage: record.py [-h] [-u URL] [-o OUT_DIR] [-s SLEEP_TIME] [-n] [--offset OFFSET]

Process arguments

options:
  -h, --help            show this help message and exit
  -u URL, --url URL     url to twitch channel
  -o OUT_DIR, --out OUT_DIR
                        directory where to save video
  -s SLEEP_TIME, --sleep SLEEP_TIME
                        time to sleep in seconds before recording starts
  -n, --now             start recording right now
  --offset OFFSET       amount of minutes to start recording before stream is online. Default is 5

```

## TODO
- [ ] Package with PyInstall. Has support for python3+, Windows and Linux, one file
executable
- [x] Rewriting below scripts into python only
- [x] Read time until critical role from website
- [x] Update cronjob to launch python script in virtualenv
## Requirements

[Streamlink](https://github.com/streamlink/streamlink)

```
(optional) Selenium with Firefox driver to parse wheniscriticalrole.com
```
(example) python3 record.py -u twitch.tv/criticalrole -w 3600 -o outdir
```
Omitting `-n` or `-w` option defaults to using Selenium to parse the above
mentioned website and gets the most accurate time automatically. You will need
Selenium and a Firefox driver available in your Path
