import uvicorn
from transformers import pipeline
from fastapi import FastAPI, Query

app = FastAPI()
@app.get("/SentimentAnalyzer")
async def SentimentAnalyzer(q: str = Query(None, max_length = 1000)):
    try:
        sentiment_pipeline = pipeline("sentiment-analysis")
        result = sentiment_pipeline(q)
        SentimentType = result[0]['label']
        SentimentValue = result[0]['score']
        return {"SentimentType": SentimentType, "SentimentValue": SentimentValue}
    except Exception as e:
        return {"Error": str(e), "SentimentType": None, "SentimentValue": 0.0}


if __name__ == '__main__':
    uvicorn.run(app ,host="0.0.0.0",port=9005)

