from sqlalchemy.orm import declarative_base

Base = declarative_base()

# Import models
from app.modules.user.model import User
from app.modules.post.model import Post