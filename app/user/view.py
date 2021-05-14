import requests
from fastapi import APIRouter, Depends

from app.immo.model import City
from app.user.model import User
from app.utils import get_email

router = APIRouter(
    prefix="/user",
    tags=["User"],
    dependencies=[Depends(get_email)],
    responses={404: {"description": "Not found"}},
)


@router.get('/me', response_model=User)
def get_me(email=Depends(get_email)):
    return {"email": email}
