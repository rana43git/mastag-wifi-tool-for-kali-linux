import subprocess

import os

cmd="gnome-terminal --command='"'bash -c "'"sudo wash -i wlan0mon; sleep 60"'"'"'"
os.system(cmd)
