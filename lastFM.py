#!/usr/bin/env python
# -*-coding=utf-8 -*-
import urllib
import json
import ConfigParser

config = ConfigParser.RawConfigParser()
config.read('config.ini')

API_KEY = config.get('Last.FM', 'API_KEY')
lovedTracksURL = "https://ws.audioscrobbler.com/2.0/?method=user.getlovedtracks"
topTracksURL = "https://ws.audioscrobbler.com/2.0/?method=user.gettoptracks"
similarTracksURL = "https://ws.audioscrobbler.com/2.0/?method=track.getsimilar"
geoTopTracksURL = "https://ws.audioscrobbler.com/2.0/?method=geo.gettoptracks"

def getLovedTracks(username):
    page = 1
    artists = []
    tracks = []
    nextPage = True
    while nextPage:
        URL = lovedTracksURL + "&user=" + username + "&api_key=" + API_KEY + "&page=" + str(page) + "&format=json"
        try:
            response = urllib.urlopen(URL)
            data = json.loads(response.read())
        except:
            return False

        if 'error' in data:
            print data['message']
            return False
        else:
            for t in data['lovedtracks']['track']:
                artists.append(t['artist']['name'])
                tracks.append(t['name'])
            totalPages = data['lovedtracks']['@attr']['totalPages']
            if int(totalPages) > page:
                page += 1
            else:
                nextPage = False
    return artists, tracks

def getTopTracks(username, period, limit):
    #periods: overall | 7day | 1month | 3month | 6month | 12month
    URL = topTracksURL + "&user=" + username + "&period=" + period + "&limit=" + str(limit) + "&api_key=" + API_KEY + "&format=json"
    artists = []
    tracks = []
    try:
        response = urllib.urlopen(URL)
        data = json.loads(response.read())
    except:
        return False

    if 'error' in data:
        print data['message']
        return False
    else:
        for t in data['toptracks']['track']:
            artists.append(t['artist']['name'])
            tracks.append(t['name'])
    return artists, tracks

def getSimilar(artist, track, limit):
    artists = []
    tracks = []
    URL = similarTracksURL + "&artist=" + artist + "&track=" + track + "&api_key=" + API_KEY + "&limit=" + str(
        limit) + "&autocorrect=1" + "&format=json"
    try:
        response = urllib.urlopen(URL)
        data = json.loads(response.read())
    except:
        return False

    if 'error' in data:
        print data['message']
        return False
    else:
        founded_track = len(data["similartracks"]["track"])
        for i in range(founded_track):
            artists.append(data["similartracks"]["track"][i]["artist"]["name"])
            tracks.append(data["similartracks"]["track"][i]["name"])

    return artists, tracks



def getGeoTopTracks (country, limit):
    artists = []
    tracks = []

    if limit % 50 == 0:
        totalPages = limit / 50
    else:
        totalPages = (limit / 50) + 1

    total = 0
    for page in range(1, totalPages + 1):
        URL = geoTopTracksURL + "&country=" + country + "&api_key=" + API_KEY + "&page=" + str(page) + "&limit=" +  "&format=json"
        try:
            response = urllib.urlopen(URL)
            data = json.loads(response.read())
        except:
            return False

        if 'error' in data:
            print data['message']
            return False
        else:
            for t in data['tracks']['track']:
                artists.append(t['artist']['name'])
                tracks.append(t['name'])
                total = total + 1
                if total == limit:
                    return artists, tracks
