import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import random
import os
from dotenv import load_dotenv

load_dotenv()

CLIENT_ID = os.getenv("SPOTIPY_CLIENT_ID")
CLIENT_SECRET = os.getenv("SPOTIPY_CLIENT_SECRET")

auth_manager = SpotifyClientCredentials(client_id=CLIENT_ID, client_secret=CLIENT_SECRET)
sp = spotipy.Spotify(auth_manager=auth_manager)

EMOTION_QUERIES = {
    "happy": [
        "happy upbeat pop",
        "feel good summer hits",
        "energetic dance music",
        "positive vibes playlist",
        "uplifting indie pop"
    ],
    "sad": [
        "sad emotional acoustic",
        "heartbreak ballad",
        "melancholic indie",
        "sad piano music",
        "lonely night songs"
    ],
    "angry": [
        "angry rock metal",
        "intense workout music",
        "aggressive hip hop",
        "hard rock energy",
        "punk rock rage"
    ],
    "neutral": [
        "chill ambient relaxing",
        "lofi hip hop study",
        "popular hits today",
        "indie pop mix",
        "soft jazz evening"
    ]
}

def get_song_by_emotion(emotion: str) -> dict:
    queries = EMOTION_QUERIES.get(emotion.lower(), EMOTION_QUERIES["neutral"])
    query = random.choice(queries)
    offset = random.randint(0, 40)

    try:
        results = sp.search(q=query, type="track", limit=10, offset=offset)
    except Exception as e:
        print("Spotify API Error:", e)
        return {"name": "No song found", "artist": "", "url": "", "track_id": ""}

    tracks = results.get("tracks", {}).get("items", [])
    if not tracks:
        return {"name": "No song found", "artist": "", "url": "", "track_id": ""}

    track = random.choice(tracks)
    return {
        "name": track["name"],
        "artist": track["artists"][0]["name"],
        "url": track["external_urls"]["spotify"],
        "track_id": track["id"]
    }
