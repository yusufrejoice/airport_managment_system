from pydantic import BaseModel,EmailStr
from datetime import date, datetime 


# schema for travellings
class travellings_request(BaseModel):
    id : int
    date : date
    source : str
    destinition : str
    passenger_details : str
    ticket_amount : float
    additional_req : float
    total_amount : float
    payment_type : str


class travellings_response(BaseModel):
    date : date
    source : str
    destinition : str
    passenger_details : str
    ticket_amount : float
    additional_req : float
    total_amount : float
    payment_type : str
    
    

    class confing:
        orm_mode=True