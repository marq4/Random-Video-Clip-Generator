""" Initialize Google API key from OS environment (GitHub secret). """

import os
import sys

GOOGLE_API_KEY = os.environ.get("GOOGLEAPIYOUTUBEKEY")

if GOOGLE_API_KEY is None:
    print('YouTube API key not found on OS environment variables. ')
    sys.exit(1)
