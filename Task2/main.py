from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
import models, schemas, crud
from database import engine, SessionLocal, Base

app = FastAPI()

Base.metadata.create_all(bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post("/blogs")
def create_blog(blog: schemas.BlogCreate, db: Session = Depends(get_db)):
    return crud.create_blog(db, blog)


@app.get("/blogs")
def get_blogs(db: Session = Depends(get_db)):
    return crud.get_blogs(db)


@app.get("/blogs/{blog_id}")
def get_blog(blog_id: int, db: Session = Depends(get_db)):
    blog = crud.get_blog(db, blog_id)
    if not blog:
        raise HTTPException(status_code=404, detail="Blog not found")
    return blog


@app.put("/blogs/{blog_id}")
def update_blog(blog_id: int, blog: schemas.BlogUpdate, db: Session = Depends(get_db)):
    return crud.update_blog(db, blog_id, blog)


@app.delete("/blogs/{blog_id}")
def delete_blog(blog_id: int, db: Session = Depends(get_db)):
    return crud.delete_blog(db, blog_id)