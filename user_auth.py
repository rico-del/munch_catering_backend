from fastapi import APIRouter, HTTPException
from database import db # Ensure you have a database.py with 'db'
from models import UserRegister, UserLogin
from auth_utils import hash_password, verify_password, create_token

router = APIRouter(prefix="/auth", tags=["Auth"])

@router.post("/register")
async def register(user: UserRegister):
    user_exists = await db.users.find_one({"email": user.email})
    if user_exists: raise HTTPException(400, "Email taken")
    u_dict = user.dict()
    u_dict["password"] = hash_password(user.password)
    await db.users.insert_one(u_dict)
    return {"msg": "Registered"}

@router.post("/login")
async def login(user: UserLogin):
    db_u = await db.users.find_one({"email": user.email})
    if not db_u or not verify_password(user.password, db_u["password"]):
        raise HTTPException(401, "Invalid")
    return {"token": create_token({"sub": user.email})}