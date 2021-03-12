record.py [![Build Status](https://travis-ci.com/Jelle-M/record-twitch.svg?branch=master)](https://travis-ci.com/Jelle-M/record-twitch)

# record-critrole
Info to record Twitch.tv shows on Windows or on a Ubuntu 18.04 (or similar)
system.

In essence, this is a CLI wrapper to call `streamlink v2.0.0`. It offers more reliable
recording and allows you to set a duration (optional) and a time until
recording (optional).

There are files with .py for both windows/linux, a linux shell .sh script + cronjob and a  windows batch .bat + scheduled task. 

Initially created to record [Critical Role](https://critrole.com). One feature is to parse the website http://wheniscriticalrole.com to see when the show airs.

## TODO
GUI with PyQT5. Fastest and easiest for required functionality. TKTinker feels
like too much work to learn.

Package with PyInstall. Has support for python3+, Windows and Linux, one file
executable. PyInstall method failed due to not having streamlink installed.
Tried adding dependencies to hidden_imports in .spec file, but to no avail.

Docker seems overkill. Mostly due to size of >100MB. Run from a virtual environment instead. 

- [x] Rewriting below scripts into python only
- [x] Read time until critical role from website
- [x] Update cronjob to launch python script in virtualenv
## Essential Requirements
[Twitch oauth token](https://twitchapps.com/tmi/)

[Streamlink](https://github.com/streamlink/streamlink)

Read the docs:
* For Windows click to [`releases/`](https://github.com/streamlink/streamlink/releases)

* For Ubuntu 18.04 (or similar) run `sudo pip install streamlink`

### Windows task scheduler
Set a weekly trigger 5mins before shows goes live with the action to start `recordT_manager.bat` with optional arg (default=2000 or 5.5hrs) duration of recording. 

### Python3.6 (**RECOMMENDED**) (Ubuntu 18.04 and Windows 10)
Required:
```
streamlink
python3.6 
dependencies listed in `requirements.txt` 
(optional) Selenium with Firefox driver
```

Setup environment
```
(optional) mkvirtualenv -p /usr/bin/python3.6 <env-name> 
(required) pip3 install -r requirements.txt
(example) python3 record.py -u twitch.tv/geekandsundry -o outdir
-w 3600
```
By default `-u` is set as `twitch.tv/geekandsundry`

`-t` if not set, `--twitch-oauth-token` when calling streamlink will not be set and will use token set in streamlink config

`-o /home/user/Videos/criticalrole` to specify folder (folder must exist). Paths can be POXIX or Windows format. Thanks to `pathlib`.

`-n` start recording right now (overrides `- w` option)

`-w` amount of seconds to wait until start recording. Check
[wheniscriticalrole.com](https://wheniscriticalrole.com)

Omitting `-n` or `-w` option defaults to using Selenium to parse the above
mentioned website and gets the most accurate time automaticly. You will need
Selenium and a Firefox driver available in your Path. (google how to setup or
make sure to use either of these 2 arguments)
