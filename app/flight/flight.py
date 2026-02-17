from main import FastAPI , Response , status , HTTPException, Depends , APIRouter
from main import Session
from app.flight import models,schemas
from app.utils import get_db
from app.flight.service import all_fly_details_service,add_new_fly_service,get_fly_via_id_service,remove_fly_service,update_fly_service

router= APIRouter(
    prefix="/flight",
    tags= ['flights']
)

air=FastAPI

# getting flights details   
@router.get("/get_all")
def get_all(db:Session = Depends (get_db)):

    try:
        if not all_fly_details_service :
            raise print(f"account with username : {id} was not found ")
    except: 
        return all_fly_details_service(db)
    



# add new flights
@router.post("/add",status_code=status.HTTP_201_CREATED,response_model=schemas.fly_response)
def create_fly(fly:schemas.fly_request,db:Session = Depends (get_db)):
    
    return add_new_fly_service(fly,db)

   



# getting flights details via flight_number         
@router.get("/get/{flight_num}",response_model=schemas.fly_response)
def get_post(flight_num : int,db:Session = Depends (get_db)):

    return get_fly_via_id_service(flight_num,db)

   


# remove flights details        
@router.delete("/remove/{flight_num}")
def remove_flight(flight_num : int,db:Session = Depends (get_db)):

    return remove_fly_service(flight_num,db)

    


# updating flights details          
@router.put("/update/{flight_num}",response_model=schemas.fly_response)
def update_flight(flight_num : int , fly:schemas.fly_request,db:Session = Depends (get_db)):

    return update_fly_service(flight_num,fly,db)
     