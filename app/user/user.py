from main import FastAPI , Response , status , HTTPException, Depends, APIRouter
from main import Session
from app.user import models,schemas
from app.database import engine , SessionLocal
from app.utils import pwd_context
from app.utils import get_db
from app.user.service import get_all_users_details_service,get_all_user_via_id_service,add_new_user_service,remove_user_sevice,update_user_service


router= APIRouter(
    prefix="/user",
    tags= ['users']
)

air = FastAPI()

models.Base.metadata.create_all(bind=engine)


# getting users details   
@router.get("/get_all")
def get_all_user(db:Session = Depends (get_db)):
    

    return get_all_users_details_service(db) 



# user registretion 
@router.post("/add", status_code=status.HTTP_201_CREATED,
          response_model=schemas.users_response)
def create_user(user: schemas.user_request, db: Session = Depends(get_db)):


    return add_new_user_service(user,db)

# getting user details via id         
@router.get("/get/{id}",response_model=schemas.users_response)
def get_user(id : str,db:Session = Depends (get_db)):

    
    return get_all_user_via_id_service(id,db)




# removing user via id         
@router.delete("/remove/{id}")
def remove_user(id: str,db:Session = Depends (get_db)):
    

    return remove_user_sevice(id,db)


# updating user details via id         
@router.put("/update/{id}")
def update_user(id: str , new_details:schemas.user_request,db:Session = Depends (get_db)):
    
    return update_user_service(id,new_details,db)

    