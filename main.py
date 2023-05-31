from fastapi import FastAPI
from routers import auticka


app = FastAPI()

app.include_router(auticka.router)

