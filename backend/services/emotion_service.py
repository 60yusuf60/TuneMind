from transformers import pipeline

"""
Uses a pre-trained Hugging Face model to detect emotions from text.
Detected emotions are mapped to Spotify-friendly categories to fetch the perfect song.
"""

emotion_classifier = pipeline(
    "text-classification",
    model="j-hartmann/emotion-english-distilroberta-base",
    top_k=1
)

EMOTION_MAP = {
    "joy": "happy",
    "sadness": "sad",
    "anger": "angry",
    "fear": "sad",
    "disgust": "angry",
    "surprise": "happy",
    "neutral": "neutral"
}

def detect_emotion(message: str) -> str:
    try:
        result = emotion_classifier(message)
        label = result[0][0]["label"].lower()
        return EMOTION_MAP.get(label, "neutral")
    except Exception as e:
        print("Emotion detection error:", e)
        return "neutral"