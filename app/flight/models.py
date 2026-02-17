from sqlalchemy import Column, Integer, String, Boolean ,Date ,JSON ,Float
from sqlalchemy.sql.expression import null
from app.database import Base
import uuid
from sqlalchemy.dialects.postgresql import UUID



class flight_model (Base):
    __tablename__ = "flights"
    flight_num = Column(Integer,primary_key=True,nullable=False)
    destinition = Column(String,nullable=False)
    source = Column(String,nullable=False)
    timing = Column(String, nullable=False)
    compny = Column(String,nullable=False)
    fual_cap = Column(String,nullable=False)
    passanger_cap_busi = Column(Integer , nullable=False)
    passanger_cap_eco = Column(Integer , nullable=False)
    ticket_charges = Column(Integer , nullable=False)
    pilot_id = Column(Integer , nullable=False)