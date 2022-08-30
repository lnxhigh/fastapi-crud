from fastapi import FastAPI
from fastapi import Form, Request
from urllib import request
from fastapi import HTTPException, status

from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse, RedirectResponse

from typing import Optional
from fastapi import Path

from db import Inventory
from common import getList, getTitleList

app = FastAPI()
app.mount("/static", StaticFiles(directory="static/"), name="static")
templates = Jinja2Templates(directory="templates")

inventory = Inventory.item
id = len(inventory)


# Root
@app.get("/")
async def index(request: Request):
    lists = getList(inventory)
    return templates.TemplateResponse("index.html", {"request": request , "lists": lists})


# Read
@app.get("/items/{id}")    
async def read(
    request: Request,
    id: Optional[int] = Path(None, description="Get Item from id")
):
    if id in inventory:   
        return templates.TemplateResponse("read.html", {
            "request": request,
            "lists": getList(inventory),
            "id": id,
            "title": inventory[id]['title'],
            "content": inventory[id]['description']
        })
    
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)


# Create
@app.get("/create")
async def create(request: Request):
    return templates.TemplateResponse("create.html", {"request": request, "lists": getList(inventory)})

@app.post("/create")
async def create_send(
    request: Request, 
    title: str = Form(...), 
    description: str = Form(...)
):
    if title in getTitleList(inventory):
        return HTMLResponse(f"""
                <script type='text/javascript'>
                    alert('The document named "{title}" already exsits.');
                    window.location.href = "/";
                </script>
        """
        )
    
    global id
    id += 1
    inventory[id] = {"title": title, "description": description}
    return RedirectResponse(f"/items/{id}", status_code=status.HTTP_303_SEE_OTHER)


# Update
@app.get("/update/{id}")
async def update(request: Request, id: int):
    if id not in inventory:
        return HTMLResponse(f"""
                <script type='text/javascript'>
                    alert('The Id does not already exsits.');
                    window.location.href = "/";
                </script>
        """)
    
    return templates.TemplateResponse("update.html", {
        "request": request , 
        "lists": getList(inventory),
        "title": inventory[id]["title"],
        "description": inventory[id]["description"]
        })

@app.post("/update/{id}")
def update_send(
    request: Request, 
    id: int,
    title: str = Form(...), 
    description: str = Form(...)
):
    inventory[id] = {"title": title, "description": description}
    return RedirectResponse(f"/items/{id}", status_code=status.HTTP_303_SEE_OTHER)


# Delete
@app.post("/delete")
def delete(request: Request, id: int = Form(...)):
    del inventory[id]

    return HTMLResponse("""
        <script>
            alert('Successfully deleted.');
            window.location.href = "/";
        </script>
    """)
