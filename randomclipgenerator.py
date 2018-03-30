#!/usr/bin/python

# Random Video Clips Player
# By marq_
# Based on code by @author niknow

import subprocess
import xml.etree.cElementTree as ET
import os
import random


xmlplaylistfile = "clips.xspf"
subfolder = "videos"
numclips = 20
intervalmin = 4
intervalmax = 17


"""
For all files under folder "videos",
Do many times:
    Select a video at random.
    Select a starting point for it at random.
    Select a duration between 5-15 sec at random.
    Add this info to playlist file.
Execute VLC and play it.
To play prevoiusly generated playlists add them to batch file execvlc.bat.
"""

# By @author eyquem
def line_prepender(filename,line):
    with open(filename,'r+') as f:
        content=f.read()
        f.seek(0,0)
        f.write(line.rstrip('\r\n')+'\n'+content)
#

ffprobestr = ("ffprobe -v error -select_streams v:0 -show_entries stream=duration " +
              "-of default=noprint_wrappers=1:nokey=1 ")

# Create a list of all files in folder 'videos':
Videos = os.listdir(subfolder)

playlist = ET.Element("playlist", version="1", xmlns="http://xspf.org/ns/0/")
trackList = ET.SubElement(playlist, "trackList")

for q in range(numclips):
    # Choose a random file number:
    selected = random.randint(0, len(Videos) - 1)

    # Create path to current video file:
    videofile = os.path.join(subfolder, Videos[selected]).replace("\\","/")

    # Get the duration of that video:
    getdurationcmd = ffprobestr + videofile
    proc = subprocess.Popen(getdurationcmd, stdout=subprocess.PIPE, shell=True)
    (out, err) = proc.communicate()
    duration = str(out).split(".")[0].split("b'")[1]

    # Select a starting point from begining of video to end of video - 15sec:
    beginat = random.randint(0, int(duration) - intervalmax)

    # Select a clip length:
    cliplength = random.randint(intervalmin, intervalmax)
    playto = beginat + cliplength

    # Add the clip to the playlist:
    track = ET.SubElement(trackList, "track")
    ET.SubElement(track, "location").text = "file:///C:/CDATA/Videos/" + videofile
    extension = ET.SubElement(track, "extension", application="http://www.videolan.org/vlc/playlist/0")
    ET.SubElement(extension, "vlc:option").text = "start-time=" + str(beginat)
    ET.SubElement(extension, "vlc:option").text = "stop-time=" + str(playto)
    ET.SubElement(extension, "vlc:option").text = "no-audio"
#

# Create xml file:
ET.ElementTree(playlist).write(xmlplaylistfile)
line_prepender(xmlplaylistfile, "<?xml version=\"1.0\" encoding=\"UTF-8\"?>")

# Open VLC with playlist:
subprocess.call("exevlc.bat " + xmlplaylistfile)


