from fastapi import HTTPException
import models
def get_all_blog(db):
    blogs = db.query(models.Blog).all()
    return blogs

def get_single_blog(id,db):
   blog= db.query(models.Blog).filter(models.Blog.id==id).first()
   if not  blog:
        raise HTTPException(status_code=404, detail=f"blog not found with the id of {id}")
   return blog

def delete_blog(id,db):
    blog = db.query(models.Blog).filter(models.Blog.id==id)
    if not blog.first():
        raise HTTPException(status_code=404, detail=f"blog not found with the id of {id}")
    blog.delete(synchronize_session=False)
    db.commit()
    return {"message":f"blog deleted successfully!"}

def update_blog(request,id,db):
    blog = db.query(models.Blog).filter(models.Blog.id==id)
    if not blog.first():
        raise HTTPException(status_code=404, detail=f"blog not found with the id of {id}")
    blog.update({"title":request.title,"description":request.description,"isPublished":request.isPublished},synchronize_session=False)
    db.commit()
    return {"messages":"Blog updated successfully!"}

def create_blog(request,db,current_user_email):
    blog_author = db.query(models.User).filter(models.User.email==current_user_email).first()
    new_blog = models.Blog(title=request.title,description=request.description,isPublished=request.isPublished,user_id=blog_author.id)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return {
        'message':'blog created successfully!',
        'data':new_blog
    }