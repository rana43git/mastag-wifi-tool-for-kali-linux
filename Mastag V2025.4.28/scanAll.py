import subprocess

import os

cmd="gnome-terminal --command='"'bash -c "'"sudo airodump-ng wlan0; sleep 60"'"'"'"
os.system(cmd)
