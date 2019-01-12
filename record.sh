#!/bin/sh
URL=twitch.tv/geekandsundry
AUTH_TOKEN=YOUR_AUTH_TOKEN or set auth token in streamlink cfg (google this)
OUTDIR=/home/user/Videos/criticalrole/
cd $OUTDIR
while true
do
    TIME=$(date +%Y-%m-%d_%H:%M:%S)
    streamlink --twitch-oauth-token $AUTH_TOKEN $URL best -o "$TIME.flv" --force -O --retry-streams 30 --retry-open 9999
    rleep 30
done
