from fastapi import APIRouter, Depends
from fastapi.exceptions import HTTPException
from sqlalchemy.orm import Session

from app.api import crud
from app.database import get_db
from app.schemas import schemas
from app.schemas.schemas import MeasurementsModel

measurements_routes = APIRouter(prefix="/measurements", tags=["Measurements"])


@measurements_routes.post("/")
async def create_measurements(
    measurements: schemas.MeasurementsModel,
    db: Session = Depends(get_db)
):
    """Сохранение изменений."""
    return await crud.create_measurements(measurements=measurements, db=db)


@measurements_routes.get(
    "/measurements_all", response_model=list[MeasurementsModel]
)
async def get_measurements(
    db: Session = Depends(get_db)
):
    """Получение всех данных."""
    return await crud.get_mesurments_all(db=db)


@measurements_routes.get(
    "/measurements/{device_id}/", response_model=list[MeasurementsModel]
)
async def get_measurements_by_device_id(
    device_id: int, db: Session = Depends(get_db)
):
    """Получение измерений для устройства."""
    device = await crud.get_device_id(device_id=device_id, db=db)
    if device is None:
        raise HTTPException(status_code=404, detail="Device not found")
    return device


@measurements_routes.get("/measurements/statistics/{device_id}/")
async def get_statistics_by_device_id(
    device_id: int, db: Session = Depends(get_db)
):
    """Вычисление статистики для устройства за период."""
    devices = await crud.get_device_id(device_id=device_id, db=db)
    if devices is None:
        raise HTTPException(status_code=404, detail="Device not found")

    x_values = [device.x for device in devices]
    y_values = [device.y for device in devices]
    z_values = [device.z for device in devices]
    length = x_values + y_values + z_values
    summ = [x + y + z for x, y, z in zip(x_values, y_values, z_values)]
    mediana = [
        (x + y + z) / 2 for x, y, z in zip(x_values, y_values, z_values)
    ]

    return {
        "min_values": min(x_values, y_values, z_values),
        "max_values": max(x_values, y_values, z_values),
        "count": len(length),
        "sum": summ,
        "median": mediana,
    }
