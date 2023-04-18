import requests
from fastapi import HTTPException
from http import HTTPStatus
from datetime import datetime
from bs4 import BeautifulSoup
from app.uf.services.services import get_uf_from_html


def get_uf(date: str):
    req_date = datetime.strptime(date, "%d-%m-%Y")
    limit_date = datetime(2013, 1, 1)
    if req_date < limit_date:
        raise HTTPException(
            status_code=HTTPStatus.BAD_REQUEST,
            detail="La fecha mínima permitida es 01-01-2013",
        )

    url = f"https://www.sii.cl/valores_y_fechas/uf/uf{req_date.year}.htm"
    req = requests.get(url)
    if req.status_code == 404:
        raise HTTPException(
            status_code=HTTPStatus.NOT_FOUND,
            detail="No se encontró la página de la UF para este año",
        )

    # print("text: ", req.text)
    return get_uf_from_html(req.text, req_date)
