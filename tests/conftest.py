"""
Define fixture functions to make them accessible across multiple test files.
"""

import pytest


def pytest_addoption(parser):
    """ Pass different values to a test function via command line option. """
    parser.addoption("--video_url", action="store")


def pytest_generate_tests(metafunc):
    """ This is called for every test.
    Only get/set command line arguments if the argument is specified
    in the list of test "fixturenames". """
    option_value = metafunc.config.option.video_url
    if 'video_url' in metafunc.fixturenames and option_value is not None:
        metafunc.parametrize("video_url", [option_value])
