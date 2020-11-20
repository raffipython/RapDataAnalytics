# -*- coding: utf-8 -*-
"""
Created on Fri Nov 20 10:27:29 2020

@author: Razor
"""

# modified version of
# https://github.com/FrancescoGuarneri/AzLyricsAPI/blob/master/api/azapi.py
# https://www.azlyrics.com/e/eminem.html

from bs4 import BeautifulSoup
import urllib.request
import urllib.error
import urllib.parse

def process_album(album):
    pass


def response(url):
    response = urllib.request.urlopen(url)
    read_lyrics = response.read()
    soup = BeautifulSoup(read_lyrics)
    albums = soup.find_all("div", attrs={"class": "album"})

    albums = soup.find_all("div", attrs={"class": "listalbum-item"})
    #<!-- start of song list -->
    #<script type="text/javascript">
    albums = soup.find_all())

    for album in albums:
        print(album)


def curl(artist):
    artist = artist.lower().replace(" ", "%20")
    generate_url = 'http://azlyrics.com/'+ artist[0] + "/" + artist + '.html'
    print(generate_url)
    response(generate_url)



"""
def processing(generate_url, artist, title, save):
    response = urllib.request.urlopen(generate_url)
    read_lyrics = response.read()
    soup = BeautifulSoup(read_lyrics)

    lines = soup.find_all("div", attrs={"class": None, "id": None})
    print(lines)


    #lyrics = soup.find_all("div", attrs={"class": None, "id": None})




    #lyrics = [x.getText() for x in lyrics]


    #printing(artist, title, save, lyrics)

def printing(artist, title, save, lyrics):
    for x in lyrics:
        print(x, end="\n\n")
    #if save == True:
    #    saving(artist, title, lyrics)
    #elif save == False:
    #    pass

def saving(artist, title, lyrics):
        f = open(artist + '_' + title + '.txt', 'w')
        f.write("\n".join(lyrics).strip())
        f.close()


#generating(artist, title, save)
"""

curl("eminem")
