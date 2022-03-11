# -*- coding: utf-8 -*-
"""
Created on Fri Mar 11 19:00:54 2022

@author: Koala
"""

#!/usr/bin/python3
from __future__ import print_function
from __future__ import unicode_literals
import musicbrainzngs
import sys

musicbrainzngs.set_useragent(
    "python-musicbrainzngs-example",
    "0.1",
    "https://github.com/alastair/python-musicbrainzngs/",
)

def get_tracklist(artist):
    result = musicbrainzngs.search_releases(artist=artist, limit=1)       
    # id = result["release-list"][0]["id"]
    for i in range(len(result["release-list"])):
        #### get tracklist
        new_result = musicbrainzngs.get_release_by_id(id, includes=["recordings"])
        t = (new_result["release"]["medium-list"][i]["track-list"])
        for x in range(len(t)):
            line = (t[x])
            print(f'{line["number"]}. {line["recording"]["title"]}')

if __name__ == '__main__':
    ### get first release
    if len(sys.argv) > 1:
        artist, album = [sys.argv[1], sys.argv[2]]
        get_tracklist(artist, album)
    else:
        artist = input("Artist: ")
        # album = input("Album: ")
        if not artist == "":
            get_tracklist(artist)
        else:
            print("Artist or Album missing")
