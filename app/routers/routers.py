from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from schemas import schemas


from api import crud
from database import get_db

measurements_routes = APIRouter(prefix='/measurements', tags=['Measurements'])


@measurements_routes.post('/', response_model=schemas.Measurements)
async def create_measurements(measurements: schemas.Measurements, db: Session = Depends(get_db)):
    """Сохранение изменений."""
    return await crud.create_measurements(measurements=measurements, db=db)


@measurements_routes.get('/measurements/{device_id}/',response_model=schemas.Measurements)
async def get_measurements_by_device_id():
    """Получение измерений для устройства."""
    ...


@measurements_routes.get('/measurements/statistics/{device_id}/',response_model=schemas.Measurements
)
async def get_statistics_by_device_id():
    """Вычисление статистики для устройства за период."""
    ...
