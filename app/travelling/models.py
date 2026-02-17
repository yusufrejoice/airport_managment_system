from sqlalchemy import Column, Integer, String, Boolean ,Date ,JSON ,Float
from sqlalchemy.sql.expression import null
from app.database import Base
import uuid
from sqlalchemy.dialects.postgresql import UUID


class travelling_model (Base):
    __tablename__ = "travellings"

    
    id = Column(Integer , primary_key=True,nullable=False)
    date = Column(Date, nullable=False)
    source = Column(String,nullable=False)
    destinition = Column(String,nullable=False)
    passenger_details = Column(String, nullable=False)
    ticket_amount = Column(Float, nullable=False)
    additional_req = Column(Float , nullable=False)
    total_amount = Column(Float, nullable=False )
    payment_type = Column(String , nullable=False)