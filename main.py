from fastapi import FastAPI
from motor.motor_asyncio import AsyncIOMotorClient
import os

# Import all our logic
from user_auth import router as auth
from booking_api import router as booking
from payment_api import router as payment
from caterer_api import router as caterer
from search_api import router as search

app = FastAPI(title="Munch Catering API")

# DB Connection
client = AsyncIOMotorClient("mongodb://localhost:27017")
db = client.munch_catering

# Connect all 6 APIs
app.include_router(auth)
app.include_router(booking)
app.include_router(payment)
app.include_router(caterer)
app.include_router(search)

@app.get("/")
async def root(): return {"status": "Vegan API Online"}