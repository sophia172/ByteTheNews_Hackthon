import os

import uvicorn
from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
from news_summary_extractor import ArticleExtractor
from speak import speak
from fastapi.responses import StreamingResponse
app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
class URLData(BaseModel):
    url: str

@app.post("/api/data")
async def process_everything(request_data: URLData):
    news_url = request_data.url
    article_extractor = ArticleExtractor()
    article_summary =await article_extractor(news_url)
    audio_bytes= await speak(article_summary)
    return StreamingResponse(audio_bytes, media_type="audio/wav")

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0",port=8000)
