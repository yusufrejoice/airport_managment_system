from pydantic import BaseModel,EmailStr
from datetime import date, datetime 

class Userlogin(BaseModel):
    email : EmailStr
    password : str


class Pilotlogin(BaseModel):
    email : EmailStr
    password : str