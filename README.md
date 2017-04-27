# SpotifyPlaylistGenerator

Generate playlists for your spotify account from command line interface: 
<ul>
<li>similar tracks to any track (Uses last.fm's similarTracks method) </li>
<li>your loved tracks from last.fm</li>
<li>your top tracks (weekly, monthly,...) from last.fm</li>
<li>top tracks by an artist, country or tag.</li>
</ul>

<h2> Usage</h2>
<h4>Get Similar Tracks</h4>

parameters: 
<ul>
<li>artist (required):</li>
<li>track (required):</li>
<li>count (optional): default = 20</li>
<li>playlistName (optional): default = "Similar Tracks to {track}"</li>
</ul>

<code>main.py getsimilar --artist="tame impala" --track="let it happen" --count=20</code>

<code>main.py getsimilar --artist="empire of the sun" --track="we are the people" --count=10 --playlistName="example playlist"</code>

<h4>Get Top Tracks</h4>

parameters: 
<ul>
<li>lastFMUserName (required): </li>
<li>period (optional): 7day | 1month | 3month | 6month | 12month | overall. default = 1month</li>
<li>count (optional): default = 20</li>
<li>playlistName (optional): default = "{lastFMUserName}'s Top Songs"</li>
</ul>

<code>main.py gettop lastFMUserName="yourUserName" --period=6month --count=30</code>

<h4>Get Loved Tracks</h4>

parameters: 
<ul>
<li>lastFMUserName (required): </li>
<li>playlistName (optional): default = "Loved Songs by {lastFMUserName}"</li>
</ul>

<code>main.py getloved "yourUserName"</code>

<h4>Get Top Tracks by Country</h4>

Get the most popular tracks on Last.fm last week by country

parameters: 
<ul>
<li>country (required):</li>
<li>count (optional): default = 50</li>
<li>playlistName (optional): default = "{country} Top {count}"</li>
</ul>

<code>main.py gettopbycounty --country=turkey --count=100</code>

<h4>Get Top Tracks by an Artist</h4>

parameters: 
<ul>
<li>artist (required):</li>
<li>count (optional): default = 20</li>
<li>playlistName (optional): default = "The best {artist} songs"</li>
</ul>

<code>main.py gettopbyartist --artist="muse" --count="10"</code>

<h4>Get Top Tracks by Tag</h4>
Get the top tracks tagged by this tag.
parameters: 
<ul>
<li>tag (required):</li>
<li>count (optional): default = 25</li>
<li>playlistName (optional): default = "Top {tag} songs"</li>
</ul>

<code>main.py gettopbytag --tag="indie"</code>

<h4>Get Chart Top Tracks</h4>
Get the top tracks chart
parameters: 
<ul>
<li>count (optional): default = 25</li>
<li>playlistName (optional): default = "Top songs by Last.FM"</li>
</ul>

<code>main.py getcharttoptracks"</code>

<h4>Show Top Tags</h4>
Use this to view the most popular tags on Last.fm
<code>main.py showtoptags</code>

<h2>Requirements:</h2> 
- <a href = "https://github.com/plamere/spotipy">spotipy</a>
- <a href = "https://github.com/google/python-fire">python-fire</a>

