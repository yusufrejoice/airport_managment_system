from app import utils
from main import FastAPI , Response , status , HTTPException, Depends, APIRouter
from sqlalchemy.orm import Session 
from app.auth import models,schemas 
from app.utils import pwd_context
from app.utils import get_db
from app import oauth2 



def login_user_service(user_credentials, db: Session):
        
        user = db.query(models.user_model).filter(models.user_model.email == user_credentials.email).first()
        if not user :
            raise HTTPException(status_code= status.HTTP_404_NOT_FOUND , detail=f"invalid credentials" )
    
        if not utils.verify(user_credentials.password,user.password):
            raise HTTPException(
                status_code= status.HTTP_404_NOT_FOUND , 
                detail=f"invalid credentials"
                )
    
        access_token = oauth2.create_access_token(data={"user_id": str(user.id)})

        return {"access token" : access_token , "token type ": "bearer"}


def login_pilot_service(pilot_credentials, db: Session):
     
        pilot = db.query(models.pilot_model).filter(models.pilot_model.email == pilot_credentials.email).first()

        if not pilot :
            raise HTTPException(status_code= status.HTTP_404_NOT_FOUND , detail=f"invalid email or password" )

        if not utils.verify(pilot_credentials.password,pilot.password):
            raise HTTPException(
                status_code= status.HTTP_404_NOT_FOUND , 
                detail=f"invalid credentials"
                )
    
        access_token = oauth2.create_access_token(data={"pilot_id": str(pilot.id)})

        return {"access token" : access_token , "token type ": "bearer"}
