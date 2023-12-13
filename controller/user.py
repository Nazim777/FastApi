from hashPassword import passwordHash
from fastapi import HTTPException
import models


def user_create(request,db):
    new_user = models.User(name=request.name,email=request.email,password=passwordHash(request.password))
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return {
        'message':'user created successfully!',
        'data':new_user
    }

def get_single_user(id,db):
    user = db.query(models.User).filter(models.User.id==id).first()
    if not user:
        raise HTTPException(status_code=404, detail=f"user not found with the id of {id}")
    return user