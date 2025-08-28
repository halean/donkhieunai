import gradio as gr
import nest_asyncio
import sklearn
import torch
from fastapi import FastAPI, Request, WebSocket, WebSocketDisconnect
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

templates = Jinja2Templates(directory="templates")
from troly_dontu import troly

nest_asyncio.apply()
app = FastAPI()


app = gr.mount_gradio_app(app, troly.demo, path="/app1")
# app = gr.mount_gradio_app(app, pwc.demo, path="/app2")
# app = gr.mount_gradio_app(app, pwc.demo, path="/app3")
# app = gr.mount_gradio_app(app, gr_autogen_jupyterlite.demo, path="/app3")
# app.mount("/autogen_jupyterlite", gr_autogen_jupyterlite.app)


# Serve the main HTML page
@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})