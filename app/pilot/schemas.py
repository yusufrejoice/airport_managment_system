from pydantic import BaseModel,EmailStr
from datetime import date, datetime 



# schema for pilots
class pilot_request(BaseModel):
    name : str
    email: EmailStr
    password: str
    phone : int
    


class pilot_response(BaseModel):
    name : str
    email: EmailStr
    phone : int