sudo apt-get -y install samba samba-common-bin
mkdir -m 0777 /share
mkdir -m 0777 /share/data
mkdir -m 1777 /share/data/saved
if grep -Fxq "[share]" /etc/samba/smb.conf
then
   echo "/etc/samba/smb.conf already has [share] defined"
else
   echo "adding [share] to /etc/samba/smb.conf" 
   cat >> /etc/samba/smb.conf <<EOF
[share]
Comment = Pi shared folder
Path = /share
Browseable = yes
Writeable = yes
only guest = no
create mask = 0777
directory mask = 0777
Public = yes
Guest ok = yes

EOF
fi
# create samber user: root and set password
(echo "raspberry";echo "raspberry") | smbpasswd -a root
# restart samba
/etc/init.d/samba restart
