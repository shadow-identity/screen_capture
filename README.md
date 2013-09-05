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

TODO:
-----
- [ ] Make working under wayland;
- [ ] Capture sound;
