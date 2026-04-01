from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse  # Added this import
from api.routers import tasks
from repositories.models import Base
from db import engine
from fastapi.concurrency import asynccontextmanager

# Lifespan to create tables at startup
@asynccontextmanager
async def lifespan(app: FastAPI):
    try:
        Base.metadata.create_all(bind=engine)
        print("✅ Tables created")
    except Exception as e:
        print("❌ DB error:", e)
    yield
    print("🛑 App shutting down")

app = FastAPI(lifespan=lifespan)

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(tasks.router, prefix="/tasks")


@app.get("/")
async def serve_index():
    return FileResponse("index.html")

