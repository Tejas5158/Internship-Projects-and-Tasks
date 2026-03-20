from fastapi import APIRouter
from schema import UserCreate
import controller

router = APIRouter()

@router.post("/users")
def create_user(user: UserCreate):
    return controller.create_user(user)

@router.get("/users")
def get_users():
    return controller.get_users()