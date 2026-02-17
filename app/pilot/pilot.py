from main import FastAPI , Response , status , HTTPException, Depends, APIRouter
from main import Session
from app.pilot import models,schemas
from app.database import engine , SessionLocal
from app.utils import pwd_context
from app.utils import get_db
from app.pilot.service import get_all_pilot_service,add_new_pilot_service,get_via_id_service,remove_pilot_service,update_pilot_service




router= APIRouter(
    prefix="/pilot",
    tags= ['pilots']
)

air = FastAPI()

models.Base.metadata.create_all(bind=engine)


# getting pilots details   
@router.get("/get_all")
def get_all_pilots(db:Session = Depends (get_db)):


    return get_all_pilot_service(db)



# pilots registretion 
@router.post("/add", status_code=status.HTTP_201_CREATED,
          response_model=schemas.pilot_response)
def add_pilot(pil: schemas.pilot_request, db: Session = Depends(get_db)):

    return add_new_pilot_service(pil,db)



# getting pilot details via id         
@router.get("/get/{id}",response_model=schemas.pilot_response)
def get_pilot(id : int,db:Session = Depends (get_db)):


    return get_via_id_service(id,db)




# removing pilot   
@router.delete("/remove/{id}")
def remove_user(id: int,db:Session = Depends (get_db)):

    return remove_pilot_service(id,db)




# updating pilots details     
@router.put("/update/{id}")
def update_pilot(id: int , new_details:schemas.pilot_request,db:Session = Depends (get_db)):

    return update_pilot_service(id,new_details,db)
    