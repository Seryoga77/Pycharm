from fastapi import FastAPI, Path, HTTPException
from typing import Annotated

app = FastAPI()

users = {'1': 'Имя: Example, возраст: 18'}


@app.get("/users")
async def get_users():
    return users


@app.post("/user/{username}/{age}")
async def add_user(
        username: Annotated[str, Path(min_length=1, max_length=50, description="Имя пользователя")],
        age: Annotated[int, Path(ge=1, le=120, description="Возраст пользователя")]
):
    new_id = str(max(map(int, users.keys())) + 1)
    users[new_id] = f"Имя: {username}, возраст: {age}"
    return f"User {new_id} is registered"


@app.put("/user/{user_id}/{username}/{age}")
async def update_user(
        user_id: Annotated[str, Path(description="ID пользователя")],
        username: Annotated[str, Path(min_length=1, max_length=50, description="Имя пользователя")],
        age: Annotated[int, Path(ge=1, le=120, description="Возраст пользователя")]
):
    if user_id not in users:
        raise HTTPException(status_code=404, detail=f"User {user_id} not found")
    users[user_id] = f"Имя: {username}, возраст: {age}"
    return f"The user {user_id} is updated"


@app.delete("/user/{user_id}")
async def delete_user(
        user_id: Annotated[str, Path(description="ID пользователя")]
):
    if user_id not in users:
        raise HTTPException(status_code=404, detail=f"User {user_id} not found")
    del users[user_id]
    return f"User {user_id} has been deleted"
