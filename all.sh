# Note: run this with the command: sudo ./all.sh
if [[ "$EUID" -ne 0 ]]
then
 echo "Must be root, use sudo bash first"
 exit
fi

echo "apt-get update"
apt-get update -y
#echo "apt-get upgrade"
#apt-get upgrade -y
./keyboard.sh
#./timezone.sh
./ssh.sh
# ./crontab.sh
./ap.sh
#./samba.sh
# ./i2c.sh
# ./piHatHw535.sh
echo "Use raspi-config to enable i2c and spi, then run the examples"
echo "Modify /etc/rc.local to run your .py on startup"
echo "Please reboot your system"
