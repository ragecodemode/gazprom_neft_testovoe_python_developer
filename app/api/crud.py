from sqlalchemy.orm import Session

from app.db.models import Measurement
from app.schemas.schemas import MeasurementsModel


async def create_measurements(measurements: MeasurementsModel, db: Session):
    measurements = Measurement(**measurements.dict())
    db.add(measurements)
    db.commit()
    db.refresh(measurements)
    return MeasurementsModel.from_orm(measurements)


async def get_device_id(db: Session, device_id: int):
    return db.query(Measurement).filter(
        Measurement.device_id == device_id
    ).all()


async def get_mesurments_all(db: Session):
    return db.query(Measurement).all()
