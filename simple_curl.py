# -*- coding: utf-8 -*-
"""
Created on Fri Nov 20 11:01:19 2020

@author: Razor
"""

import urllib.request
import pandas as pd

artist = "eminem"
url = 'http://azlyrics.com/'+ artist[0] + "/" + artist + '.html'

# artist: eminem
    # album: a
        # songs: 1,2,3


def curl_song(url):
    lines = []
    url = url.replace("..", "https://www.azlyrics.com")
    ##print(url)
    url = url[1:-1]
    try:
        with urllib.request.urlopen(url) as response:
            html = str(response.read())
            #print(html)
            html = html.split("<!-- Usage of azlyrics.com content by any third-party lyrics provider is prohibited by our licensing agreement. Sorry about that. -->")[1].split("<br><br>")[0].split("\\n")
            for line in html:
                line = line.replace("<br>", "").replace("\\'", "").replace("<i>", "").replace("</i>", "").replace("</div>\\r", "").replace("\\r", "").replace("&quot;", "")
                if line:
                    #print(line)
                    lines.append(line)
        return lines

    except:
        pass




with urllib.request.urlopen(url) as response:
    html = str(response.read())
    try:
        parts = html.split("<!-- start of song list -->")

        print(len(parts))

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
                        ##print(song_name)
                        ###curl_song(song_name)
                        ###d = {'album': album_name, "song_name": song_name, "lyrics": lines}
                        ###df = pd.DataFrame(data=d)


        print("_____________________")
        album_name = "other_songs"
        print(album_name)
        final = albums[-1]
        final = final.split("other songs:")

        songs = final[-1].split("div class")

        for s in songs[:-1]:
            if "listalbum" in s:
                song_name = s.split("href=")[1].split()[0]
                ###curl_song(song_name)
                ###d = {'album': album_name, "song_name": song_name, "lyrics": lines}
                ###df = pd.DataFrame(data=d)

        song_name = songs[-1].split("script type")[0].split("href=")[1].split()[0]
        lines = curl_song(song_name)
        print(song_name)
        print(lines)
        print("+-+-+-+")

        d = {'album': album_name, "song_name": song_name, "lyrics": lines}
        df = pd.DataFrame(data=d, index=song_name)

        print(df)
        df.to_json('eminem.json')
    except:
        pass



























