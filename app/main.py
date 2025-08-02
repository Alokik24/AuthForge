from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.core.security import get_password_hash, verify_password, create_access_token, verify_token

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

@app.get("/test-auth")
async def test_auth():
    password = "my_password"
    hashed_password = get_password_hash(password)
    assert verify_password(password, hashed_password)

    token = create_access_token({"sub": "test_user_id"})
    user_id = verify_token(token)

    return {
        "hashed_password": hashed_password,
        "validation": verify_password(password, hashed_password),
        "token": token,
        "decoded_user_id": user_id
    }