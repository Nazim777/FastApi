from fastapi import HTTPException
from datetime import  timedelta
from hashPassword import verify_password
from jwt_token import create_access_token
import models



def login_user(request,db):
    user = db.query(models.User).filter(models.User.email==request.username).first()
    if not user:
         raise HTTPException(status_code=404, detail=f"user not found with the username of {request.username}")
    passwordCheck = verify_password(request.password,user.password)
    if not passwordCheck:
        raise HTTPException(status_code=404, detail="wrong password please try next time!")
    
    access_token_expires = timedelta(minutes=20)
    access_token = create_access_token(
        data={"sub": user.email}, expires_delta=access_token_expires
    )
    return {"access_token": access_token, "token_type": "bearer"}
    