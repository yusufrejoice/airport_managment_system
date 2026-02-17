from main import FastAPI , Response , status , HTTPException, Depends, APIRouter
from main import Session
from app.travelling import models,schemas
from app.database import engine , SessionLocal
from app.utils import pwd_context
from app.utils import get_db
from app.travelling.service import get_all_passanger_details_service,add_new_passanger_service,get_passanger_via_id_service,remove_passanger_service,update_passanger_service

router= APIRouter(
    prefix="/travelling",
    tags= ['travellings']
)

air = FastAPI()

models.Base.metadata.create_all(bind=engine)


# getting passanger details   
@router.get("/get_all")
def get_all_passanger(db:Session = Depends (get_db)):

    return get_all_passanger_details_service





# new passanger 
@router.post("/add", status_code=status.HTTP_201_CREATED,
          response_model=schemas.travellings_response)
def create_passanger(passanger: schemas.travellings_request, db: Session = Depends(get_db)):
    
    return add_new_passanger_service(passanger,db)
   
    



# getting user passanger via id         
@router.get("/get/{id}",response_model=schemas.travellings_response)
def get_passanger(id : int,db:Session = Depends (get_db)):

    return get_passanger_via_id_service(id,db)

    



# removing passenger      
@router.delete("/remove/{id}")
def remove_passanger(id: int,db:Session = Depends (get_db)):

    return remove_passanger_service(id,db)
    




@router.put("/update/{id}", response_model=schemas.travellings_response)
def update_passanger(
    id: int,
    passanger: schemas.travellings_request,
    db: Session = Depends(get_db)
):
    
    return update_passanger_service(id,passanger,db)
    