from pydantic import BaseModel

class CreateUser(BaseModel):
    username: str
    firstname: str
    lastname: str
    age: int

class UpdateUser(BaseModel):
    firstname: str
    lastname: str
    age: int

class Createtask(BaseModel):
    title: str
    content: str
    priority: int

class Updatetask(BaseModel):
    title: str
    content: str
    priority: int


