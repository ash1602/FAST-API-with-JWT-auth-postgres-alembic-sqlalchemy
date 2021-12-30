from fastapi import  Depends, status, HTTPException, APIRouter
from sqlalchemy.orm import Session
from ..database import get_db
from ..schemas import UserLogin, Token
from .. models import User
from ..utils import verify
from ..oauth2 import create_access_token
from fastapi.security.oauth2 import OAuth2PasswordRequestForm
router = APIRouter(tags=["Authentication"])


@router.post("/login", response_model= Token)
def login(credantials:OAuth2PasswordRequestForm= Depends() ,db:Session = Depends(get_db)):
    #  OAuth2PasswordRequestForm only have username field which is in our case email
    user =  db.query(User).filter(User.email== credantials.username).first()
    if not user :
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"invalid credentials")
    if not verify(credantials.password , user.password):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"invalid credentials")
    
    # create token 
    access_token = create_access_token(data = {"user_id":user.id})
    # print(access_token)
    return {"access_token": access_token, "token_type":"bearer"}