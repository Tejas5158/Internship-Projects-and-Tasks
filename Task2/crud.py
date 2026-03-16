from sqlalchemy.orm import Session
import models, schemas

# Create blog
def create_blog(db: Session, blog: schemas.BlogCreate):
    new_blog = models.Blog(
        title=blog.title,
        content=blog.content,
        author=blog.author
    )
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog


# Get all blogs
def get_blogs(db: Session):
    return db.query(models.Blog).all()


# Get blog by id
def get_blog(db: Session, blog_id: int):
    return db.query(models.Blog).filter(models.Blog.id == blog_id).first()


# Update blog
def update_blog(db: Session, blog_id: int, blog: schemas.BlogCreate):
    existing_blog = db.query(models.Blog).filter(models.Blog.id == blog_id).first()
    
    if existing_blog:
        existing_blog.title = blog.title
        existing_blog.content = blog.content
        db.commit()
        db.refresh(existing_blog)

    return existing_blog


# Delete blog
def delete_blog(db: Session, blog_id: int):
    blog = db.query(models.Blog).filter(models.Blog.id == blog_id).first()

    if blog:
        db.delete(blog)
        db.commit()

    return blog