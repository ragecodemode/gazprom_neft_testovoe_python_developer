import models
from schemas.schemas import Measurements
from sqlalchemy.orm import Session


async def create_measurements(measurements: Measurements, db: Session):
    measurements = models.Measurement(**measurements.dict())
    db.add(measurements)
    db.commit()
    db.refresh(measurements)
    return Measurements.from_orm(measurements)
