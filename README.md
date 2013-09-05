screen_capture
==============

Very simple screen capture program. Uses ffmpeg, X and x264.

Capturing parameters
--------------------
- libx264 codec;
- 30 fps;
- fullscreen resolution;
- ultrafast preset (low CPU usage, low compression);
- lossless;

Usage
-----
```
python scr_capture.py DESTINATION.mkv
```

If you want to just run 
``` 
./scr_capture.py DESTINATION.mkv
```
you need to make a module executable: 
```
chmod 001 scr_capture.py
```

TODO
----
- [ ] Make working under wayland;
- [ ] Capture sound;

See also
--------
If you like pure bash, you can use this script. 
```bash
#!/bin/sh
 
if [ $1 ]
then
sleep $1
fi
 
name=`date +%Y-%m-%d-%H-%M`
fullscreen=$(xwininfo -root | grep 'geometry' | awk '{print $2}' | awk '{ print $1 } BEGIN { FS="+" }')
 
ffmpeg -f alsa -async 1 -ac 2 -i hw:0,0 -f x11grab -r 30 -s $fullscreen -i :0.0 -acodec pcm_s16le -vcodec libx264 -preset ultrafast -threads 2 -y $name.mkv
```
