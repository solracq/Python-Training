# app.py
import asyncio
from fastapi import FastAPI

app = FastAPI()

@app.get("/slow")
async def slow():
    await asyncio.sleep(10)
    return "That was slow!"

@app.get("/fast")
async def fast():
    return "That was fast!"
