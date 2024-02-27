from datetime import datetime

from pydantic import BaseModel


class MeasurementsModel(BaseModel):
    timestamp: datetime
    device_id: int
    x: float
    y: float
    z: float

    class Config:
        orm_mode = True
