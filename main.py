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
        


def getUserTopTracks(lastFMUserName = lastFMUserName, period = "1month", count = 20, playlistName = None):
    
    print "%s\'s top %s tracks (%s)" % (lastFMUserName, count, period)
    result = lastFM.getTopTracks(lastFMUserName, period = period, limit = count) #period="overall"
    
    if result is not None:
        if playlistName is None:
            playlistName = "%s\'s Top Songs" % lastFMUserName

        generatePlaylist (result, playlistName)



def getUserLovedTracks(lastFMUserName = lastFMUserName, playlistName = None):
    
    print "loved tracks by %s" % lastFMUserName
    result = lastFM.getLovedTracks(lastFMUserName)

    if result is not None:
        if playlistName is None:
            playlistName = "Loved Songs by %s" % lastFMUserName

        generatePlaylist (result, playlistName)


def getTopTracksByCountry(country, count = 50, playlistName = None):
   
    print "%s Top %s" % (country, count)
    result = lastFM.getGeoTopTracks(country = country, limit = count)

    if result is not None:
        if playlistName is None:
            playlistName = "%s Top %s" % (country.capitalize(), count)
     
        generatePlaylist (result, playlistName)



def getTopTracksByArtist(artist, count = 20, playlistName = None):
    
    print "The best %s songs" % artist.capitalize()
    result = lastFM.getArtistTopTracks(artist = artist, limit = count)

    if result is not None:
        if playlistName is None:
            playlistName = "The best %s songs" % artist.capitalize()

        generatePlaylist (result, playlistName)



def getTopTracksByTag (tag, count = 25, playlistName = None):

    print "Top %s Songs" % (tag)
    result = lastFM.getTopTracksByTag(tag = tag, limit = count)

    if result is not None:
        if playlistName is None:
            playlistName = "Top %s Songs" % tag.capitalize()
     
        generatePlaylist (result, playlistName)



def getUserTopAlbums(lastFMUserName = lastFMUserName, count = 10, period = '3month', playlistName = None):
    
    print "%s\'s top %s albums (%s)" % (lastFMUserName, count, period)
    result = lastFM.getTopAlbums(username = lastFMUserName, limit = count, period = period)

    if result is not None:
        if playlistName is None:
            playlistName = "%s\'s top albums" % lastFMUserName

        generatePlaylist(result, playlistName, t = 'album')



def getTopTracksChart (count = 25, playlistName = None):
    
    print "Top Songs by Last.FM"
    result = lastFM.getChartTopTracks(limit = count)

    if result is not None:
        if playlistName is None:
            playlistName = "Top Songs by Last.FM"
     
        generatePlaylist (result, playlistName)



def getTopAlbumsByTag (tag, count, playlistName = None):
    print "Top {0} albums".format(tag)
    result = lastFM.getTopAlbumsByTag(tag = tag, limit = count)

    if result is not None:
        if playlistName is None:
            playlistName = "Top {0} albums".format(tag)
        generatePlaylist(result, playlistName, t = 'album')



def showTopTagsForArtist (artist):
    """top tags for an artist"""
    print "Top tags for %s:" % artist
    result = lastFM.getTopTagsForArtist(artist = artist)

    if result is not None:
        index = 0
        for i in range(len(result)/4):
            print "%-20s --> [%s]\t %-20s --> [%s]\t %-20s --> [%s]\t %-20s --> [%s]" % (result[index][0], result[index][1], result[index+1][0], result[index+1][1], result[index+2][0], result[index+2][1], result[index+3][0], result[index+3][1])
            index = index + 4    



def showTopTags ():
    """top tags from last.fm"""
    result = lastFM.getTopTags()
    if result is not None:
        index = 0
        print "\n"
        for i in range(len(result)/5):
            print "%-20s\t %-20s\t %-20s\t %-20s\t %-20s" % (result[index], result[index+1], result[index+2], result[index+3], result[index+4])
            index = index + 5



def showSimilarTags (tag):
    """similar tags to given tag"""



def showTopTagsChart ():
    result = lastFM.getTopTagsChart()
    
    if result is not None:
        index = 0
        for i in range(len(result)/5):
            print "%-20s\t %-20s\t %-20s\t %-20s\t %-20s" % (result[index], result[index+1], result[index+2], result[index+3], result[index+4])
            index = index + 5   



def showTopArtistsByTag (tag, count = 25):
    print "Top %s artists:" % tag
    result = lastFM.getTagTopArtists(tag = tag, limit = count)

    if result is not None:
        index = 0
        for i in range(len(result)/5):
            print "%-20s\t %-20s\t %-20s\t %-20s\t %-20s" % (result[index], result[index+1], result[index+2], result[index+3], result[index+4])
            index = index + 5 



def showSimilarArtists (artist, count = 15):
    print "Similar artists to %s:" % artist
    result = lastFM.getSimilarArtists(artist = artist, limit = count)

    if result is not None:
        for r in result:
            print "\U1f34e%-25s  [ %s ]" % (r[0], r[1])
        


def showTopTagsForTrack (artist, track):
    print "top tags for %s [ %s ]" % (track, artist)
    result = lastFM.getTopTagsForTrack(artist = artist, track = track)

    if result is not None:
        index = 0
        for i in range(len(result)/4):
            print "%-20s --> [%s]\t %-20s --> [%s]\t %-20s --> [%s]\t %-20s --> [%s]" % (result[index][0], result[index][1], result[index+1][0], result[index+1][1], result[index+2][0], result[index+2][1], result[index+3][0], result[index+3][1])
            index = index + 4



def showTopTagsForAlbum (artist, album):
    print "top tags for %s [ %s ]" % (album, artist)
    result = lastFM.getTopTagsForAlbum(artist = artist, album = album)

    if result is not None:
        index = 0
        for i in range(len(result)/4):
            print "%-20s --> [%s]\t %-20s --> [%s]\t %-20s --> [%s]\t %-20s --> [%s]" % (result[index][0], result[index][1], result[index+1][0], result[index+1][1], result[index+2][0], result[index+2][1], result[index+3][0], result[index+3][1])
            index = index + 4



def showTopAlbumsByTag (tag, count = 20):
    print "Top %s albums" % tag
    result = lastFM.getTopAlbumsByTag(tag = tag, limit = count)

    if result is not None:
        index = 0
        for r in result:
            print("{0} - {1}".format(r[0], r[1]))



def generatePlaylist(result, playlistName, t = 'track'):
    """."""
    if t is 'track':
        track_IDs = getTrackIDs(result)
    
    elif t is 'album':
        track_IDs = getTrackdIDsFromAlbum(getAlbumIDs(result))

    if len(track_IDs) is not 0:
        scope = "playlist-modify-public"
        token = util.prompt_for_user_token(username=username, client_id=client_id, client_secret=client_secret, redirect_uri="http://localhost:80", scope=scope)
        
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
                print "\n" + playlistName + " has been created successfully..."

        else:
            print("Can't get token for ", username)


def getTrackIDs(result):
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

    return track_IDs



def getAlbumIDs(result):
    album_IDs = []  
    sp = spotipy.Spotify()

    for r in result:
        try:
            search_res = sp.search(q='artist:{0} album:{1}'.format(r[0], r[1]), type='album', limit=1, market='TR')
        except:
            "err"

        if search_res['albums']['total'] != 0:
            album_IDs.append(search_res['albums']['items'][0]['id'])
            print "{0} - {1}".format(r[0], r[1])
        else:
            print "{0} - {1} ******* not found....".format(r[0], r[1])

    return album_IDs 



def getTrackdIDsFromAlbum(album_IDs):
    track_IDs = [] 
    sp = spotipy.Spotify()

    for album_ID in album_IDs:
        i = 0
        next_ = ""
        while next_ is not None:
            search_res = sp.album_tracks(album_id = album_ID, limit = 50, offset = 50*i)
            for r in search_res['items']:
                track_IDs.append(r['id'])
            next_ = search_res['next']
            i = i + 1
    return track_IDs



def main():
    fire.Fire()



if __name__ == '__main__':

    fire.Fire({
      'getsimilar': getSimilar,
      'usertoptracks': getUserTopTracks,
      'userlovedtracks' : getUserLovedTracks,
      'usertopalbums' : getUserTopAlbums,
      'toptracksbycountry' : getTopTracksByCountry,
      'toptracksbyartist' : getTopTracksByArtist,
      'toptracksbytag' : getTopTracksByTag,
      'toptrackschart' : getTopTracksChart,
      'topalbumsbytag' : getTopAlbumsByTag,
      'showtoptags' : showTopTags,     
      'showtoptagsforartist' : showTopTagsForArtist,
      'showtoptagschart' : showTopTagsChart,
      'showtopartistsbytag' : showTopArtistsByTag,
      'showsimilarartists' : showSimilarArtists,
      'showtoptagsfortrack': showTopTagsForTrack,
      'showtoptagsforalbum': showTopTagsForAlbum,
      'showtopalbumsbytag' : showTopAlbumsByTag
  })

