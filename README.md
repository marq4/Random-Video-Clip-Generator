# Random Clip Generator (Windows) 
Plays random sections of videos for background visual noise.
Great for parties.

You will need:
* Python.
* FFmpeg.
* VLC.
* The videos have to be locally available. 

Create a subfolder named videos and download the music videos there. 
You'll need at least 1000 videos for an hour of playback with low repeats. 
Use script sanitize_video_titles.py to clean the video file names as they can't have spaces or '-'. 

Edit file random_clip_generator.py to change:
* The name of the xml file to be generated (playlist). Default is 'clips'. 
* The name of the subfloder that contains all video files. Default is 'videos'. 
* The number of clips to be added to the playlist. About 1000 are needed for 1 hour of playback (depending on the min and max specified bellow). 
* The minimum clip duration in seconds. Recommended = 4.  
* The maximum clip duration in seconds. Recommended = 8. (Greater may cause problems as people recognize the video and may ask you to change the audio to match the visuals.)

Please feel free to create pull requests to add your own videos to the list of recommended (1080p or higher. Should be either colorful and fun or stylistic) or create your own branch with its own list that's relevant to you. 

