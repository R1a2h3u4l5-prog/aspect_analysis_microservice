from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from app.aspect_analysis import aspect_sentiment_scores

app = FastAPI()

class ReviewRequest(BaseModel):
    review_text: str

@app.post("/analyze_aspects/")
async def analyze_aspects(request: ReviewRequest):
    try:
        sentiment_scores = aspect_sentiment_scores(request.review_text)
        return {"review_text": request.review_text, "aspect_scores": sentiment_scores}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
