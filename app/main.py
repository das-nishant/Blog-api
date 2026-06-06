from fastapi import FastAPI
from app.db.base import Base
from app.db.session import engine
from app.modules.post.route import router as post_router
from app.modules.user.route import router as user_router
app = FastAPI()

app.include_router(user_router, prefix="/users", tags=["Users"])
app.include_router(post_router, prefix="/posts", tags=["Posts"])

Base.metadata.create_all(bind=engine)

@app.get("/")
def root():
    return {"message": "Blog API running 🚀"}