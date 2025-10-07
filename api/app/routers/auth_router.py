from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordRequestForm

from schemas.user_schema import UserCreate
from routers.dependencies import oauth2_schema
from services.auth_service import AuthService

auth_router = APIRouter(
    prefix='/auth',
    tags=['Authentication']
)

auth_service = AuthService()


@auth_router.post('/signin')
def signin(user: OAuth2PasswordRequestForm = Depends()):
    access_token = auth_service.authenticate(user)
    return access_token


@auth_router.post('/signup')
def signup(user: UserCreate):
    return auth_service.create_user(user)


@auth_router.get('/profile')
def profile(token: str = Depends(oauth2_schema)):
    return auth_service.decode_token(token)
