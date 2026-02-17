from sqlalchemy import Column, Integer, String, Boolean ,Date ,JSON ,Float
from sqlalchemy.sql.expression import null
from app.database import Base
import uuid
from sqlalchemy.dialects.postgresql import UUID


class pilot_model (Base):
    __tablename__ = "pilots"

    id = Column(UUID(as_uuid=True), primary_key=True ,default=uuid.uuid4)
    name = Column(String , nullable=False)
    email = Column(String , unique =True ,nullable= False )
    password= Column(String,nullable=False)
    phone = Column(Integer , nullable=False)