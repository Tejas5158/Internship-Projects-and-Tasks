from sqlalchemy import Column, Integer, String, Text, TIMESTAMP
from database import Base
from sqlalchemy.sql import func

class Blog(Base):
    __tablename__ = "blogs"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(255))
    content = Column(Text)
    author = Column(String(100))
    created_at = Column(TIMESTAMP, server_default=func.now())
    