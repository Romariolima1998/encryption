from fastapi import FastAPI
from encryption.routers import views

app = FastAPI()

app.include_router(views.encryption)

@app.get('/')
def hello_world():
    return {'hello': 'world'}