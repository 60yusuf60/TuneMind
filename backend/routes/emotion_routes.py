from fastapi import APIRouter
from pydantic import BaseModel
from services.spotify_service import get_song_by_emotion
from services.emotion_service import detect_emotion

router = APIRouter()

class EmotionRequest(BaseModel):
    text: str

class SongResponse(BaseModel):
    name: str
    artist: str
    url: str
    track_id: str

class EmotionResponse(BaseModel):
    text: str
    emotion: str
    song: SongResponse

@router.post("/", response_model=EmotionResponse)
def analyze_emotion(request: EmotionRequest):
    text = request.text
    emotion = detect_emotion(text)
    song = get_song_by_emotion(emotion)
    return {
        "text": text,
        "emotion": emotion,
        "song": song
    }