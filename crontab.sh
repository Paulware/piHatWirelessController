#!/bin/bash
if [ "$EUID" -ne 0 ]
  then echo "Must be root"
  exit
fi
echo "Adding * * * * * /usr/bin/python /var/www/html/Paulware/broadcastAddress.py to crontab"
echo "MAILTO=\"\"" > mycron
echo "@reboot cd /share/Multiplayer/Kai;node app.js" >> mycron
echo "@reboot cd /share/Multiplayer/Liam;node app.js" >> mycron
echo "@reboot cd /share/Multiplayer/template;node app.js" >> mycron
echo "@reboot cd /share/Multiplayer/newTactical;node app.js" >> mycron
crontab mycron
rm mycron
