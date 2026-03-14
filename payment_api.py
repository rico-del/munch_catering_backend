from fastapi import APIRouter
import base64, httpx
from datetime import datetime

router = APIRouter(prefix="/mpesa", tags=["Payments"])

@router.post("/stk-push")
async def stk_push(phone: str, amount: int):
    tstamp = datetime.now().strftime('%Y%m%d%H%M%S')
    # This is the Daraja Sandbox logic from your photos
    passkey = "bfb279f9aa9bdbcf158e97dd71a467cd2e0c893059b10f78e6b72ada1ed2c919"
    pw = base64.b64encode(f"174379{passkey}{tstamp}".encode()).decode()
    return {"status": "Push Sent", "timestamp": tstamp, "password": pw}