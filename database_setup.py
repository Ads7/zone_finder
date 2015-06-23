import os
import sys
from sqlalchemy import Column, Float, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
 
Base = declarative_base()

class Area(Base):
    __tablename__ = 'area'
   
    subzone_id = Column(Integer, primary=True)
    subzone_name = Column(String(250), nullable=False)
    latitude = Column(Float, nullable=False)
    longitude = Column(Float, nullable=False)



engine = create_engine('sqlite:///subzonedata.db')
Base.metadata.create_all(engine)