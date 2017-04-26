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
artistTopTracksURL = "https://ws.audioscrobbler.com/2.0/?method=artist.gettoptracks"
tagTopTracksURL = "https://ws.audioscrobbler.com/2.0/?method=tag.gettoptracks"



def getLovedTracks(username):
    result = []
    page = 1
    nextPage = True
    
    while nextPage:
        URL = lovedTracksURL + "&user=" + username + "&api_key=" + API_KEY + "&page=" + str(page) + "&format=json"
        try:
            response = urllib.urlopen(URL)
            data = json.loads(response.read())
        except:
            return None

        if 'error' in data:
            print data['message']
            return None
        else:
            for t in data['lovedtracks']['track']:
                temp_list = []
                temp_list.append(t['artist']['name'])
                temp_list.append(t['name'])

                result.append(temp_list)

            totalPages = data['lovedtracks']['@attr']['totalPages']
            if int(totalPages) > page:
                page += 1
            else:
                nextPage = False
    return result



def getTopTracks(username, period, limit):
    #periods: overall | 7day | 1month | 3month | 6month | 12month
    URL = topTracksURL + "&user=" + username + "&period=" + period + "&limit=" + str(limit) + "&api_key=" + API_KEY + "&format=json"
    result = []
    try:
        response = urllib.urlopen(URL)
        data = json.loads(response.read())
    except:
        return None

    if 'error' in data:
        print data['message']
        return None
    else:
        for t in data['toptracks']['track']:
            temp_list = []
            temp_list.append(t['artist']['name'])
            temp_list.append(t['name'])

            result.append(temp_list)
    
    return result



def getSimilar(artist, track, limit):
    result = []
    URL = similarTracksURL + "&artist=" + artist + "&track=" + track + "&api_key=" + API_KEY + "&limit=" + str(
        limit) + "&autocorrect=1" + "&format=json"
    
    try:
        response = urllib.urlopen(URL)
        data = json.loads(response.read())
    except:
        return None

    if 'error' in data:
        print data['message']
        return None
    else:
        founded_track = len(data["similartracks"]["track"])
        for i in range(founded_track):
            temp_list = []
            temp_list.append(data["similartracks"]["track"][i]["artist"]["name"])
            temp_list.append(data["similartracks"]["track"][i]["name"])

            result.append(temp_list)

    return result



def getGeoTopTracks (country, limit):
    result = []
    URL = geoTopTracksURL + "&country=" + country + "&api_key=" + API_KEY + "&limit=" + str(limit) +  "&format=json"
    
    try:
        response = urllib.urlopen(URL)
        data = json.loads(response.read())
    except:
        return None

    if 'error' in data:
        print data['message']
        return None
    else:
        for t in data['tracks']['track']:
            temp_list = []
            temp_list.append(t['artist']['name'])
            temp_list.append(t['name'])

            result.append(temp_list)

    return result



def getArtistTopTracks (artist, limit):
    result = []
    URL = artistTopTracksURL + "&artist=" + artist + "&api_key=" + API_KEY + "&limit=" + str(limit) + "&format=json"
        
    try:
        response = urllib.urlopen(URL)
        data = json.loads(response.read())
    except:
        return None

    if 'error' in data:
        print data['message']
        return None
    else:
        for t in data['toptracks']['track']:
            temp_list = []
            temp_list.append(artist)
            temp_list.append(t['name'])

            result.append(temp_list)

    return result



def getTopTracksForTag (tag, limit):
    result = []
    URL = tagTopTracksURL + "&tag=" + tag + "&limit=" + str(limit) +"&api_key=" + API_KEY + "&format=json"
    
    try:
        response = urllib.urlopen(URL)
        data = json.loads(response.read())
    except:
        return None

    if 'error' in data:
        print data['message']
        return None
    else:
        for t in data['tracks']['track']:
            temp_list = []
            temp_list.append(t['artist']['name'])
            temp_list.append(t['name'])

            result.append(temp_list)

    return result
