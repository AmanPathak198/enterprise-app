from fastapi import FastAPI

app = FastAPI(title="Enterprise App")

@app.get('/')
async def get_greetings():
    return{"Message":"Hello You"}