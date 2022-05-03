# Random Video Clip Generator (Windows) 
Plays random sections of videos for background visual noise.
Great for parties.

You will need:
* Python.
* FFmpeg.
* VLC.
* The videos have to be locally available. 

### How to use: ### 
1. Install ffmpeg by following this guide: https://www.geeksforgeeks.org/how-to-install-ffmpeg-on-windows 
2. Install python by following this guide: https://phoenixnap.com/kb/how-to-install-python-3-windows 
3. Install VLC (video player): https://www.videolan.org/vlc/download-windows.wa.html 
4. Download a couple of YT videos (from the list if you want). 
5. Download this program by doing Code > Download ZIP. 
6. Unzip it. 
7. Create a subfolder named videos and download the music videos there. You'll need at least 1000 videos for an hour of playback with low repeats. 
8. Clean the video file names (as they can't have spaces or '-') with the auxiliary script:  
    1. Copy sanitize_video_titles.py into the subfolder with the videos. 
    2. Open a command prompt. 
    3. Navigate into that folder (e.g.: cd C:\Users\YourUser\Videos\Random-Clip-Generator-main\videos). 
    4. Type this in the command prompt: python sanitize_video_titles.py 
    5. Verify no video file contains spaces or special characters. 
    6. Remove the copy of sanitize_video_titles.py from step 8.1 above. 
9. Edit file random_clip_generator.py. For an initial test run it's recommended to specify 5 clips or so. Personalize:
* The name of the xml file to be generated (playlist). Default is 'clips'. 
* The name of the subfloder that contains all video files. Default is 'videos'. 
* The number of clips to be added to the playlist. About 1000 are needed for 1 hour of playback (depending on the min and max specified bellow). 
* The minimum clip duration in seconds. Recommended = 4.  
* The maximum clip duration in seconds. Recommended = 8. (Greater may cause problems as people recognize the video and may ask you to change the audio to match the visuals.) 
10. Run the main script to generate the playlist: 
    1. Navigate out of the videos subfolder (e.g.: cd ..). 
    2. Type this in the command prompt: python random_clip_generator.py  

Please feel free to create pull requests to add your own videos to the list of recommended (1080p or higher. Should be either colorful and fun or stylistic), or create your own branch with its own list that's relevant to you. 
