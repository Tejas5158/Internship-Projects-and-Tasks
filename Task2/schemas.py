from pydantic import BaseModel

class BlogCreate(BaseModel):
    title: str
    content: str
    author: str