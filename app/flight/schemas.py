from pydantic import BaseModel,EmailStr
from datetime import date, datetime 



# schema for flights 
class fly_request(BaseModel):
    flight_num : int
    destinition: str
    source : str
    timing : str
    compny : str
    fual_cap : str
    passanger_cap_busi : int
    passanger_cap_eco : int
    ticket_charges : int
    pilot_id : str



class fly_response(BaseModel):
    flight_num : int
    destinition: str
    source : str
    timing : str
    compny : str
    fual_cap : str
    passanger_cap_busi : int
    passanger_cap_eco : int
    ticket_charges : int
    pilot_id : str

    class confing:
        orm_mode=True