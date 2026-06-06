from typing import List

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


@router.post("/", response_model=schema.PostResponse)
def create_post(
    post: schema.PostCreate,
    db: Session = Depends(get_db)
):
    return service.create_post(db, post.title, post.content)


@router.get("/", response_model=List[schema.PostResponse])
def list_posts(db: Session = Depends(get_db)):
    return service.get_posts(db)


@router.get("/{post_id}", response_model=schema.PostResponse)
def get_post(post_id: int, db: Session = Depends(get_db)):
    db_post = service.get_post(db, post_id)
    if not db_post:
        raise HTTPException(status_code=404, detail="Post not found")
    return db_post


@router.put("/{post_id}", response_model=schema.PostResponse)
def update_post(
    post_id: int,
    post: schema.PostUpdate,
    db: Session = Depends(get_db)
):
    db_post = service.update_post(db, post_id, post.title, post.content)
    if not db_post:
        raise HTTPException(status_code=404, detail="Post not found")
    return db_post


@router.delete("/{post_id}")
def delete_post(post_id: int, db: Session = Depends(get_db)):
    if not service.delete_post(db, post_id):
        raise HTTPException(status_code=404, detail="Post not found")
    return {"message": "Post deleted"}
