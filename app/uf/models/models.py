from pydantic import BaseModel
from datetime import datetime


class UFModel(BaseModel):
    uf: float
    date: str
