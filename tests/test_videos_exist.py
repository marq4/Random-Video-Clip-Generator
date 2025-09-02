"""
Verify video URLs are valid and videos exist.
No main, Pytest will run all functions that stat witg 'test'.
"""

import pytest
from youtube_utils import GOOGLE_API_KEY, verify_videos_exist, invalid_url_should_fail


@pytest.mark.integration
def test_videos_exist() -> bool:
    """
    Goes to YouTube and checks if videos listed in music video list test file exist.
    """
    assert verify_videos_exist(GOOGLE_API_KEY)
#

@pytest.mark.integration
def test_invalid_url_should_fail() -> bool:
    """
    Negative test: invalid YouTube music video id should fail.
    """
    assert invalid_url_should_fail(GOOGLE_API_KEY) is False
