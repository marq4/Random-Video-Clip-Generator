""" Common module for both Pytest and debug_manual tests. """

import os
from typing import List

import requests

API = "https://www.googleapis.com/youtube/v3/videos"
GOOGLE_API_KEY = os.environ["GOOGLEAPIYOUTUBEKEY"]


def get_response(google_api_key: str, video_id: str) -> str:
    """ Call YouTube API. """
    call_string = f"{API}?id={video_id}&part=id&key={google_api_key}"
    response = requests.get(call_string, timeout=6)
    return response
#

def check_response_valid(response: str) -> bool:
    """ Valid responses have at least one item. """
    if len(response.json()['items']) < 1:
        return False
    return True
#

def get_list_of_videos() -> List[str]:
    """ Read from YouTube music video list text file. """
    video_list = []
    with open('List.md', 'r', encoding='utf-8') as video_list_text_file:
        for line in video_list_text_file.readlines():
            if line.startswith('https'):
                video_list.append(line.rstrip())
    return video_list
#

def transform_into_list_of_ids(video_list: list) -> List[str]:
    """ Parse URLs into just the YouTube video ids. """
    id_list = []
    pattern = 'v='
    for url in video_list:
        parts = url.split(pattern, 1) # Split once.
        if len(parts) > 1:
            id_list.append(parts[1])
        else:
            # Invalid URL found.
            return False
    return id_list
#

def verify_videos_exist(google_api_key: str) -> bool:
    """ Get all video URLs in a list. Check each one. """
    videos = get_list_of_videos()
    ids = transform_into_list_of_ids(videos)
    for video_id in ids:
        response = get_response(google_api_key, video_id)
        if not check_response_valid(response):
            print(f"YouTube video NOT found: {video_id}! ")
            return False
        print(f"YouTube video found: {video_id}. ")
    return True
#

def invalid_url_should_fail(google_api_key: str) -> bool:
    """ Negative test to avoid false positives. """
    non_existent_youtube_video_id = "09vuCByb6js"
    response = get_response(google_api_key, non_existent_youtube_video_id)
    return check_response_valid(response)
#
