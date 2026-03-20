from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database.db import SessionLocal
from schemas.user_schema import UserCreate, UserUpdate
from controllers import user_controller

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/users", status_code=201)
def create_user(user: UserCreate, db: Session = Depends(get_db)):
    return user_controller.create_user(db, user)

@router.get("/users")
def get_users(db: Session = Depends(get_db)):
    return user_controller.get_users(db)

@router.get("/users/{id}")
def get_user(id: int, db: Session = Depends(get_db)):
    user = user_controller.get_user(db, id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user

@router.put("/users/{id}")
def update_user(id: int, data: UserUpdate, db: Session = Depends(get_db)):
    user = user_controller.update_user(db, id, data)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user

@router.delete("/users/{id}")
def delete_user(id: int, db: Session = Depends(get_db)):
    user = user_controller.delete_user(db, id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return {"message": "User deleted"}