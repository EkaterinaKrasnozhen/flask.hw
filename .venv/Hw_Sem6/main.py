import uvicorn
from fastapi import FastAPI
from database import *
import us
import ord
import prod

app = FastAPI()
#templates = Jinja2Templates(directory="templates")


@app.on_event("startup")
async def startup():
    await database.connect()
    
    
@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()
    
    
app.include_router(us.router, tags=["users"])
app.include_router(prod.router, tags=["products"])
app.include_router(ord.router, tags=["orders"])


if __name__ == '__main__':
    uvicorn.run(
    "main:app",
    reload=True
    )