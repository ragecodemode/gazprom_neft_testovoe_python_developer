### Описание системы:
Система учета и анализа данных, поступающих с условного устройства. Полученные данные привязываются к временной метке и устройству, с которого пришли данные, и сохраняются в БД. Набор данных используется для дальнейшего анализа. 
---

### Стэк:
- FastAPI
- PostgreSQL
- Alembic
- SQLAlchemy
- Pydatic

---

### Запустк проекта

1) В костанту POSTGRES_URL в файле database вставить свои данные от PostgreSQL.
2) Установить requirements.txt и развернуть виртуальное окружение.
3) В файле alembic.ini вставить свои данные от PostgreSQL в переменную: sqlalchemy.url.
4) Запустить файлы DockerFile и docker-compose.yaml командой:
```
Создать .env файл для того, что бы указать свои данные для docker-compose файла: пароль, имя пользователя, имя базы данных.
```
```
docker-compose up -d --build
```
