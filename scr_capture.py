#!/bin/python
# -*- coding: utf_8 -*-
import subprocess
import sys

# U can simply change fps
fps = 30

# get resolution
res = subprocess.check_output("xrandr | grep \*", shell=True).split()[0]

# ffmpeg command
command = ("ffmpeg -f x11grab -r {fps} -s {resolution} -i :0.0 -vcodec libx264 "
           "-preset ultrafast -crf 0 -threads 0 {filename}")

if len(sys.argv) <> 2:
    print "You must specify filename to save, for example:"
    print "{my_name} screencast.mkv".format(my_name=__file__)
    print "python {my_name} screencast.mkv".format(my_name=__file__)
    sys.exit(1)

sys.exit(subprocess.call(command.format(resolution=res,
                                        filename=sys.argv[1],
                                        fps=fps),
                         shell=True))
 


