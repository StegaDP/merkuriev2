import datetime
from dataclasses import dataclass


@dataclass()
class User:
    id: int
    can_create: bool
    can_approve: bool
    can_pay: bool


@dataclass()
class Report:
    id: int
    document_name: str
    creation_date: datetime.datetime
    approve_date: datetime.datetime
    payment_date: datetime.datetime
    description: str
