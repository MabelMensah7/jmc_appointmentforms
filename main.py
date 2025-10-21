from fastapi import FastAPI
from routes import appointments

app = FastAPI(title="Japan Medical Center API")

# Include your appointment routes
app.include_router(appointments.router, prefix="/api")

