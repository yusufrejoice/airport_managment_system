from fastapi import FastAPI , Response , status , HTTPException, Depends, APIRouter
from fastapi.params import Body
from pydantic import BaseModel
from random import randrange
from uuid import uuid4
import psycopg2
from psycopg2.extras import RealDictCursor
import time 
from sqlalchemy.orm import Session
from app import utils
from app.database import engine , SessionLocal 
from app.utils import pwd_context
from app.flight import flight
from app.pilot import pilot
from app.user import user
from app.travelling import travelling
from app.auth import auth
from app.utils import get_db
from app.flight import models
from app.pilot import models
from app.travelling import models
from app.user import models
#



 


air = FastAPI()
models.Base.metadata.create_all(bind=engine)
air.include_router(flight.router)
air.include_router(pilot.router)
air.include_router(user.router)
air.include_router(travelling.router)
air.include_router(utils.router)
air.include_router(auth.router)









    

    
