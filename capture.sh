#!/bin/sh

if [ $1 ]
then
sleep $1
fi

name=`date +%Y-%m-%d-%H-%M`
fullscreen=$(xwininfo -root | grep 'geometry' | awk '{print $2}' | awk '{ print $1 } BEGIN { FS="+" }')
#echo $fullscreen
#fmpeg -f alsa -ac 2 -i pulse -f x11grab -r 5 -s $fullscreen -i :0.0 -acodec pcm_s16le -vcodec libx264 -preset ultrafast -threads 2 -y $name.mkv 
ffmpeg -f alsa -ac 2 -i pulse -f x11grab -r 5 -s 1920x1080 -i :0.0 -acodec pcm_s16le -vcodec libx264 -preset ultrafast -threads 2 -y $name.mkv

