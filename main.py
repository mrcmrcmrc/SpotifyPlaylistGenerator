#!/usr/bin/python
import spotipy
import spotipy.util as util
import lastFM
import fire
import ConfigParser


config = ConfigParser.RawConfigParser()
config.read('config.ini')
    
username = config.get('Spotify', 'UserName')
client_id = config.get('Spotify', 'client_id')
client_secret = config.get('Spotify', 'client_secret')
lastFMUserName = config.get('Last.FM', 'UserName')



def getSimilar(artist, track, limit = 20, playlistName = "Similar Tracks"):
    print "%s similar tracks to %s" % (limit, track)
    artists,tracks = lastFM.getSimilar(artist = artist, track = track, limit = limit)
    generatePlaylist(artists, tracks, playlistName)



def getTop(lastFMUserName=lastFMUserName, period="1month", limit = 20, playlistName = "Top Tracks"):
    print "%s\'s top %s tracks (%s)" % (lastFMUserName, limit, period)
    artists, tracks = lastFM.getTopTracks(lastFMUserName, period=period, limit=limit) #period="overall"
    generatePlaylist(artists, tracks, playlistName)



def getLoved(lastFMUserName=lastFMUserName, playlistName = "Loved Tracks"):
    print "%s\'s loved tracks" % lastFMUserName
    artists, tracks = lastFM.getLovedTracks(lastFMUserName)
    generatePlaylist(artists, tracks, playlistName)



def generatePlaylist(artists, tracks, playlistName):
    
    scope = "playlist-modify-public"
    
    token = util.prompt_for_user_token(username=username, client_id=client_id, client_secret=client_secret, redirect_uri="http://localhost:80", scope=scope)
    
    track_IDs = []
    filters=['/', '.', 'ft', 'feat', '-', '[', '(', '~']
    if len(artists) is not 0:
        sp = spotipy.Spotify()
        for index, artist in enumerate(artists):
            try:
                search_res = sp.search(q=artist + " " + tracks[index], type='track', limit=1, market='TR')
            except:
                
                 "err"
            if len(search_res['tracks']['items']) == 0:
                for letter in tracks[index]:
                    if letter in filters:
                        search_res = sp.search(q=artist + " " + tracks[index].split(letter)[0], type='track', limit=1, market='TR')
                        break
                if len(search_res['tracks']['items']) > 0:
                    if search_res['tracks']['items'][0]['id'] not in track_IDs:
                        track_IDs.append(search_res['tracks']['items'][0]['id'])
                        print artist + " - " + tracks[index] + "****************"
                else:
                    print "couldn't find " + artist + " - " + tracks[index]
                continue
            if search_res['tracks']['items'][0]['id'] not in track_IDs:
                track_IDs.append(search_res['tracks']['items'][0]['id'])
                print artist + " - " + tracks[index] + "............."

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
                print playlistName + " has been created successfully"

        else:
            print("Can't get token for ", username)



def main():
    fire.Fire()



if __name__ == '__main__':
  fire.Fire({
      'getsimilar': getSimilar,
      'gettop': getTop,
      'getloved' : getLoved,
  })

