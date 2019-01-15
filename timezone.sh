#!/bin/bash
# Get and set the timezone
TZ=`wget -O - -q http://geoip.ubuntu.com/lookup | sed -n -e 's/.*<TimeZone>\(.*\)<\/TimeZone>.*/\1/p'`
echo "Got a timezone of : $TZ"
cp /usr/share/zoneinfo/$TZ /etc/localtime