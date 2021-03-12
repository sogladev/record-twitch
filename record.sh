#!/bin/sh
URL=twitch.tv/geekandsundry
OUTDIR=/home/user/Videos/criticalrole/
cd $OUTDIR
while true
do
    TIME=$(date +%Y-%m-%d_%H:%M:%S)
    streamlink $URL best -o "$TIME.flv" --force -O --retry-streams 30 --retry-open 9999
    rleep 30
done
