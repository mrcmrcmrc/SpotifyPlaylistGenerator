# SpotifyPlaylistGenerator

Generate playlists for your spotify account from command line interface: 
<ul>
<li>similar tracks to any track (Uses last.fm's similarTracks method) </li>
<li>your loved tracks from last.fm</li>
<li>your top tracks (weekly, monthly,...) from last.fm</li>
</ul>

<h2> Usage</h2>
<h4>Get Similar Tracks</h4>

getSimilar(artist, track, limit = 20, playlistName = "Similar Tracks"):

<code>main.py getsimilar --artist="tame impala" --track="let it happen" --limit=20</code>

<code>main.py getsimilar --artist="empire of the sun" --track="we are the people" --limit=10 --playlistName="example playlist"</code>

<h4>Get Top Tracks</h4>

getTop(lastFMUserName=lastFMUserName, period="1month", limit = 20, playlistName = "Top Tracks"):

period: 1month, 3month, 6month, 12month, overall

<code>main.py gettop lastFMUserName="yourUserName" --period=6month --limit=30</code>

<h4>Get Loved Tracks</h4>

getLoved(lastFMUserName="yourUserName", playlistName = "Loved Tracks"):

<code>main.py getloved "yourUserName"</code>

<h4>Get Geo Top Tracks</h4>

Get the most popular tracks on Last.fm last week by country

getGeoTop(country, limit=50, playlistName = "Geo Top Tracks"):

<code>main.py getgeotop --country=turkey --limit=100</code>

<h2>Requirements:</h2> 
- <a href = "https://github.com/plamere/spotipy">spotipy</a>

