import requests
from fastapi import APIRouter, Depends

from app.immo.model import City
from app.utils import get_email

router = APIRouter(
    prefix="/immoprice",
    tags=["Prix immo"],
    dependencies=[Depends(get_email)],
    responses={404: {"description": "Not found"}},
)


@router.post('')
def get_sales(city: City):
    res = requests.get(f'https://a-effiprices.efficity.com/map/dvf/0.{city.codeRegion}.{city.codeDepartement}.{city.code}')
    return res.json()
