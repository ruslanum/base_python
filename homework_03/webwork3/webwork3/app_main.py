from fastapi import FastAPI

app = FastAPI()


@app.get("/ping", summary="Returns pong")
def hello():
    return {"message": "pong"}
