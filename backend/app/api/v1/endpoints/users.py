from typing import List
from fastapi import APIRouter, Depends, HTTPException
from app.models.user import User, UserCreate, UserUpdate
from app.db.mongodb import get_database

router = APIRouter()

@router.get("/", response_model=List[User])
async def get_users(db = Depends(get_database)):
    """
    Retrieve all users.
    """
    users = await db.users.find().to_list(1000)
    return users

@router.get("/{user_id}", response_model=User)
async def get_user(user_id: str, db = Depends(get_database)):
    """
    Get a specific user by ID.
    """
    user = await db.users.find_one({"_id": user_id})
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user

@router.put("/{user_id}", response_model=User)
async def update_user(user_id: str, user_update: UserUpdate, db = Depends(get_database)):
    """
    Update a user.
    """
    user = await db.users.find_one({"_id": user_id})
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    
    update_data = user_update.dict(exclude_unset=True)
    if update_data:
        await db.users.update_one(
            {"_id": user_id},
            {"$set": update_data}
        )
    
    return await db.users.find_one({"_id": user_id})