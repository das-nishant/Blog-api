from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.db.session import SessionLocal
from . import schema, service

router = APIRouter()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/signup", response_model=schema.UserResponse)
def signup(
    user: schema.UserCreate,
    db: Session = Depends(get_db)
):
    return service.create_user(
        db,
        user.username,
        user.email,
        user.password
    )


@router.post("/login", response_model=schema.UserResponse)
def login(
    credentials: schema.UserLogin,
    db: Session = Depends(get_db)
):
    user = service.authenticate_user(
        db,
        credentials.email,
        credentials.password
    )

    if not user:
        raise HTTPException(status_code=401, detail="Invalid email or password")

    return user