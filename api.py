from fastapi import Depends, FastAPI
from pydantic import BaseModel
from summarize import get_model, Model


app = FastAPI()


class SummarizationRequest(BaseModel):
    text: str


class SummarizationResponse(BaseModel):
    summarized_text: str


@app.post("/predict", response_model=SummarizationResponse)
def predict(request: SummarizationRequest, model: Model = Depends(get_model)):
    return SummarizationResponse(summarized_text=model.predict(request.text))
