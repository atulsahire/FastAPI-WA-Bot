from fastapi import FastAPI, Request, HTTPException, Query
from engine import handle_message
from dotenv import load_dotenv
from fastapi.responses import FileResponse
from pathlib import Path
import os

load_dotenv()
app = FastAPI()
VERIFY_TOKEN = os.getenv("VERIFY_TOKEN")

# Health check
@app.get("/")
async def home():
    return {"message": "API is up"}

# Webhook verification
from fastapi.responses import PlainTextResponse

@app.get("/webhook")
async def verify_webhook(
    hub_mode: str = Query(None, alias="hub.mode"),
    hub_challenge: str = Query(None, alias="hub.challenge"),
    hub_verify_token: str = Query(None, alias="hub.verify_token")
):
    print("hub_mode:", hub_mode)
    print("hub_challenge:", hub_challenge)
    print("hub_verify_token:", hub_verify_token)
    my_tkn = "atul-access-token"
    print("in verify_webhook")
    if hub_mode == "subscribe" and hub_verify_token == my_tkn:
        # Return as plain text to ensure Meta's validator accepts it
        print("sending resposne :",hub_challenge)
        return PlainTextResponse(content=hub_challenge)
    raise HTTPException(status_code=403, detail="Verification failed")

# Handle incoming messages
@app.post("/webhook")
async def handle_webhook(request: Request):
    data = await request.json()
    print("Received webhook:", data)

    if data:
        for entry in data.get("entry", []):
            for change in entry.get("changes", []):
                value = change.get("value", {})
                phone_number_id = value.get("metadata", {}).get("phone_number_id")
                message_data = value.get("messages", [])
                for message in message_data:
                    handle_message(message, phone_number_id)

    return {"status": "EVENT_RECEIVED"}

@app.get("/get_image")
async def get_image():
    image_path = Path("C:\\Users\\User\\Downloads\\library.jpg")
    print(image_path)
    if not image_path.is_file():
        return {"error": "Image not found on the server"}
    return FileResponse(image_path)


@app.get("/get_file/{filename}")
async def get_file(filename: str):
    image_path = Path("C:\\PID\\YPCPL\\NewsLetter\\newsletter_pdf\\"+filename)
    if not image_path.is_file():
        return {"error": "file not found on the server"}
    return FileResponse(image_path)


@app.get("/items/{item_id}")
async def read_item(item_id: int):
    return {"item_id": item_id}