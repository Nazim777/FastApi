from fastapi import APIRouter
from fastapi import  Depends,status
from schemas import Login
from sqlalchemy.orm import Session
from database import get_db
from controller import auth as auth_controller
from fastapi.security import OAuth2PasswordRequestForm
router = APIRouter(
    tags=["Login"]
)


@router.post('/login',status_code=status.HTTP_202_ACCEPTED)
def login_user(request:OAuth2PasswordRequestForm = Depends(),db: Session = Depends(get_db)):
   return auth_controller.login_user(request,db)
