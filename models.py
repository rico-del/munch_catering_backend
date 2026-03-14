from pydantic import BaseModel, EmailStr
from typing import List, Optional

class UserRegister(BaseModel):
    full_name: str
    email: EmailStr
    password: str
    role: str = "customer" # customer or caterer

class UserLogin(BaseModel):
    email: EmailStr
    password: str

class MenuTier(BaseModel):
    name: str  # Standard, Premium, Deluxe
    price_per_head: float
    items: List[str]

class CatererProfile(BaseModel):
    business_name: str
    owner_id: str
    description: str
    tiers: List[MenuTier]

class BookingRequest(BaseModel):
    caterer_id: str
    customer_phone: str
    guest_count: int
    selected_tier: str

class CustomQuote(BaseModel):
    user_id: str
    description: str
    guest_count: int
    budget_estimate: float

class QuoteUpdate(BaseModel):
    quote_id: str
    status: str #for example "approved", "rejected" & "contacted"
    cateerr: str

