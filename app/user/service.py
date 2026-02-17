from main import FastAPI , Response , status , HTTPException, Depends, APIRouter
from main import Session
from app.user import models,schemas
from app.database import engine , SessionLocal
from app.utils import pwd_context
from app.utils import get_db



def get_all_users_details_service(db):

    users=db.query(models.user_model).all()
    return users


def add_new_user_service(user,db):

    user_data = user.dict()
    
    user_data["password"] = pwd_context.hash(user.password)

    

    new_users = models.user_model(**user_data)

    db.add(new_users)
    db.commit()
    db.refresh(new_users)

    return new_users


def get_all_user_via_id_service(id,db):

    user_name = db.query(models.user_model).filter(models.user_model.id==id).first()
    
    
    if not user_name :
        raise HTTPException(status_code= status.HTTP_404_NOT_FOUND ,
                            detail= f"account with username : {id} was not found ")

    return user_name


def remove_user_sevice(id,db):

    deleted_user = db.query(models.user_model).filter(models.user_model.id==id)
    if not deleted_user.first() :
        raise HTTPException(status_code= status.HTTP_204_NO_CONTENT ,
                            detail= f"product with id : {id} was removed ")
    
    deleted_user.delete(synchronize_session=False)
    db.commit()
    

    return deleted_user.first()


def update_user_service(id,new_details,db):

    updated_user= db.query(models.user_model).filter(models.user_model.id==id)

    user_data = new_details.dict()
    
    user_data["password"] = pwd_context.hash(new_details.password)



    updated_user = models.user_model(**user_data)

    db.add(updated_user)
    db.commit()
    db.refresh(updated_user)
    return updated_user