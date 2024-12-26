import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from kink import di

from controller.controller import controller

app = FastAPI()
origins = [
    "http://localhost:8080",
    "http://127.0.0.1:5173/",
    "http://localhost:5173/",
    "http://127.0.0.1:8080/",
    # Ajoutez d'autres origines si nécessaire
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    # allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
controller()
try:
    print("add middleware to app")
    app.include_router(di["auth_api_router"], tags=["stockage"], prefix="/auth")
    app.include_router(di["questions_api_router"], tags=["tech"], prefix="/questions")
except Exception as e:
    print(e)
    raise e


@app.get("/")
def read_root():
    return {"Hello": "World"}


if __name__ == "__main__":
    uvicorn.run("main:app", host="localhost", port=8080, reload=True)
