""" Remove spaces and special characters from file names. """

import os
import re

# ignore = [os.path.basename(__file__), 'random_clip_generator.py', 'exevlc.bat']

for original in os.listdir("."):
    if original == os.path.basename(__file__) \
        or original == 'random_clip_generator.py' \
        or original == 'exevlc.bat':
        continue
    sanitized = re.sub(r"[^a-zA-Z0-9\.]", '', original)
    if sanitized != original:
        os.rename(original, sanitized)
