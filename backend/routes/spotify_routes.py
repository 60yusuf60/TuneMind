from fastapi import APIRouter, Body
from services.spotify_service import get_song_by_emotion

router = APIRouter(prefix="/spotify", tags=["spotify"])

@router.post("/")
def fetch_song(emotion: str = Body(..., embed=True)):
    """
    Receives detected emotion and returns a song from Spotify.
    """
    song = get_song_by_emotion(emotion)
    return {"emotion": emotion, "song": song}