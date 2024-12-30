from fastapi import FastAPI, Path, HTTPException
from typing import Annotated
from pydantic import BaseModel
from typing import List

app = FastAPI()

users: List['User'] = []


class User(BaseModel):
    id: int
    username: str
    age: int


@app.get("/users")
async def get_user_page():
    return users


@app.post("/user/{username}/{age}")
async def  register_user(
        username: Annotated[str, Path(min_length=1, max_length=50, description="Имя пользователя")],
        age: Annotated[int, Path(ge=1, le=120, description="Возраст пользователя")]
):
    new_id = users[-1].id + 1 if users else 1
    new_user = User(id=new_id, username=username, age=age)
    users.append(new_user)
    return new_user


@app.put("/user/{user_id}/{username}/{age}")
async def update_user(
        user_id: Annotated[int, Path(description="ID пользователя")],
        username: Annotated[str, Path(min_length=1, max_length=50, description="Имя пользователя")],
        age: Annotated[int, Path(ge=1, le=120, description="Возраст пользователя")]
):
    for user in users:
        if user.id == user_id:
            user.username = username
            user.age = age
            return user
    raise HTTPException(status_code=404, detail="User was not found")


@app.delete("/user/{user_id}")
async def delete_user(
        user_id: Annotated[int, Path(description="ID пользователя")]
):
    for user in users:
        if user.id == user_id:
            users.remove(user)
            return user
    raise HTTPException(status_code=404, detail="User was not found")