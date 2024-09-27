from fastapi import APIRouter, Request
from fastapi.templating import Jinja2Templates

router = APIRouter(tags=['Фронтенд'])
templates = Jinja2Templates(directory='app/templates')

# @router.get('/ui/')
# async def get_students_html(request: Request):
#     return templates.TemplateResponse('main.html', context={'request': request})