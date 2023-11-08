import uvicorn
from fastapi import FastAPI, Request, Response
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

app = FastAPI()
templates = Jinja2Templates(directory="templates")


@app.get("/")
async def root(request: Request):
    """Root endpoint"""
    return templates.TemplateResponse(
        "index.html", {"request": request, "message": "Hello, World!"}
    )


@app.get("/contact", response_class=HTMLResponse)
async def contact(request: Request):
    """Contact endpoint"""
    return templates.TemplateResponse(
        "contact.html",
        {"request": request, "address": "Montreal, Quebec", "phone": "000-000-6969"},
    )


@app.post("/contact")
async def contact_post(request: Request, response: Response):
    """Contact endpoint"""
    form = await request.form()
    name = form.get("name")
    email = form.get("email")
    message = form.get("message")
    if not name or not email or not message:
        response.status_code = 400
        return {"error": "Please fill out all fields."}
    return {"name": name, "email": email, "message": message}


if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=8000)
