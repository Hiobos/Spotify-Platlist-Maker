# Spotify-Platlist-Maker-Top100-Songs
 <h2>Creates playlists with top 100 songs from entered date, webscarping / Spotify API.
<br>Scraping data of 100 most played songs from <a href="https://www.billboard.com/charts/hot-100/">Billboard</a></h2>

<h3><br>modules used:<br>
-spotipy (authentication, adding tracks, creating playlists)<br>
-requests<br>
-Beautifulsoup 4</h3>

<h2>How to use:<br></h2>
<h3>enter spotify for developers (https://developer.spotify.com/dashboard) log in, create an app<br>
and in APIs select "WEB API", redirect uri can be: http://127.0.0.1:9090 <br>
Then in folder keys create:<br>
client_id.txt (paste client id from app dashboard)<br>
client_secret.txt (paste client secret from app dashboard)<br>
redirect_uri.txt (paste redirect uri from dashboard)<br>
Afer launching the app it will ask for a date and then fetch list of tracks from website, <br>
then it will create playlist on your profile and add them one by one.<br>
</h3><h2>
Input:<br>
<img src="img/img.png"><br>
Result:<br>
<img src="img/img_1.png">
</h2>
