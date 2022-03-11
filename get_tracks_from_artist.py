# -*- coding: utf-8 -*-
"""
Created on Fri Mar 11 19:00:54 2022

@author: Koala
"""

#!/usr/bin/python3
from __future__ import print_function
from __future__ import unicode_literals
import musicbrainzngs
# import sys

musicbrainzngs.set_useragent(
    "python-musicbrainzngs-example",
    "0.1",
    "https://github.com/alastair/python-musicbrainzngs/",
)

def get_tracklist(artist):
    artist_id = musicbrainzngs.search_artists(artist=artist, strict=True)['artist-list'][0]['id']
    result = musicbrainzngs.browse_releases(artist=artist_id, release_status=['official'], release_type=['album'], includes=['recordings'], limit=10, offset=0)
    for i in range(len(result["release-list"])):
        #### get tracklist
        id = result["release-list"][i]["id"]
        new_result = musicbrainzngs.get_release_by_id(id, includes=["recordings"])
        t = (new_result["release"]["medium-list"][0]["track-list"])
        for x in range(len(t)):
            line = (t[x])
            print(f'{line["number"]}. {line["recording"]["title"]}')

if __name__ == '__main__':
    ### get first release
    artist = input("Artist: ")
    # album = input("Album: ")
    if not artist == "":
        get_tracklist(artist)
    else:
        print("Artist or Album missing")
