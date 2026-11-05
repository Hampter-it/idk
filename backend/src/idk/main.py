from fastapi import FastAPI


app = FastAPI(title="IDK API")


@app.get("/health")
def get_docs():
    return {"status": "ok"}


