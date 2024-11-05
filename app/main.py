from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root_page():
    return {"I'm ready."}
