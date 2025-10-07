from contextlib import asynccontextmanager

from fastapi import FastAPI
from fastapi.responses import RedirectResponse
from fastapi.middleware.cors import CORSMiddleware

from config.database import get_db
from routers.user_router import user_router
from routers.auth_router import auth_router
from routers.phone_router import phone_router
from routers.contact_router import contact_router

db = get_db()


@asynccontextmanager
async def lifespan(_: FastAPI):
    if db.is_closed():
        db.connect()
    try:
        yield
    finally:
        if not db.is_closed():
            db.close()

app = FastAPI(lifespan=lifespan, title='Contact Flow API', version='1.0.0')

app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_methods=['*'],
    allow_headers=['*'],
    allow_credentials=True
)


@app.get('/')
def read_root():
    return RedirectResponse(url='/docs')


app.include_router(user_router)
app.include_router(auth_router)
app.include_router(phone_router)
app.include_router(contact_router)
