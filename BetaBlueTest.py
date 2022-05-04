#!/usr/bin/env python
import subprocess, sys

cmd=['rfcomm', 'connect', sys.argv[0], '1']

for i in range(0, 1001):
    subprocess.call(cmd)
print('Connecting...')
