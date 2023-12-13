from fastapi import APIRouter
from fastapi import  Depends,status
from schemas import User,PresentUser
from sqlalchemy.orm import Session
from database import get_db
from controller import user as user_controller
router = APIRouter(
    prefix="/user",
    tags=["Users"]
)


@router.post('/',status_code=status.HTTP_201_CREATED)
def create_user(request:User,db: Session = Depends(get_db)):
    return user_controller.user_create(request,db)


@router.get('/{id}',response_model=PresentUser)
def single_user(id,db: Session = Depends(get_db)):
    return user_controller.get_single_user(id,db)