# import the packages
from typing import Union
from fastapi import FastAPI

# app instance
app = FastAPI()

# app endpoints
@app.get("/test")
async def test():
    return "Test route working"

@app.get("/home")
async def home():
    return "Hello world"
