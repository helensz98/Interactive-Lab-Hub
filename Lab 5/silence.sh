ffmpeg -f lavfi -i anullsrc=r=44100:cl=mono -t 0.5 -q:a 9 -acodec libmp3lame out.mp