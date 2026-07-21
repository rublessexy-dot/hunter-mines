from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse, HTMLResponse
from pathlib import Path

app = FastAPI(
    title="Mines MiniApp",
    version="1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

BASE_DIR = Path(__file__).resolve().parent.parent


@app.get("/", response_class=HTMLResponse)
async def index():
    return """
    <html>
        <body style="background:red;color:white;font-size:50px;">
            ПРОВЕРКА
        </body>
    </html>
    """

@app.get("/ping")
async def ping():
    return {"ping": "pong"}