""" Verify video URLs are valid and videos exist. """

import requests
import os

API = 'https://www.googleapis.com/youtube/v3/videos'

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
        response = requests.get(f"{API}?id={video_id}&part=id&key={google_api_key}")
        #print(f"For {video_id} got: {response.json()['items'][0]}")#TMP
        if len(response.json()['items']) < 1:
            return False
        #print(f"For {video_id} got: {response.status_code}")#TMP: always returns 200.
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
#

if __name__ == '__main__':
    main()

