# 🎶 Spotify Time Machine Playlist Maker

Create a Spotify playlist with the **top 100 Billboard hits** from any past date!

This tool scrapes historical music data from the [Billboard Hot 100](https://www.billboard.com/charts/hot-100/) and uses the Spotify API to create a playlist with the matching songs.

---

## 🚀 Features

- 🔧 Scrapes Billboard's Top 100 songs from a selected date  
- 📀 Creates a playlist on your Spotify profile  
- 🎵 Adds available songs to your new playlist  

---

## 📦 Requirements

- `spotipy`  
- `requests`  
- `beautifulsoup4`  

---

Install dependencies using:

```bash
pip install spotipy requests beautifulsoup4
```

---

## 🛠️ Setup Instructions
Go to the Spotify Developer <a href='https://developer.spotify.com/dashboard'>Dashboard</a>

Log in and create a new app

Under Redirect URI, use:
http://127.0.0.1:9090
In your project folder, create a keys directory with the following files:<br />
keys/<br />
├── client_id.txt         # Your Spotify Client ID<br />
├── client_secret.txt     # Your Spotify Client Secret<br />
└── redirect_uri.txt      # Your redirect URI<br />
Paste the appropriate values from your Spotify App Dashboard into each file

---
## Usage

Run the app:
```bash
python main.py
```
When prompted, enter a date in the format:

```bash
YYYY-MM-DD
```
The script will:
<ol>
 <li>Scrape the Billboard chart from that date</li>

 <li>Search each song on Spotify</li>

 <li>Create a new playlist</li>

 <li>Add found songs to the playlist</li>
</ol>

---

##💡 Example


Input:<br>
```bash
2025-04-12
```
Result:<br>
<img src="img/img_1.png">

