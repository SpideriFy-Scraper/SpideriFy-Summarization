from fastapi import Depends, FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from summarize import get_model, Model

app = FastAPI(title="Statelss Summarization MicroService")

origins = [
    "http://spiderify-api:8080",
    "http://spiderify-api",
    "http://localhost",
    "http://localhost:8080",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class SummarizationRequest(BaseModel):
    text: str


class SummarizationResponse(BaseModel):
    summarized_text: str


@app.post("/predict", response_model=SummarizationResponse)
def predict(request: SummarizationRequest, model: Model = Depends(get_model)):
    return SummarizationResponse(summarized_text=model.predict(request.text))
