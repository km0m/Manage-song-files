# -*- coding: utf-8 -*-
"""
Created on Sun Mar  6 18:42:34 2022

@author: Koala
"""

import musicbrainzngs
import getpass
import sys
from urllib.request import Request, urlopen

artist_name = input("Enter artist name: ")

agent_name = "search-artist.py"
agent_version = "0.1"
# this script doesn't submit anything (empty dict)
# so testing this on live server (with live passwords) is okay.
musicbrainz_server = "musicbrainz.org"

musicbrainzngs.set_hostname(musicbrainz_server)
musicbrainzngs.set_useragent(
    agent_name,
    agent_version,
    "https://github.com/km0m/Manage-song-files.git",
)

musicbrainzngs.set_rate_limit(limit_or_interval=False, new_requests=1)

result = musicbrainzngs.search_artists(query=artist_name, limit=None, offset=None, strict=True)
artist_id = result['artist-list'][0]['id']

artist = musicbrainzngs.get_artist_by_id(artist_id, includes=['releases'])

for release in artist['artist']['release-list']:
  release_id = release['id']
  media = musicbrainzngs.get_release_by_id(release_id, includes=['media'])
  print(media['release']['title'])
#for artist in result['artist-list']:
#    print("{name}: {id}".format(name=artist["name"], id=artist['id']))['id']
