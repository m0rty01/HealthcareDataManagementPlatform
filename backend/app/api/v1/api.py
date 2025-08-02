from fastapi import APIRouter
from app.api.v1.endpoints import auth, users, health_records

api_router = APIRouter()

api_router.include_router(auth.router, prefix="/auth", tags=["authentication"])
api_router.include_router(users.router, prefix="/users", tags=["users"])
api_router.include_router(health_records.router, prefix="/health-records", tags=["health records"]) 