# collect.py

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()  # This is the base class for all models

class Member(Base):
    __tablename__ = "members"  # Table name in the database

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    phone = Column(String)
    payment_status = Column(Integer)
