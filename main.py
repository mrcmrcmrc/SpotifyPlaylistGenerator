#!/usr/bin/python
# -*- coding: utf-8 -*-
import spotipy
import spotipy.util as util
import lastFM
import fire
import ConfigParser
import sys

reload(sys)    # to re-enable sys.setdefaultencoding()
sys.setdefaultencoding('utf-8')

config = ConfigParser.RawConfigParser()
config.read('config.ini')
    
username = config.get('Spotify', 'UserName')
client_id = config.get('Spotify', 'client_id')
client_secret = config.get('Spotify', 'client_secret')
lastFMUserName = config.get('Last.FM', 'UserName')



def getSimilar(artist, track, count = 20, playlistName = None):
    
    print "%s similar tracks to %s" % (count, track)
    result = lastFM.getSimilar(artist = artist, track = track, limit = count)

    if result is not None:
        if playlistName is None:
            playlistName = "Similar Songs to %s" % track.capitalize()

        generatePlaylist(result, playlistName)
        



def getTop(lastFMUserName = lastFMUserName, period = "1month", count = 20, playlistName = None):
    
    print "%s\'s top %s tracks (%s)" % (lastFMUserName, count, period)
    result = lastFM.getTopTracks(lastFMUserName, period = period, limit = count) #period="overall"
    
    if result is not None:
        if playlistName is None:
            playlistName = "%s\'s Top Songs" % lastFMUserName

        generatePlaylist (result, playlistName)



def getLoved(lastFMUserName = lastFMUserName, playlistName = None):
    
    print "loved tracks by %s" % lastFMUserName
    result = lastFM.getLovedTracks(lastFMUserName)

    if result is not None:
        if playlistName is None:
            playlistName = "Loved Songs by %s" % lastFMUserName

        generatePlaylist (result, playlistName)


def getTopByCountry(country, count = 50, playlistName = None):
   
    print "%s Top %s" % (country, count)
    result = lastFM.getGeoTopTracks(country = country, limit = count)

    if result is not None:
        if playlistName is None:
            playlistName = "%s Top %s" % (country.capitalize(), count)
     
        generatePlaylist (result, playlistName)



def getTopByArtist(artist, count = 20, playlistName = None):
    
    print "The best %s songs" % artist.capitalize()
    result = lastFM.getArtistTopTracks(artist = artist, limit = count)

    if result is not None:
        if playlistName is None:
            playlistName = "The best %s songs" % artist.capitalize()

        generatePlaylist (result, playlistName)



def getTopByTag (tag, count = 25, playlistName = None):

    print "Top %s Songs" % (tag)
    result = lastFM.getTopTracksByTag(tag = tag, limit = count)

    if result is not None:
        if playlistName is None:
            playlistName = "Top %s Songs" % tag.capitalize()
     
        generatePlaylist (result, playlistName)



def showTopTags ():
    """top tags from last.fm"""
    result = lastFM.getTopTags()
    if result is not None:
        index = 0
        for i in range(len(result)/5):
            print "%-20s\t %-20s\t %-20s\t %-20s\t %-20s" % (result[index], result[index+1], result[index+2], result[index+3], result[index+4])
            index = index + 5



def getChartTopTracks (count = 25, playlistName = None):
    
    print "Top Songs by Last.FM"
    result = lastFM.getChartTopTracks(limit = count)

    if result is not None:
        if playlistName is None:
            playlistName = "Top Songs by Last.FM"
     
        generatePlaylist (result, playlistName)



def generatePlaylist(result, playlistName):
    scope = "playlist-modify-public"
    token = util.prompt_for_user_token(username=username, client_id=client_id, client_secret=client_secret, redirect_uri="http://localhost:80", scope=scope)
    
    track_IDs = []
    filters=['/', '.', 'ft', 'feat', '-', '[', '(', '~']

    count = len(result)
    found = 0
    sp = spotipy.Spotify()
    for r in result:
        try:
            search_res = sp.search(q='artist:{0} track:{1}'.format(r[0], r[1]), type='track', limit=1, market='TR')
        except:
            
             "err"
        if len(search_res['tracks']['items']) == 0:
            for letter in r[1]:
                if letter in filters:
                    search_res = sp.search(q='artist:{0} track:{1}'.format(r[0], r[1]), type='track', limit=1, market='TR')
                    break
            if len(search_res['tracks']['items']) > 0:
                if search_res['tracks']['items'][0]['id'] not in track_IDs:
                    track_IDs.append(search_res['tracks']['items'][0]['id'])
                    found = found + 1
                    print '\r{0} - {1} [{2} of {3}]{4}\r'.format(r[0], r[1], found, count, ' '*50),
             

            else:
                found = found + 1
                print '\r{0} - {1} NOT FOUND [{2} of {3}]{4}\r'.format(r[0], r[1], found, count, ' '*50),

            continue
        if search_res['tracks']['items'][0]['id'] not in track_IDs:
            track_IDs.append(search_res['tracks']['items'][0]['id'])
            found = found + 1
            #sys.stdout.write('\r%s - %s\t[%d of %d]\033[K\n' % (r[0], r[1], found, count))
            print '{0} - {1} [{2} of {3}]{4}\r'.format(r[0], r[1], found, count, ' '*50),
    

    if len(track_IDs) is not 0:
        if token:
            sp = spotipy.Spotify(auth=token)
            sp.trace = False
            playlist = sp.user_playlist_create(username, playlistName)

            if playlist and playlist.get('id'):
                i = 0
                while (len(track_IDs) / 100) >= i:
                    if len(track_IDs) == i:
                        sp.user_playlist_add_tracks(username, playlist.get('id'), track_IDs[i * 100:])
                    else:
                        sp.user_playlist_add_tracks(username, playlist.get('id'), track_IDs[i*100:(i+1)*100])
                        i += 1
                print "\n" + playlistName + " has been created successfully"

        else:
            print("Can't get token for ", username)



def main():
    fire.Fire()



if __name__ == '__main__':

    fire.Fire({
      'getsimilar': getSimilar,
      'gettop': getTop,
      'getloved' : getLoved,
      'gettopbycounty' : getTopByCountry,
      'gettopbyartist' : getTopByArtist,
      'gettopbytag' : getTopByTag,
      'showtoptags' : showTopTags,
      'getcharttoptracks' : getChartTopTracks
  })

