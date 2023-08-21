from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel
import uvicorn
from fastapi.templating import Jinja2Templates
templates = Jinja2Templates(directory="templates")

app = FastAPI()

#pip install fastapi
#pip install "uvicorn[standard]"

    
class Users(BaseModel):
    name: str
    email: str
    password: str
    
class Users_id(Users):
    id: int
    
users = [
    Users_id(id=1, name='Kate', email='01@', password='1234'),
    Users_id(id=2, name='Pavel', email='02@', password='1234'),
    Users_id(id=3, name='Yar', email='03@', password='1234')]


@app.get("/", response_model=list[Users_id])
async def get_user():
    return users
 
    
@app.post("/user/", response_model=Users_id)
async def create_user(new_user: Users):
    id = len(users) + 1
    user = Users_id
    user.id = id
    user.name = new_user.name
    user.email = new_user.email
    user.password = new_user.password
    users.append(user)
    return user

    
@app.put("/users/{id}", response_model=Users)
async def update_task(id: int, put_user: Users):
    for user in users:
        if user.id == id:
            user.name = put_user.name
            user.password = put_user.password
            user.email = put_user.email
            return user
    raise HTTPException(status_code=404, detail='User not found')
    

@app.delete("/user/{id}")
async def delete_user(id: int):
    for user in users:
        if user.id == id:
            users.remove(user)
            return users
    raise HTTPException(status_code=404, detail='User not found')


if __name__ == '__main__':
    uvicorn.run(
    "users:app",
    # host="127.0.0.1",
    # port=8000,
    reload=True
    )