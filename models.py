from sqlalchemy import Column, Integer, String, Boolean
from database import Base

# Hall of Fame Class
class HallOfFame(Base):
    __tablename__ = "Hall_Of_Famers"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    year_inducted = Column(Integer)
    age = Column(Integer)
    years_active = Column(Integer)
    still_active = Column(Boolean)
    total_titles_won = Column(Integer)
    
    
# Suerstars Class
class Superstars(Base):
    __tablename__ = "Superstars"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    debut_year = Column(Integer)
    age = Column(Integer)
    is_currently_active = Column(Boolean)
    total_titles_won = Column(Integer)
    current_brand = Column(String)
    

# Next Gen Class
class Next_Generation(Base):
    __tablename__ = "Next_Generation"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    debut_year = Column(Integer)
    age = Column(Integer)
    total_titles_won = Column(Integer)
    current_brand = Column(String)