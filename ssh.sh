#!/bin/bash
# update_file filename "Find String" "Replace String"
update_file() {
  cat $1 | sed -e "s/$2/$3/" > /f
  mv /f $1
}

# permit ssh login  
touch /boot/ssh
# permit root ssh login
update_file /etc/ssh/sshd_config "#PermitRootLogin prohibit-password" "PermitRootLogin yes"
echo "root:raspberry" | sudo chpasswd
echo "pi:raspberry1" | sudo chpasswd
echo "ssh.sh completed"

