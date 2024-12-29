from fastapi import FastAPI, Path, Query
from fastapi.responses import JSONResponse

app = FastAPI()

@app.get("/")
def read_root():
    return JSONResponse(content={"message": "Главная страница"})

@app.get("/user/admin")
def read_admin():
    return JSONResponse(content={"message": "Вы вошли как администратор"})

@app.get("/user/{user_id}")
def read_user(
    user_id: int = Path(
        ...,
        ge=1,
        le=100,
        description="Введите ID пользователя",
        example=1
    )
):
    return JSONResponse(content={"message": f"Вы вошли как пользователь № {user_id}"})

@app.get("/user/{username}/{age}")
def read_user_info(
    username: str = Path(
        ...,
        min_length=5,
        max_length=20,
        description="Введите имя пользователя",
        example="UrbanUser"
    ),
    age: int = Path(
        ...,
        ge=18,
        le=120,
        description="Введите возраст",
        example=24
    )
):
    return JSONResponse(content={"message": f"Информация о пользователе. Имя: {username}, Возраст: {age}"})


