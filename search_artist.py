# -*- coding: utf-8 -*-
"""
Created on Sun Mar  6 18:42:34 2022

@author: Koala
"""

import musicbrainzngs
import getpass
import sys

agent_name = "search-artist.py"
agent_version = "0.1"
# this script doesn't submit anything (empty dict)
# so testing this on live server (with live passwords) is okay.
musicbrainz_server = "test.musicbrainz.org"
#musicbrainz_server = "musicbrainz.org"

musicbrainzngs.set_hostname(musicbrainz_server)
musicbrainzngs.set_useragent(
    agent_name,
    agent_version,
    "https://github.com/km0m/Manage-song-files.git",
)
sys.stdout.write("Please input your Musicbrainz username: ")
username = user_input()
password = getpass.getpass("Enter your Musicbrainz password: ")

musicbrainzngs.auth(username, password)
musicbrainzngs.set_rate_limit(limit_or_interval=False, new_requests=1)

musicbrainzngs.musicbrainz.VALID_RELEASE_STATUSES = ['official']

musicbrainzngs.get_artist_by_id('Oasis', includes=['recordings', 'releases', 'discids', 'media'])
