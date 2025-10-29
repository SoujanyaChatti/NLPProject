from fastapi import FastAPI
from app.api.routes import router as api_router
from app.database import get_database
from contextlib import asynccontextmanager

@asynccontextmanager
async def lifespan(app: FastAPI):
    # on startup
    app.mongodb_client = get_database()
    print("Connected to the MongoDB database!")
    yield
    # on shutdown
    app.mongodb_client.client.close()
    print("Disconnected from the MongoDB database!")

app = FastAPI(lifespan=lifespan)

@app.get("/")
def read_root():
    return {"message": "Welcome to the AI-Powered English Learning Platform!"}

app.include_router(api_router, prefix="/api")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
