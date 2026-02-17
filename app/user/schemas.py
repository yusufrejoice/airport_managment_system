from pydantic import BaseModel,EmailStr
from datetime import date, datetime 

# schema for users
class user_request(BaseModel):
    name : str
    email : EmailStr
    password: str
    date_of_birth : date
    passport_num : int
    year : int
    is_active : bool
    is_block : bool
    city : str
    state : str
    contry : str
    


class users_response(BaseModel):
    name : str
    email: EmailStr
    date_of_birth : date
    passport_num : int
    year : int
    city : str
    state : str
    contry : str
    

    class confing:
        orm_mode=True
