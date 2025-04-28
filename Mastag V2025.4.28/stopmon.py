import subprocess

import os

cmd="gnome-terminal --command='"'bash -c "'"sudo airmon-ng check kill;sudo systemctl start NetworkManager;sudo airmon-ng stop wlan0; sleep 1"'"'"'"
os.system(cmd)
