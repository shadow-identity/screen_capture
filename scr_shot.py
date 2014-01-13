#!/bin/python
# -*- coding: utf_8 -*-
import subprocess
from datetime import datetime
import time

delay = 5
command = ("import -window root 'scr {date_time}.png'")
while True:
    subprocess.call(command.format(date_time=datetime.now()), shell=True)
    time.sleep(delay)


