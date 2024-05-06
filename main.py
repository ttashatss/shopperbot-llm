from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional
import uvicorn

from functions.get_answer import get_answer

class Input(BaseModel):
    userId: str
    userInfo: Optional[str] = None
    prompt: str
    location: Optional[str] = None

app = FastAPI()

@app.post("/")
async def api_post(input: Input):
    print(input)
    answer = get_answer(input.prompt)
    return answer

# if __name__ == "__main__":
#     prompt = 'From this question, what is the correct choice - you can answer with only one letter A, B, C, or D? Question: What is the capital of France? Choice: A. Paris B. London C. Berlin D. Madrid'
#     print(get_answer(prompt))