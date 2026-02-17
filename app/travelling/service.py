from main import FastAPI , Response , status , HTTPException, Depends, APIRouter
from main import Session
from app.travelling import models,schemas
from app.database import engine , SessionLocal
from app.utils import pwd_context
from app.utils import get_db


def get_all_passanger_details_service(db):

    passanger=db.query(models.travelling_model).all()
    return passanger


def add_new_passanger_service(passanger,db):

    new_passanger= models.travelling_model(id=passanger.id,
                                           date=passanger.date,
                                           source=passanger.source,
                                           destinition=passanger.destinition,
                                           passenger_details=passanger.passenger_details,
                                           ticket_amount=passanger.ticket_amount,
                                           additional_req=passanger.additional_req,
                                           total_amount=passanger.ticket_amount + passanger.additional_req,
                                           payment_type=passanger.payment_type)
    db.add(new_passanger)
    db.commit()
    db.refresh(new_passanger)
    return new_passanger


def get_passanger_via_id_service(id,db):

    passanger = db.query(models.travelling_model).filter(models.travelling_model.id==id).first()
    
    
    if not passanger :
        raise HTTPException(status_code= status.HTTP_404_NOT_FOUND ,
                            detail= f"pasanger with id : {id} was not found ")

    return passanger


def remove_passanger_service(id,db):

    deleted_passanger = db.query(models.travelling_model).filter(models.travelling_model.id==id)
    if not deleted_passanger.first() :
        raise HTTPException(status_code= status.HTTP_204_NO_CONTENT ,
                            detail= f"passanger with id : {id} was not found ")
    
    deleted_passanger.delete(synchronize_session=False)
    db.commit()
    

    return deleted_passanger.first()

def update_passanger_service(id,passanger,db):

    updated_passanger = db.query(models.travelling_model).filter(
        models.travelling_model.id == id
    ).first()

    if not updated_passanger:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"passenger with id {id} not found"
        )

    
    updated_passanger.date = passanger.date
    updated_passanger.source = passanger.source
    updated_passanger.destinition = passanger.destinition
    updated_passanger.passenger_details = passanger.passenger_details
    updated_passanger.ticket_amount = passanger.ticket_amount
    updated_passanger.additional_req = passanger.additional_req
    updated_passanger.total_amount = passanger.total_amount
    updated_passanger.payment_type = passanger.payment_type

    db.commit()
    db.refresh(updated_passanger)

    return updated_passanger
