""" Random video clips player for Win10. """

import os
import random
import subprocess
import sys
import xml.etree.ElementTree as ET
from subprocess import Popen

XML_PLAYLIST_FILE = 'clips.xspf'
SUBFOLDER = 'videos'
NUMBER_OF_CLIPS = 5
INTERVAL_MIN = 4
INTERVAL_MAX = 8
CURRENT_DIRECTORY = os.path.dirname( os.path.abspath(__file__) )


def prepend_line(filename: str, line: str) -> None:
    """ Append line to beginning of file. """
    assert filename, f"Cannot prepend line: '{line}' to invalid {filename}. "
    if line is not None and len(line) > 0:
        with open(filename, 'r+', encoding='utf-8') as file:
            content = file.read()
            file.seek(0,0)
            file.write( line.rstrip("\r\n") + "\n" + content )


def list_files_subfolder() -> list:
    """ Create a list of all files in SUBFOLDER (videos). """
    subfolder_contents = os.listdir(SUBFOLDER)
    if subfolder_contents is None or len(subfolder_contents) < 1:
        print(f"There are no files under {SUBFOLDER}. ")
        sys.exit()
    return subfolder_contents


def select_video_at_random(list_of_files: list) -> str:
    """ Choose a video. :return: Video filename with Win full path. """
    assert list_of_files and SUBFOLDER
    subpath = os.path.join(CURRENT_DIRECTORY, SUBFOLDER)
    selected = random.randint(0, len(list_of_files) - 1)
    return ( os.path.join(subpath, list_of_files[selected]) ).replace("\\", "/")


def get_video_duration(num_to_log: int, video: str) -> int:
    """ Extract video duration with ffprobe and subprocess.Popen.
        :return: Video duration in seconds. """
    assert video
    ffprobe_str = "ffprobe -v error -select_streams v:0 \
        -show_entries stream=duration -of default=noprint_wrappers=1:nokey=1"
    command = f"{ffprobe_str} {video} "
    with Popen(command, stdout=subprocess.PIPE) as process:
        (out, err) = process.communicate()
    if err:
        print(f"Process error: [{str(err)}]. Iteration: {num_to_log}. ")
    result = ( ( ( ( str(out) ).split('.', maxsplit=1) )[0] ).split("b'") )[1]
    seconds = int(result)
    assert INTERVAL_MIN < seconds > 0, f"Video too short: {video} "
    return seconds


def choose_starting_point(video_length: int) -> int:
    """ Choose beginning of clip.
    :return: Starting point from beginning of video to end of video - max. """
    assert video_length > 0
    return random.randint(0, video_length - INTERVAL_MAX)


def add_clip_to_tracklist(track_list: ET.Element, \
    video: str, start: int, end: int) -> None:
    """ Add clip (track) to playlist.trackList sub element tree and mute.
        :param: track_list: Contains the clips.
        :param: video: The name of the video file to be cut.
        :param: start: Begin clip from.
        :param: end: Stop clip at. """
    assert track_list is not None and video and start >= 0
    track = ET.SubElement(track_list, 'track')
    ET.SubElement(track, 'location').text = f"file:///{video}"
    extension = ET.SubElement(track, 'extension', \
        application='http://www.videolan.org/vlc/playlist/0')
    ET.SubElement(extension, 'vlc:option').text = f"start-time={start}"
    ET.SubElement(extension, 'vlc:option').text = f"stop-time={end}"
    ET.SubElement(extension, 'vlc:option').text = 'no-audio'


def create_xml_file(playlist_et: ET.Element) -> None:
    """ Finally write the playlist tree element as an xspf file to disk. """
    ET.ElementTree(playlist_et).write(XML_PLAYLIST_FILE)
    prepend_line(XML_PLAYLIST_FILE, '<?xml version="1.0" encoding="UTF-8"?>')


def generate_random_video_clips_playlist(video_list: list) -> ET.Element:
    """
    * Create playlist as an xml element tree.
    * Create tracklist as subelement of playlist. This contains the clips.
    * For each clip to be generated:
        + Select a video at random.
        + Choose beginning and end of clip from selected video.
        + Add clip to playlist.
    """
    assert video_list

    playlist = ET.Element("playlist", version="1", xmlns="http://xspf.org/ns/0/")
    tracks = ET.SubElement(playlist, "trackList")

    assert 1 <= NUMBER_OF_CLIPS < sys.maxsize, \
        "Invalid number of clips: {NUMBER_OF_CLIPS} "

    for iteration in range(NUMBER_OF_CLIPS):
        video_file = select_video_at_random(video_list)
        duration = get_video_duration(iteration, video_file)

        begin_at = choose_starting_point(duration)
        clip_length = random.randint(INTERVAL_MIN, INTERVAL_MAX)
        play_to = begin_at + clip_length

        add_clip_to_tracklist(tracks, video_file, begin_at, play_to)

    return playlist


def execute_vlc() -> None:
    """ Call VLC only once and pass it the xspf playlist. """
    executable = os.path.join(CURRENT_DIRECTORY, 'exevlc.bat')
    with Popen([executable, f"{CURRENT_DIRECTORY}/{XML_PLAYLIST_FILE}"]):
        pass


def verify_intervals_valid() -> None:
    """ Music video clips should be between at most 15 to 25 seconds long. """
    assert 15 >= INTERVAL_MIN >= 1
    assert 25 >= INTERVAL_MAX >= 1


def main():
    """
    * Get list of videos.
    * Generate an xml playlist with random clips from those videos.
    * Run VLC with that playlist.
    """
    verify_intervals_valid()
    files = list_files_subfolder()
    top_element = generate_random_video_clips_playlist(files)
    create_xml_file(top_element)
    execute_vlc()

if __name__ == "__main__":
    main()
