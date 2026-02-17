from main import FastAPI , Response , status , HTTPException, Depends , APIRouter
from main import Session
from app.flight import models,schemas
from app.utils import get_db


def all_fly_details_service(db: Session):
        
        fly=db.query(models.flight_model).all()
        return fly

def add_new_fly_service(fly,db:Session):
         
    new_fly= models.prod(flight_num=fly.flight_num,
                         destinition=fly.destinition,
                         source=fly.source,
                         timing=fly.timing,
                         compny=fly.compny,
                         fual_cap=fly.fual_cap,
                         passanger_cap_busi=fly.passanger_cap_busi,
                         passanger_cap_eco=fly.passanger_cap_eco,
                         ticket_charges=fly.ticket_charges,
                         pilot_id=fly.pilot_id
                         )
    db.add(new_fly)
    db.commit()
    db.refresh(new_fly)
    return new_fly

def get_fly_via_id_service(flight_num,db:Session):
      
        id_prod= db.query(models.flight_model).filter(models.flight_model.flight_num==flight_num).first()
    
    
        if not id_prod :
                raise HTTPException(status_code= status.HTTP_404_NOT_FOUND ,
                            detail= f"flight with flight number :{flight_num} was not found ")

        return id_prod 

def remove_fly_service(flight_num,db):
        removed_flight = db.query(models.prod).filter(models.flight_model.flight_num==flight_num)
        if not removed_flight.first() :
                raise HTTPException(status_code= status.HTTP_204_NO_CONTENT ,
                            detail= f"flight with flight number : {flight_num} was removed ")
    
        removed_flight.delete(synchronize_session=False)
        db.commit()
    

        return removed_flight.first()

def update_fly_service(flight_num,fly,db):
        updated_flight= db.query(models.flight_model).filter(models.flight_model.flight_num==flight_num)


        prod=updated_flight.first()
        if not updated_flight :
                raise HTTPException(status_code= status.HTTP_200_OK ,
                            detail= f"update flight with flight number : {flight_num} is updated ")
    
        updated_flight.update(fly.dict(),synchronize_session=False)
        db.commit()
        return updated_flight.first()