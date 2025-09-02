""" Verify video URL is valid and video exists. """

import requests

pattern = '"playabilityStatus":{"status":"ERROR","reason":"Video unavailable"'
url = $1 %%%

def test_new_url(url):
    request = requests.get(url)
    return False if pattern in request.text else True
