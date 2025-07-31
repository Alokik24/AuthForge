from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(
    title="AuthForge",
    description="An authentication microservice for your applications",
    version="1.0.0"
)

# Middleware to allow frontend calls
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], # TODO - Change to specific origins in prduction
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Health route
@app.get("/")
async def root():
    return {"message": "AuthForge API is running!"}

@app.get("/health")
async def health_check():
    return {
        "status": "healthy",
        "version": "1.0.0",
        "service": "AuthForge"
    }