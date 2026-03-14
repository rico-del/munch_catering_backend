import os
from motor.motor_asyncio import AsyncIOMotorClient
from dotenv import load_dotenv

# Load the variables from .env file
load_dotenv()

MONGO_URL = os.getenv("MONGO_URL", "mongodb://localhost:27017")

# This is the actual connection engine
client = AsyncIOMotorClient(MONGO_URL)

# This is our database name. 
# It will show up in MongoDB Compass as 'munch_catering'
db = client.munch_catering



def get_db():
    return db
