# -*- coding: utf-8 -*-
"""
Created on Fri Nov 20 11:01:19 2020

@author: Razor
"""

import urllib.request

artist = "eminem"
url = 'http://azlyrics.com/'+ artist[0] + "/" + artist + '.html'



with urllib.request.urlopen(url) as response:
    html = response.read()
    for line in html.split(""):
        print(line)



