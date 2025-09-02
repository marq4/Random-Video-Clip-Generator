""" Verify video URLs are valid and videos exist. """

import requests
import os

API = 'https://www.googleapis.com/youtube/v3/videos'

def get_response(google_api_key: str, video_id: str) -> str:
    """ Call YouTube API. """
    response = requests.get(f"{API}?id={video_id}&part=id&key={google_api_key}")
    return response
#

def check_response_valid(response: str) -> bool:
    """ Valid responses have at least one item. """
    if len(response.json()['items']) < 1:
        return False
    return True
#

def test_invalid_url_should_fail(google_api_key: str) -> bool:
    """ Negative test to avoid false positives. """
    non_existent_youtube_video_id = "09vuCByb6js"
    response = get_response(google_api_key, non_existent_youtube_video_id)
    return check_response_valid(response):
#

def test_verify_videos_exist(google_api_key: str) -> bool:
    """ Get all video URLs in a list. Check each one. """
    videos = []
    with open('List.md', 'r') as video_list_text_file:
        for line in video_list_text_file.readlines():
            if line.startswith('https'):
                videos.append(line.rstrip())
    #print(f"{videos=}")#TMP
    ids = []
    pattern = 'v='
    for url in videos:
        parts = url.split(pattern, 1) # Split once.
        if len(parts) > 1:
            ids.append(parts[1])
        else:
            # Invalid URL found.
            return False
    #print(f"{ids=}")#TMP
    #ids.append('s76dc8udch98d') #TMP: should fail. TODO: negative test.  
    for video_id in ids:
        response = get_response(google_api_key, video_id)
        if not check_response_valid(response):
            return False
        print(f"YouTube video found: {video_id}")#TMP: I just want to verify it is really working.    
    return True
#

def main() -> None:
    """
    * Get KEY env var.
    * Execute test.
    """
    google_api_key = os.environ.get('GOOGLEAPIYOUTUBEKEY')
    if not google_api_key:
        print(f"YouTube API key not found on OS environment variables. ")
        exit(1)
    test_verify_videos_exist(google_api_key)
    assert test_invalid_url_should_fail(google_api_key) == False
#

if __name__ == '__main__':
    main()

