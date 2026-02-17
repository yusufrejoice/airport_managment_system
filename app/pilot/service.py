from main import FastAPI , Response , status , HTTPException, Depends, APIRouter
from main import Session
from app.pilot import models,schemas
from app.database import engine , SessionLocal
from app.utils import pwd_context
from app.utils import get_db


def get_all_pilot_service(db):
    
    pilots=db.query(models.pilot_model).all()
    return pilots


def add_new_pilot_service(pil,db):

    pilot_data = pil.dict()
    
    pilot_data["password"] = pwd_context.hash(pil.password)

 

    new_pilot = models.pilot_model(**pilot_data)

    db.add(new_pilot)
    db.commit()
    db.refresh(new_pilot)

    return new_pilot


def get_via_id_service(id,db):

    pilot_details = db.query(models.pilot_model).filter(models.pilot_model.id==id).first()
    
    
    if not pilot_details :
        raise HTTPException(status_code= status.HTTP_404_NOT_FOUND ,
                            detail= f"pilot with id : {id} was not found ")

    return pilot_details


def remove_pilot_service(id,db):

    deleted_pilot = db.query(models.pilot_model).filter(models.pilot_model.id==id)
    if not deleted_pilot.first() :
        raise HTTPException(status_code= status.HTTP_204_NO_CONTENT ,
                            detail= f"pilot with id : {id} was not exist ")
    
    deleted_pilot.delete(synchronize_session=False)
    db.commit()
    

    return deleted_pilot.first()


def update_pilot_service(id,new_details,db):

    updated_pilot= db.query(models.pilot_model).filter(models.pilot_model.id==id)

    pilot_data = new_details.dict()
    
    pilot_data["password"] = pwd_context.hash(new_details.password)

    
    updated_pilot = models.pilot_model(**pilot_data)

    db.add(updated_pilot)
    db.commit()
    db.refresh(updated_pilot)
    return updated_pilot
