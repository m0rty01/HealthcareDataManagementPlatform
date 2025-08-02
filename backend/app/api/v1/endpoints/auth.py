from datetime import datetime, timedelta
from typing import Any
from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from pydantic import ValidationError
from app.core.security import create_access_token, verify_password, get_password_hash
from app.core.config import settings
from app.models.user import User, UserCreate
from app.db.mongodb import get_database

router = APIRouter()

@router.post("/login")
async def login(
    form_data: OAuth2PasswordRequestForm = Depends(),
    db = Depends(get_database)
) -> Any:
    """
    OAuth2 compatible token login, get an access token for future requests
    """
    user = await db.users.find_one({"email": form_data.username})
    if not user or not verify_password(form_data.password, user["hashed_password"]):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect email or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    
    access_token_expires = timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
    return {
        "access_token": create_access_token(
            data={"sub": str(user["_id"])}, expires_delta=access_token_expires
        ),
        "token_type": "bearer",
    }

@router.post("/register", response_model=User)
async def register(
    user_in: UserCreate,
    db = Depends(get_database)
) -> Any:
    """
    Register new user
    """
    try:
        # Log incoming data
        print(f"Received raw data: {user_in}")
        print(f"Raw request data type: {type(user_in)}")
        print(f"Raw request data dict: {user_in.__dict__ if hasattr(user_in, '__dict__') else None}")
        
        # Check if email already exists
        user = await db.users.find_one({"email": user_in.email})
        if user:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Email already registered",
            )
        
        # Create user data
        try:
            user_data = user_in.model_dump()  # Use model_dump() instead of dict()
            print(f"User data after model_dump: {user_data}")
        except Exception as e:
            print(f"Error dumping model: {e}")
            print(f"User data type: {type(user_in)}")
            print(f"User data dict: {user_in.__dict__ if hasattr(user_in, '__dict__') else None}")
            print(f"Model dump error: {str(e)}")
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=f"Invalid user data: {str(e)}"
            )
        
        try:
            hashed_password = get_password_hash(user_data.pop("password"))
            user_data.update({
                "hashed_password": hashed_password,
                "is_active": True,
                "created_at": datetime.utcnow(),
                "blockchain_address": None  # Will be set when user connects wallet
            })
        except Exception as e:
            print(f"Error processing user data: {e}")
            print(f"User data before processing: {user_data}")
            print(f"Processing error: {str(e)}")
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=f"Error processing user data: {str(e)}"
            )
        
        # Log user data before insertion
        print(f"Inserting user data: {user_data}")
        
        try:
            result = await db.users.insert_one(user_data)
            user_data["_id"] = str(result.inserted_id)
            return User(**user_data)
        except Exception as e:
            print(f"Error inserting user: {e}")
            print(f"User data for insertion: {user_data}")
            print(f"Insertion error: {str(e)}")
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail=f"Error inserting user: {str(e)}"
            )
    except ValidationError as e:
        print(f"Validation error: {e}")
        print(f"Validation error details: {e.errors()}")
        print(f"Raw validation error: {str(e)}")
        error_details = []
        for error in e.errors():
            error_details.append({
                "field": error["loc"][0] if error["loc"] else "unknown",
                "message": error["msg"]
            })
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail={"errors": error_details}
        )
    except HTTPException as e:
        raise e
    except Exception as e:
        print(f"Unexpected error: {e}")
        print(f"Error type: {type(e)}")
        print(f"Error args: {e.args}")
        print(f"Full error: {str(e)}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Unexpected error: {str(e)}"
        ) 