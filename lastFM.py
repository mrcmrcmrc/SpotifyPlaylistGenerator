#!/usr/bin/env python
# -*-coding=utf-8 -*-
import requests
import json
import ConfigParser

config = ConfigParser.RawConfigParser()
config.read('config.ini')

API_KEY = config.get('Last.FM', 'API_KEY')
URL = "https://ws.audioscrobbler.com/2.0/"


def getLovedTracks(username):
    result = []
    page = 1
    nextPage = True
    
    while nextPage:
        params = {'method' : 'user.getlovedtracks', 'user' : username, 'page' : page, 'api_key': API_KEY, 'format' : 'json'}
        
        try:
            response = requests.post(URL, data=params, timeout=5).json()
        except requests.exceptions.RequestException as e:
            print e
            return None

        if 'error' in response:
            print response['message']
            return None
        else:
            for track in response['lovedtracks']['track']:
                temp_list = []
                temp_list.append(track['artist']['name'])
                temp_list.append(track['name'])

                result.append(temp_list)

            totalPages = response['lovedtracks']['@attr']['totalPages']
            if int(totalPages) > page:
                page += 1
            else:
                nextPage = False
    return result



def getTopTracks(username, period, limit, includePC = False):
    #periods: overall | 7day | 1month | 3month | 6month | 12month
    params = {'method' : 'user.gettoptracks', 'user' : username, 'period' : period, 'limit' : limit, 'api_key': API_KEY, 'format' : 'json'}    
    result = []
    try:
        response = requests.post(URL, data=params, timeout=5).json()
    except requests.exceptions.RequestException as e:
        print e
        return None

    if 'error' in response:
        print response['message']
        return None
    else:
        for track in response['toptracks']['track']:
            temp_list = []
            temp_list.append(track['artist']['name'])
            temp_list.append(track['name'])
            
            if includePC is True:
                temp_list.append(track['playcount'])
            
            result.append(temp_list)
    return result



def getTopAlbums(username, period, limit, includePC = False):
    params = {'method' : 'user.gettopalbums', 'user' : username, 'period' : period, 'limit' : limit, 'api_key': API_KEY, 'format' : 'json'} 
    result = []
    try:
        response = requests.post(URL, data=params, timeout=5).json()
    except requests.exceptions.RequestException as e:
        print e
        return None

    if 'error' in response:
        print response['message']
        return None
    else:
        for album in response['topalbums']['album']:
            temp_list = []
            temp_list.append(album['artist']['name'])
            temp_list.append(album['name'])

            if includePC is True:
                temp_list.append(album['playcount'])
            
            result.append(temp_list)
    
    return result    



def getTopArtists(username, period, limit, includePC = False):
    params = {'method' : 'user.gettopartists', 'user' : username, 'period' : period, 'limit' : limit, 'api_key': API_KEY, 'format' : 'json'} 
    result = []
    
    try:
        response = requests.post(URL, data=params, timeout=5).json()
    except requests.exceptions.RequestException as e:
        print e
        return None

    if 'error' in response:
        print response['message']
        return None
    else:
        for artist in response['topartists']['artist']:
            temp_list = []
            temp_list.append(artist['name'])

            if includePC is True:
                temp_list.append(artist['playcount'])
            
            result.append(temp_list)
    
    return result   



def getSimilar(artist, track, limit):
    params = {'method' : 'track.getsimilar', 'artist' : artist, 'track' : track, 'limit' : limit, 'api_key': API_KEY, 'format' : 'json', 'autocorrect' : '1'} 
    result = []
    
    try:
        response = requests.post(URL, data=params, timeout=5).json()
    except requests.exceptions.RequestException as e:
        print e
        return None

    if 'error' in response:
        print response['message']
        return None
    else:
        for t in response['similartracks']['track']:
            temp_list = []
            temp_list.append(t["artist"]["name"])
            temp_list.append(t["name"])

            result.append(temp_list)

    return result



def getGeoTopTracks (country, limit):    
    params = {'method' : 'geo.gettoptracks', 'country' : country, 'limit' : limit, 'api_key': API_KEY, 'format' : 'json'} 
    result = []
    
    try:
        response = requests.post(URL, data=params, timeout=5).json()
    except requests.exceptions.RequestException as e:
        print e
        return None

    if 'error' in response:
        print response['message']
        return None
    else:
        for track in response['tracks']['track']:
            temp_list = []
            temp_list.append(track['artist']['name'])
            temp_list.append(track['name'])

            result.append(temp_list)

    return result



def getGeoTopArtists (country, limit):    
    params = {'method' : 'geo.gettopartists', 'country' : country, 'limit' : limit, 'api_key': API_KEY, 'format' : 'json'} 
    result = []
    
    try:
        response = requests.post(URL, data=params, timeout=5).json()
    except requests.exceptions.RequestException as e:
        print e
        return None

    if 'error' in response:
        print response['message']
        return None
    else:
        for artist in response['topartists']['artist']:
            result.append(artist['name'])

    return result   



def getArtistTopTracks (artist, limit):
    params = {'method' : 'artist.gettoptracks', 'artist' : artist, 'limit' : limit, 'api_key': API_KEY, 'format' : 'json'} 
    result = []
    
    try:
        response = requests.post(URL, data=params, timeout=5).json()
    except requests.exceptions.RequestException as e:
        print e
        return None

    if 'error' in response:
        print response['message']
        return None
    else:
        for track in response['toptracks']['track']:
            temp_list = []
            temp_list.append(artist)
            temp_list.append(track['name'])

            result.append(temp_list)

    return result



def getTopTracksByTag (tag, limit):
    params = {'method' : 'tag.gettoptracks', 'tag' : tag, 'limit' : limit, 'api_key': API_KEY, 'format' : 'json'} 
    result = []
    
    try:
        response = requests.post(URL, data=params, timeout=5).json()
    except requests.exceptions.RequestException as e:
        print e
        return None

    if 'error' in response:
        print response['message']
        return None
    else:
        for track in response['tracks']['track']:
            temp_list = []
            temp_list.append(track['artist']['name'])
            temp_list.append(track['name'])

            result.append(temp_list)

    return result



def getTopTags ():
    params = {'method' : 'tag.gettoptags', 'api_key': API_KEY, 'format' : 'json'} 
    result = []
    
    try:
        response = requests.post(URL, data=params, timeout=5).json()
    except requests.exceptions.RequestException as e:
        print e
        return None

    if 'error' in response:
        print response['message']
        return None
    else:
        for tag in response['toptags']['tag']:
            result.append(tag['name'])

    return result



def getChartTopTracks (limit):
    params = {'method' : 'chart.gettoptracks', 'limit' : limit, 'api_key': API_KEY, 'format' : 'json'} 
    result = []
    
    try:
        response = requests.post(URL, data=params, timeout=5).json()
    except requests.exceptions.RequestException as e:
        print e
        return None

    if 'error' in response:
        print response['message']
        return None
    else:
        for track in response['tracks']['track']:
            temp_list = []
            temp_list.append(track['artist']['name'])
            temp_list.append(track['name'])

            result.append(temp_list)

    return result



def getTopTagsForArtist (artist): #artist.getTopTags
    params = {'method' : 'artist.gettoptags', 'artist' : artist, 'api_key': API_KEY, 'format' : 'json'} 
    result = []
    
    try:
        response = requests.post(URL, data=params, timeout=5).json()
    except requests.exceptions.RequestException as e:
        print e
        return None

    if 'error' in response:
        print response['message']
        return None
    else:
        for tag in response['toptags']['tag']:
            temp_list = []
            temp_list.append(tag['name'])
            temp_list.append(ag['count'])
            
            result.append(temp_list)

    return result



def getSimilarTags (tag): #tag.getSimilar
    pass



def getTopTagsChart ():
    params = {'method' : 'chart.gettoptags', 'api_key': API_KEY, 'format' : 'json'} 
    result = []
    
    try:
        response = requests.post(URL, data=params, timeout=5).json()
    except requests.exceptions.RequestException as e:
        print e
        return None

    if 'error' in response:
        print response['message']
        return None
    else:
        for tag in response['tags']['tag']:
            result.append(tag['name'])

    return result



def getTopArtistsChart ():
    params = {'method' : 'chart.gettopartists', 'api_key': API_KEY, 'format' : 'json'} 
    result = []
    
    try:
        response = requests.post(URL, data=params, timeout=5).json()
    except requests.exceptions.RequestException as e:
        print e
        return None

    if 'error' in response:
        print response['message']
        return None
    else:
        for artist in response['artists']['artist']:
            result.append(artist['name'])

    return result 



def getTagTopArtists (tag, limit): #tag.getTopArtist
    params = {'method' : 'tag.gettopartists', 'tag' : tag, 'limit' : limit, 'api_key': API_KEY, 'format' : 'json'} 
    result = []
    
    try:
        response = requests.post(URL, data=params, timeout=5).json()
    except requests.exceptions.RequestException as e:
        print e
        return None

    if 'error' in response:
        print response['message']
        return None
    else:
        for artist in response['topartists']['artist']:
            result.append(artist['name'])

    return result



def getTopTagsForTrack (artist, track, limit = 100): #track.getTopTags
    params = {'method' : 'track.gettoptags', 'artist' : artist, 'track' : track, 'limit' : limit, 'api_key': API_KEY, 'format' : 'json'} 
    result = []
    
    try:
        response = requests.post(URL, data=params, timeout=5).json()
    except requests.exceptions.RequestException as e:
        print e
        return None

    if 'error' in response:
        print response['message']
        return None
    else:
        for tag in response['toptags']['tag']:
            temp_list = []
            temp_list.append(tag['name'])
            temp_list.append(tag['count'])
            
            result.append(temp_list)
            if len(result) == limit:
                return result
    return result



def getTopTagsForAlbum (artist, album): #album.getTopTags
    params = {'method' : 'album.gettoptags', 'artist' : artist, 'album' : album, 'api_key': API_KEY, 'format' : 'json'} 
    result = []
    
    try:
        response = requests.post(URL, data=params, timeout=5).json()
    except requests.exceptions.RequestException as e:
        print e
        return None

    if 'error' in response:
        print response['message']
        return None
    else:
        for tag in response['toptags']['tag']:
            temp_list = []
            temp_list.append(tag['name'])
            temp_list.append(tag['count'])
            
            result.append(temp_list)

    return result



def getSimilarArtists (artist, limit): #artist.getSimilar
    params = {'method' : 'artist.getsimilar', 'artist' : artist, 'limit' : limit, 'api_key': API_KEY, 'format' : 'json'} 
    result = []
    
    try:
        response = requests.post(URL, data=params, timeout=5).json()
    except requests.exceptions.RequestException as e:
        print e
        return None

    if 'error' in response:
        print response['message']
        return None
    else:
        for a in response['similarartists']['artist']:
            temp_list = []
            temp_list.append(a['name'])
            temp_list.append(a['match'])
            
            result.append(temp_list)

    return result



def getTopAlbumsByTag (tag, limit):
    params = {'method' : 'tag.gettopalbums', 'tag' : tag, 'limit' : limit, 'api_key': API_KEY, 'format' : 'json'} 
    result = []
    
    try:
        response = requests.post(URL, data=params, timeout=5).json()
    except requests.exceptions.RequestException as e:
        print e
        return None

    if 'error' in response:
        print response['message']
        return None
    else:
        for album in response['albums']['album']:
            temp_list = [] 
            temp_list.append(album['artist']['name'])
            temp_list.append(album['name'])
            
            result.append(temp_list)

    return result



def getTagInfo (tag):
    params = {'method' : 'tag.getinfo', 'tag' : tag, 'api_key': API_KEY, 'format' : 'json'} 
    result = []
    
    try:
        response = requests.post(URL, data=params, timeout=5).json()
    except requests.exceptions.RequestException as e:
        print e
        return None

    if 'error' in response:
        print response['message']
        return None
    else:
        if response['tag']['wiki']['content'] == "":
            return None
        else: 
            return response['tag']['wiki']['content']
