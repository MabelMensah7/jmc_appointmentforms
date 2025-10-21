from fastapi import FastAPI
from fastapi.responses import RedirectResponse
from routes import appointments

app = FastAPI(title="Japan Medical Center API")

# Redirect root (/) to the booking page
@app.get("/")
def root_redirect():
    return RedirectResponse(url="/api/book")

# Include appointments router
app.include_router(appointments.router, prefix="/api")
