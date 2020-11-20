# -*- coding: utf-8 -*-
"""
Created on Fri Nov 20 11:01:19 2020

@author: Razor
"""

import urllib.request

artist = "eminem"
url = 'http://azlyrics.com/'+ artist[0] + "/" + artist + '.html'



with urllib.request.urlopen(url) as response:
    html = str(response.read())
    parts = html.split("<!-- start of song list -->")

    lines = parts[1].split("<div id=")


    albums = lines[2:23]
    names = {}
    #print(albums)
    for album in albums[:-1]:
        songs = album.split("div class")
        if len(songs) > 1:
            print("\n\n++++++++++++++++++++")
            album_name = songs[0].split("<b>")[1].split("</b>")[0]
            print(album_name)
            for song in songs[1:]:
                song_name = song.split("href=")
                if song_name[0] == "=\"listalbum-item\"><a ":
                    song_name = song_name[1].split(" ")[0]
                    print(song_name)





    final = albums[-1]
    final = final.split("other songs:")[0]
    songs = final.split("div class")
    if len(songs) > 1:
            print("\n\n++++++++++++++++++++")
            album_name = songs[0].split("<b>")[1].split("</b>")[0]
            print(album_name)
            for song in songs[1:]:
                song_name = song.split("href=")
                song_name = song.split("href=")
                if song_name[0] == "=\"listalbum-item\"><a ":
                    song_name = song_name[1].split(" ")[0]
                    print(song_name)




