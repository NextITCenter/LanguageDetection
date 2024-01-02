from fastapi import FastAPI, Form, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel

from service import detect_language
import uvicorn

app = FastAPI()

app.mount('/static', StaticFiles(directory='static'), name='static')

templates = Jinja2Templates(directory='templates')


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}


@app.get("/lang")
async def get_lang(request: Request):
    return templates.TemplateResponse(request=request, name="lang.html")


# @app.post("/lang")
# async def post_lang(request: Request, text: str = Form()):
#     result_lang = detect_language(text)
#     return templates.TemplateResponse(request=request, name="lang.html", context={"text": text, "msg": result_lang})


class Item(BaseModel):
    text: str


# fastpai는 함수 매개변수가 request header에 있는 내용만 매핑시켜준다.
# 만약 request body에 있는 내용을 가져오려면 pydantic 라이브러리를 통해 매핑시켜야 한다.
@app.post("/lang")
async def post_lang(item: Item):
    result_lang = detect_language(item.text)
    return {"text": item.text, "msg": result_lang}


if __name__ == "__main__":
    uvicorn.run('main:app', host='0.0.0.0', port=8000, reload=True)