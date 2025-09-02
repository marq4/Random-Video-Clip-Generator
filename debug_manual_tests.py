"""
This script is executed if Pytest fails.
Cannot be executed locally as the Google API key is a secret stored in GitHub.
"""

import sys

from youtube_utils import (GOOGLE_API_KEY, invalid_url_should_fail,
                           verify_videos_exist)


def main() -> None:
    """
    * Get KEY env var.
    * Execute tests.
    """
    if not GOOGLE_API_KEY:
        print('Unable to import YouTube API key from common module. ')
        sys.exit(1)
    if verify_videos_exist(GOOGLE_API_KEY):
        print('Success: all YouTube videos listed were found. ')
    else:
        print('Failure: NOT all YouTube videos listed were found. ')
    if invalid_url_should_fail(GOOGLE_API_KEY) is False:
        print('Success: Negative test (invalid URL) completed as expected. ')
    else:
        print('Failure: invalid URL should fail! ')
#

if __name__ == '__main__':
    main()
