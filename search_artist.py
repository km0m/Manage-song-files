# -*- coding: utf-8 -*-
"""
Created on Sun Mar  6 18:42:34 2022

@author: Koala
"""

import musicbrainzngs
import sys

agent_name = "password_test.py"
agent_version = "0.1"
# this script doesn't submit anything (empty dict)
# so testing this on live server (with live passwords) is okay.
musicbrainz_server = "test.musicbrainz.org"
#musicbrainz_server = "musicbrainz.org"

musicbrainzngs.set_useragent(
    "python-search-artist_example",
    "0.1",
    "https://github.com/km0m/Manage-song-files.git",
)

musicbrainzngs.set_rate_limit(limit_or_interval=1.0, new_requests=1)

musicbrainzngs.musicbrainz.VALID_RELEASE_STATUSES = ['official']

musicbrainzngs.get_artist_by_id('Oasis', includes=['recordings', 'releases', 'discids', 'media'])
