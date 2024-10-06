from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from app.pages.router import router as pages_router
from fastapi.staticfiles import StaticFiles
from fastapi.responses import JSONResponse



app = FastAPI()
app.include_router(pages_router)
    

templates = Jinja2Templates(directory='app/templates')
app.mount("/static", StaticFiles(directory="app/static"), name="static")

@app.get("/")
async def root(request: Request):
    return templates.TemplateResponse('main.html', context={'request': request})

@app.get("/tasks/")
async def root(request: Request):
    return templates.TemplateResponse('tasks.html', context={'request': request})

@app.get("/plugins/")
async def root(request: Request):
    return templates.TemplateResponse('plugins.html', context={'request': request})

@app.get("/settings/")
async def root(request: Request):
    return templates.TemplateResponse('settings.html', context={'request': request})




