from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

router = APIRouter()

# Point to your templates folder
templates = Jinja2Templates(directory="templates")

@router.get("/book", response_class=HTMLResponse)
async def book_appointment(request: Request):
    return templates.TemplateResponse("appointments.html", {"request": request})
