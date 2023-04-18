from datetime import datetime
from bs4 import BeautifulSoup
from app.uf.models.models import UFModel


def get_uf_from_html(html: str, date: datetime):
    month = parse_month(date.month)
    soup = BeautifulSoup(html, "html.parser")
    month_tag = soup.find("div", {"id": f"mes_{month}"})
    uf_value = month_tag.find("th", text=f"{date.day}").find_next_sibling("td").text
    uf = uf_value.replace(".", "").replace(",", ".")
    return UFModel(uf=float(uf), date=date.strftime("%d-%m-%Y"))


def parse_month(month: int):
    months = {
        1: "enero",
        2: "febrero",
        3: "marzo",
        4: "abril",
        5: "mayo",
        6: "junio",
        7: "julio",
        8: "agosto",
        9: "septiembre",
        10: "octubre",
        11: "noviembre",
        12: "diciembre",
    }
    return months[month]
