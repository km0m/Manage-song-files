# -*- coding: utf-8 -*-
"""
Created on Sun Mar  6 18:42:34 2022

@author: Koala
"""

import musicbrainzngs
import sys
import urllib3

musicbrainzngs.set_useragent(
    "python-search-artist_example",
    "0.1",
    "https://github.com/km0m/Manage-song-files.git",
)

musicbrainzngs.get_artist_by_id('Oasis', includes=['recordings', 'releases', 'discids', 'media'])
