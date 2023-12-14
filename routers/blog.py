from fastapi import APIRouter
from fastapi import Depends,status
from schemas import User,Blog,PresentBlogs
from sqlalchemy.orm import Session
from database import get_db
from controller import blog as blog_controller
from oauth2 import get_current_user
router = APIRouter(
    prefix='/blog',
    tags=["Blogs"]
)

@router.post('/',status_code=status.HTTP_201_CREATED)
def create_blog(request:Blog,db: Session = Depends(get_db),current_user: User = Depends(get_current_user)):
    return blog_controller.create_blog(request,db,current_user.email)
    # return {"message": "This is a protected route", "user_email": current_user.email}


@router.get('/',status_code=status.HTTP_200_OK,response_model=list[PresentBlogs])
def all_blogs(db:Session=Depends(get_db),current_user: User = Depends(get_current_user)):
    return blog_controller.get_all_blog(db)


@router.get('/{id}',status_code=status.HTTP_200_OK,response_model=PresentBlogs)
def single_blog(id,db:Session=Depends(get_db),current_user: User = Depends(get_current_user)):
    return blog_controller.get_single_blog(id,db)

@router.delete('/{id}',status_code=status.HTTP_200_OK)
def delete_blog(id,db:Session=Depends(get_db),current_user: User = Depends(get_current_user)):
    return blog_controller.delete_blog(id,db)


@router.put('/{id}', status_code=status.HTTP_202_ACCEPTED)
def update_blog(request:Blog,id,db:Session=Depends(get_db),current_user: User = Depends(get_current_user)):
    return blog_controller.update_blog(request,id,db)