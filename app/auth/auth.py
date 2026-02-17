from app import utils
from main import FastAPI , Response , status , HTTPException, Depends, APIRouter
from sqlalchemy.orm import Session 
from app.auth import schemas 
from app.utils import pwd_context
from app.utils import get_db
from app import oauth2
from app.auth.service import login_user_service, login_pilot_service 


router= APIRouter(
    prefix="/login",
    tags= ['authentication']
)


@router.post('/user') 
def login_user(user_credentials:schemas.Userlogin , db:Session = Depends (get_db)) :
   
   return login_user_service(user_credentials, db)


@router.post('/pilot') 
def login_pilot(pilot_credentials:schemas.Pilotlogin , db:Session = Depends (get_db)) :
   
   return login_pilot_service(pilot_credentials, db)
    