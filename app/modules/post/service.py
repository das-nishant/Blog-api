from sqlalchemy.orm import Session
from . import model


def create_post(db: Session, title: str, content: str):
    post = model.Post(title=title, content=content)
    db.add(post)
    db.commit()
    db.refresh(post)
    return post


def get_posts(db: Session):
    return db.query(model.Post).all()


def get_post(db: Session, post_id: int):
    return db.query(model.Post).filter(model.Post.id == post_id).first()


def update_post(db: Session, post_id: int, title: str, content: str):
    post = get_post(db, post_id)
    if not post:
        return None
    post.title = title
    post.content = content
    db.commit()
    db.refresh(post)
    return post


def delete_post(db: Session, post_id: int):
    post = get_post(db, post_id)
    if not post:
        return False
    db.delete(post)
    db.commit()
    return True
