from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def read_root():
    return "Главная страница"


@app.get("/user/admin")
async def read_admin():
    return "Вы вошли как администратор"


@app.get("/user/{user_id}")
async def read_user(user_id: str):
    return f"Вы вошли как пользователь № {user_id}"


@app.get("/user")
async def read_user_info(username: str, age: str):
    return f"Информация о пользователе. Имя: {username}, Возраст: {age}"
