from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from src.routers import ocr_api
from src.config.globals import settings

app = FastAPI(root_path=settings.API_PREFIX)

origins = [
    "http://localhost:5173",
    "http://127.0.0.1:5173",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(ocr_api.router, prefix="/ocr", tags=["ocr"])
