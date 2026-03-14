from fastapi import APIRouter
from database import db
from models import CatererProfile, QuoteUpdate


router = APIRouter(prefix="/caterer", tags=["Caterer Dashboard"])


@router.post("/update-profile")
async def update_profile(profile:CatererProfile):
    await db.caterers.update_one(
        {"owner_id": profile.owner_id},
        {"$set": profile.model_dump()},
        upsert=True
    )

    return{"message": "Profile synced to MongoDB!"}
