""" this is just a test modul to test some code """
import datetime
from dataclasses import dataclass

@dataclass
class ApaInfo:
    api_id: str
    create_date: datetime
    update_date: datetime
