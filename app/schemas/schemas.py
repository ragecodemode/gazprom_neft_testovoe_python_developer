from datetime import datetime

from pydantic import BaseModel, ConfigDict


class Measurements(BaseModel):
    timestamp: datetime
    device_id: int
    x: float
    y: float
    z: float

    model_config = ConfigDict(from_attributes=True)
