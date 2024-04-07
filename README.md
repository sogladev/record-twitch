# record-critrole
Record Twitch.tv shows on Windows, Ubuntu 18.04+ (or similar)

In essence, this is a CLI wrapper to call `streamlink`. As of writing this, it offers more reliable recordings by auto-retrying if connection is lost or the stream disconnects.

Allows you to set a duration (optional) and a time until recording (optional).

There are files with .py for both windows/linux, a linux shell .sh script + cronjob and a  windows batch .bat + scheduled task. 

Initially created to record [Critical Role](https://critrole.com). One feature is to parse the website http://wheniscriticalrole.com to see when the show airs.

## TODO
- [ ] Package with PyInstall. Has support for python3+, Windows and Linux, one file
executable
- [x] Rewriting below scripts into python only
- [x] Read time until critical role from website
- [x] Update cronjob to launch python script in virtualenv
## Requirements

[Streamlink](https://github.com/streamlink/streamlink)

```
(optional) Selenium with Firefox driver
```
(example) python3 record.py -u twitch.tv/criticalrole -w 3600 -o outdir
```
Omitting `-n` or `-w` option defaults to using Selenium to parse the above
mentioned website and gets the most accurate time automatically. You will need
Selenium and a Firefox driver available in your Path