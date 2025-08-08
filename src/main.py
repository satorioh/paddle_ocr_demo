from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .routers import ocr_api
from .config.globals import settings

# test_file = "./test/1.png"
test_file = "./test/2.pdf"

app = FastAPI(root_path=settings.API_PREFIX)

origins = [
    "http://localhost:8000",
    "http://127.0.0.1:8000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(ocr_api.router, prefix="/ocr", tags=["ocr"])
