from sqlalchemy.orm import Session
from .model import User


def create_user(
    db: Session,
    username: str,
    email: str,
    password: str
):
    user = User(
        username=username,
        email=email,
        password=password
    )

    db.add(user)
    db.commit()
    db.refresh(user)

    return user


def get_user_by_email(db: Session, email: str):
    return db.query(User).filter(User.email == email).first()


def authenticate_user(
    db: Session,
    email: str,
    password: str
):
    user = get_user_by_email(db, email)

    if not user or user.password != password:
        return None

    return user