import pydantic
from datetime import date as date_type, time as time_type

class Reminder(pydantic.BaseModel):
    date: date_type = pydantic.Field(
        description="the date at which the user should be reminded"
    )
    time: time_type = pydantic.Field(
        description="the time at which the user should be reminded"
    )
    description: str = pydantic.Field(
        description="the description that should be reminded about"
    )
    is_done: bool = pydantic.Field(
        description="if the reminder is done reminding"
    )