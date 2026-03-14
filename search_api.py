from fastapi import APIRouter
from database import db 

router = APIRouter(prefix="/search", tags=["Search & Discovery"])


@router.get("/caterers")
async def get_all_caterers(tier:str = None):
    query = {"tiers.name": tier} if tier else{}
    return await db.caterers.find(query).to_list(100)