#!/bin/bash
# update_file filename "Find String" "Replace String"
update_file() {
  cat $1 | sed -e "s/$2/$3/" > /f
  mv /f $1
}

# us keyboard 
update_file /etc/default/keyboard "XKBLAYOUT=\"gb\"" "XKBLAYOUT=\"us\""

echo "Keyboard country set to US.  This will be affected on next reboot" 

