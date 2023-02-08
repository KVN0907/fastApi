from .database import Base
from sqlalchemy import Column, Integer, String


class DbUser(Base):
  __tablename__ = 'ctteam'
  id = Column(Integer, primary_key=True, index=True)
  username = Column(String)
  email = Column(String)
  password = Column(String)
  designation = Column(String)