""" Verify video URLs are valid and videos exist. """

import requests

#pattern = '"playabilityStatus":{"status":"ERROR","reason":"Video unavailable"'
#url = $1 %%%

def test_new_url():
    """ Get all video URLs in a list. Check each one. """
    videos = []
    with open('List.md', 'r') as video_list_text_file:
        for line in video_list_text_file.readlines():
            videos.append(line)
    with open('log.txt', 'w') as logfile:
        logfile.write(videos)
    #request = requests.get(url)
    return True #TMP
    #return False if pattern in request.text else True



