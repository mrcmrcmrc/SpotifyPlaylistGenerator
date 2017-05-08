#!/usr/bin/env python
# -*-coding=utf-8 -*-
import urllib
import json
import ConfigParser

config = ConfigParser.RawConfigParser()
config.read('config.ini')

API_KEY = config.get('Last.FM', 'API_KEY')
userLovedTracksURL = "https://ws.audioscrobbler.com/2.0/?method=user.getlovedtracks"
userTopTracksURL = "https://ws.audioscrobbler.com/2.0/?method=user.gettoptracks"
userTopAlbumsURL = "https://ws.audioscrobbler.com/2.0/?method=user.gettopalbums"
similarTracksURL = "https://ws.audioscrobbler.com/2.0/?method=track.getsimilar"
geoTopTracksURL = "https://ws.audioscrobbler.com/2.0/?method=geo.gettoptracks"
artistTopTracksURL = "https://ws.audioscrobbler.com/2.0/?method=artist.gettoptracks"
tagTopTracksURL = "https://ws.audioscrobbler.com/2.0/?method=tag.gettoptracks"
topTagsURL = "https://ws.audioscrobbler.com/2.0/?method=tag.gettoptags"
chartTopTracks = "https://ws.audioscrobbler.com/2.0/?method=chart.gettoptracks"
artistTopTagsURL = "https://ws.audioscrobbler.com/2.0/?method=artist.gettoptags"
similarTagsURL = "https://ws.audioscrobbler.com/2.0/?method=tag.getsimilar"
topTagsChartURL = "https://ws.audioscrobbler.com/2.0/?method=chart.gettoptags"
tagTopArtistsURL = "https://ws.audioscrobbler.com/2.0/?method=tag.gettopartists"
trackTopTagsURL = "https://ws.audioscrobbler.com/2.0/?method=track.gettoptags"
albumTopTagsURL = "https://ws.audioscrobbler.com/2.0/?method=album.gettoptags"
similarArtistsURL = "https://ws.audioscrobbler.com/2.0/?method=artist.getSimilar"
tagTopAlbumsURL = "https://ws.audioscrobbler.com/2.0/?method=tag.getTopAlbums"


def getLovedTracks(username):
    result = []
    page = 1
    nextPage = True
    
    while nextPage:
        URL = userLovedTracksURL + "&user=" + username + "&api_key=" + API_KEY + "&page=" + str(page) + "&format=json"
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
    URL = userTopTracksURL + "&user=" + username + "&period=" + period + "&limit=" + str(limit) + "&api_key=" + API_KEY + "&format=json"
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



def getTopAlbums(username, period, limit):
    URL = userTopAlbumsURL + "&user=" + username + "&period=" + period + "&limit=" + str(limit) + "&api_key=" + API_KEY + "&format=json"
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
        for t in data['topalbums']['album']:
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



def getTopTracksByTag (tag, limit):
    result = []
    URL = tagTopTracksURL + "&tag=" + tag + "&limit=" + str(limit) + "&api_key=" + API_KEY + "&format=json"
    
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



def getTopTags ():
    result = []
    URL = topTagsURL + "&api_key=" + API_KEY + "&format=json"

    try:
        response = urllib.urlopen(URL)
        data = json.loads(response.read())
    except:
        return None

    if 'error' in data:
        print data
        return None
    else:
        for t in data['toptags']['tag']:
            result.append(t['name'])

    return result



def getChartTopTracks (limit):
    result = []
    URL = chartTopTracks + "&limit=" + str(limit) + "&api_key=" + API_KEY + "&format=json"
    
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



def getTopTagsForArtist (artist): #artist.getTopTags
    result = []
    URL = artistTopTagsURL + "&artist=" + artist + "&api_key=" + API_KEY + "&format=json" + "&autocorrect=1"

    try:
        response = urllib.urlopen(URL)
        data = json.loads(response.read())
    except:
        return None

    if 'error' in data:
        print data
        return None
    else:
        for t in data['toptags']['tag']:
            temp_list = []
            temp_list.append(t['name'])
            temp_list.append(t['count'])
            
            result.append(temp_list)

    return result



def getSimilarTags (tag):
    result = []
    URL = similarTagsURL + "&tag=" + tag + "&api_key=" + API_KEY + "&format=json"

    try:
        response = urllib.urlopen(URL)
        data = json.loads(response.read())

    except:
        return None

    if 'error' in data:
        print data
        return None
    else:
        pass



def getTopTagsChart ():
    result = []
    URL = topTagsChartURL + "&api_key=" + API_KEY + "&format=json"

    try:
        response = urllib.urlopen(URL)
        data = json.loads(response.read())

    except:
        return None

    if 'error' in data:
        print data
        return None
    else:
        for t in data['tags']['tag']:
            result.append(t['name'])

    return result



def getTagTopArtists (tag, limit): #tag.getTopArtist
    result = []
    URL = tagTopArtistsURL + "&tag=" + tag + "&api_key=" + API_KEY + "&limit=" + str(limit) + "&format=json"

    try:
        response = urllib.urlopen(URL)
        data = json.loads(response.read())

    except:
        return None

    if 'error' in data:
        print data
        return None
    else:
        for artist in data['topartists']['artist']:
            result.append(artist['name'])

    return result



def getTopTagsForTrack (artist, track): #track.getTopTags
    result = []
    URL = trackTopTagsURL + "&artist=" + artist  + "&track=" + track + "&api_key=" + API_KEY  + "&format=json" + "&autocorrect=1"

    try:
        response = urllib.urlopen(URL)
        data = json.loads(response.read())

    except:
        return None

    if 'error' in data:
        print data
        return None
    else:
        for tag in data['toptags']['tag']:
            temp_list = []
            temp_list.append(tag['name'])
            temp_list.append(tag['count'])
            
            result.append(temp_list)

    return result



def getTopTagsForAlbum (artist, album): #album.getTopTags
    result = []
    URL = albumTopTagsURL + "&artist=" + artist  + "&album=" + album + "&api_key=" + API_KEY  + "&format=json" + "&autocorrect=1"

    try:
        response = urllib.urlopen(URL)
        data = json.loads(response.read())

    except:
        return None

    if 'error' in data:
        print data
        return None
    else:
        for tag in data['toptags']['tag']:
            temp_list = []
            temp_list.append(tag['name'])
            temp_list.append(tag['count'])
            
            result.append(temp_list)

    return result



def getSimilarArtists (artist, limit): #artist.getSimilar
    result = []
    URL = similarArtistsURL + "&artist=" + artist + "&limit=" + str(limit) + "&api_key=" + API_KEY  + "&format=json" + "&autocorrect=1"

    try:
        response = urllib.urlopen(URL)
        data = json.loads(response.read())

    except:
        return None

    if 'error' in data:
        print data
        return None
    else:
        for a in data['similarartists']['artist']:
            temp_list = []
            temp_list.append(a['name'])
            temp_list.append(a['match'])
            
            result.append(temp_list)

    return result



def getTopAlbumsByTag (tag, limit):
    result = []
    URL = tagTopAlbumsURL + "&tag=" + tag + "&api_key=" + API_KEY + "&limit=" + str(limit) + "&format=json"

    try:
        response = urllib.urlopen(URL)
        data = json.loads(response.read())

    except:
        return None

    if 'error' in data:
        print data
        return None
    else:
        for album in data['albums']['album']:
            temp_list = [] 
            temp_list.append(album['artist']['name'])
            temp_list.append(album['name'])
            
            result.append(temp_list)

    return result


#TODO: tag.getTopTracks
