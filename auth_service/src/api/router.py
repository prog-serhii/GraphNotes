from dependency_injector.wiring import Provide, inject
from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordRequestForm


router = APIRouter()


def dependency(provider):
    return Depends(Provide[provider])


@router.post('/login')
@inject
async def login(
    form_data: OAuth2PasswordRequestForm = Depends(),

):
    pass
