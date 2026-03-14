from fastapi import APIRouter
from database import db
from models import BookingRequest
from bson import ObjectId
from models import BookingRequest, CustomQuote

router = APIRouter(prefix="/bookings", tags=["Bookings"])

@router.post("/create")
async def create_booking(req: BookingRequest):
    caterer = await db.caterers.find_one({"_id": ObjectId(req.caterer_id)})
    # Find price from the selected tier
    tier_price = next(t["price_per_head"] for t in caterer["tiers"] if t["name"] == req.selected_tier)
    
    total = req.guest_count * tier_price
    booking = {
        "customer_phone": req.customer_phone,
        "total": total,
        "deposit_20": total * 0.20,
        "balance_80": total * 0.80,
        "status": "Awaiting Deposit"
    }
    res = await db.bookings.insert_one(booking)
    return {"id": str(res.inserted_id), "deposit": total * 0.20}


@router.post("/request-quote")
async def request_quote(quote:CustomQuote):
    quote_data = quote.model_dump()
    quote_data["status"] = "pending_review"
    await db.quotes.insert_one(quote.model_dump) #stores custom requests individual caterers will review later

    return {"message": "Quote request sent! Our team will contact you."}