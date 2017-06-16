# SpotifyPlaylistGenerator

Generate playlists for your spotify account from command line interface: 
<ul>
<li>similar tracks to any track (Uses last.fm's similarTracks method) </li>
<li>your loved tracks from last.fm</li>
<li>your top tracks (weekly, monthly,...) from last.fm</li>
<li>top tracks by an artist, country or tag.</li>
</ul>

<h2>Installation</h2>
<ol>
<li>Clone repository</li>
<li>Install requirements</li>
<li>Fill config.ini file with your API keys</li>
<li>Use one of the functions below</li>
</ol>
<p><strong>Note:</strong> On the first run, open given url with a browser and complete authorization. Then paste redirected url to the console.</p>

<h2>Usage</h2>

<h3>Get Similar Tracks</h3>

parameters: 
<ul>
<li>artist (required):</li>
<li>track (required):</li>
<li>count (optional): default = 20</li>
<li>playlistName (optional): default = "Similar Tracks to {track}"</li>
</ul>

<code>main.py getsimilar --artist="tame impala" --track="let it happen" --count=20</code>

<code>main.py getsimilar --artist="empire of the sun" --track="we are the people" --count=10 --playlistName="example playlist"</code>

<h3>Get Top Tracks</h3>

parameters: 
<ul>
<li>lastFMUserName (required): </li>
<li>period (optional): 7day | 1month | 3month | 6month | 12month | overall. default = 1month</li>
<li>count (optional): default = 20</li>
<li>playlistName (optional): default = "{lastFMUserName}'s Top Songs"</li>
</ul>

<code>main.py usertoptracks lastFMUserName="yourUserName" --period=6month --count=30</code>

<h3>Get Loved Tracks</h3>

parameters: 
<ul>
<li>lastFMUserName (required): </li>
<li>playlistName (optional): default = "Loved Songs by {lastFMUserName}"</li>
</ul>

<code>main.py userlovedtracks "yourUserName"</code>

<h3>Get Top Albums</h3>

parameters: 
<ul>
<li>lastFMUserName (required): </li>
<li>period (optional): 7day | 1month | 3month | 6month | 12month | overall. default = 1month</li>
<li>count (optional): default = 20</li>
<li>playlistName (optional): default = "{lastFMUserName}'s Top Songs"</li>
</ul>

<code>main.py usertopalbums lastFMUserName="yourUserName" --period=6month --count=30</code>

<h3>Get Top Tracks by Country</h3>

Get the most popular tracks on Last.fm last week by country

parameters: 
<ul>
<li>country (required):</li>
<li>count (optional): default = 50</li>
<li>playlistName (optional): default = "{country} Top {count}"</li>
</ul>

<code>main.py toptracksbycountry --country=turkey --count=100</code>

<h3>Get Top Tracks by an Artist</h3>

parameters: 
<ul>
<li>artist (required):</li>
<li>count (optional): default = 20</li>
<li>playlistName (optional): default = "The best {artist} songs"</li>
</ul>

<code>main.py toptracksbyartist --artist="muse" --count="10"</code>

<h3>Get Top Tracks by Tag</h3>

Get the top tracks tagged by this tag.

parameters: 
<ul>
<li>tag (required):</li>
<li>count (optional): default = 25</li>
<li>playlistName (optional): default = "Top {tag} songs"</li>
</ul>

<code>main.py toptracksbytag --tag="indie"</code>

<h3>Get Chart Top Tracks</h3>

Get the top tracks chart

parameters: 
<ul>
<li>count (optional): default = 25</li>
<li>playlistName (optional): default = "Top songs by Last.FM"</li>
</ul>

<code>main.py toptrackschart</code>

<h3>Show Top Tags</h3>

Use this to view the most popular tags on Last.fm

<code>main.py showtoptags</code>

<h3>Show Top Tags For A Track</h3>

Returns the top tags for given track

parameters: 
<ul>
<li>artist (required)</li>
<li>track (required)</li>
</ul>

<code>main.py showtoptagsfortrack --artist="therion" --track="birt of venus illegitima"</code>

<h3>Show Top Artists by Country</h3>

It shows the most popular artists on Last.FM by country.

parameters: 
<ul>
<li>country (required)</li>
</ul>

<code>main.py showtopartistsbycountry --country="turkey"</code>

...

...

<h2>Requirements:</h2>
<ul>
<li><a href = "https://github.com/plamere/spotipy">spotipy</a></li>
<li><a href = "https://github.com/google/python-fire">python-fire</a></li>
</ul>

