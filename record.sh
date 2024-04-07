#!/bin/sh

# Set variables
URL=twitch.tv/criticalrole
OUTDIR=/home/$USER/Videos/criticalrole/

# Change to output directory
cd $OUTDIR

# Download stream on loop
while true; do
    TIME=$(date +%Y-%m-%d_%H:%M:%S)
    streamlink $URL best -o "$TIME.flv" --force -O --retry-streams 30 --retry-open 9999
    sleep 30
done
