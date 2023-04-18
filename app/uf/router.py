from fastapi import APIRouter
from .controller.controller import get_uf

router = APIRouter()


@router.get("/uf/{date}")
def get(date: str):
    return get_uf(date)
