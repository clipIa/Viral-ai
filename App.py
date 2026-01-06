from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import subprocess

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

class Req(BaseModel):
    url: str

@app.post("/generate")
def generate(req: Req):
    subprocess.run(["yt-dlp", "-o", "video.mp4", req.url])
    subprocess.run([
        "ffmpeg", "-i", "video.mp4",
        "-ss", "30", "-to", "55",
        "-vf", "scale=1080:1920",
        "short.mp4"
    ])
    return {"ok": True, "message": "Short generado"}
