from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routes.emotion_routes import router as emotion_router

app = FastAPI(title="TuneMind - Emotion Music")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

app.include_router(emotion_router, prefix="/emotion")

@app.get("/")
def read_root():
    return {"message": "Hello TuneMind!"}