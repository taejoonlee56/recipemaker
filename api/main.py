from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import requests
import json

app = FastAPI()

class Query(BaseModel):
    prompt: str
    model: str = "test"

@app.post("/generate")
async def generate_text(query: Query):
    try:
        response = requests.post(
            "http://localhost:11434/api/generate",
            json={"model": query.model, "prompt": query.prompt},
            stream=True  # 응답을 스트리밍 방식으로 받기 위함
        )

        response_text = ""
        for line in response.iter_lines():
            if line:
                line_data = json.loads(line.decode("utf-8"))
                response_text += line_data.get("response", "")

        return {"generated_text": response_text}
    except requests.RequestException as e:
        raise HTTPException(status_code=500, detail=f"Error communicating with Ollama: {str(e)}")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
