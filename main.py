from database import SessionLocal, Base, engine
from models import HallOfFame, Superstars, Next_Generation
from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional

app = FastAPI()
Base.metadata.create_all(bind=engine)

# CRUD Operations for Hall of Fame
class Create_Hall_of_Famer(BaseModel):
    name: str
    year_inducted: int  
    age: int
    years_active: int
    still_active: bool
    total_titles_won: int

class Update_Hall_of_Famer(BaseModel):
    id: int
    name: Optional[str] = None
    year_inducted: Optional[int] = None
    age: Optional[int] = None
    years_active: Optional[int] = None
    still_active: Optional[bool] = None
    total_titles_won: Optional[int] = None

class Delete_Hall_of_Famer(BaseModel):
    id: int


# CRUD Operations for Superstars
class Create_Superstar(BaseModel):
    name: str
    debut_year: int
    age: int
    is_currently_active: bool
    total_titles_won: int
    current_brand: str
    
class Update_Superstar(BaseModel):
    id: int
    name: Optional[str] = None
    debut_year: Optional[int] = None
    age: Optional[int] = None
    is_currently_active: Optional[bool] = None
    total_titles_won: Optional[int] = None
    current_brand: Optional[str] = None
    
class Delete_Superstar(BaseModel):
    id: int
    
# CRUD Operations for Next Generation
class Create_Next_Generation(BaseModel):
    name: str
    debut_year: int
    age: int
    total_titles_won: int
    current_brand: str
    
class Update_Next_Generation(BaseModel):
    id: int
    name: Optional[str] = None
    debut_year: Optional[int] = None
    age: Optional[int] = None
    total_titles_won: Optional[int] = None
    current_brand: Optional[str] = None
    
class Delete_Next_Generation(BaseModel):
    id: int
    

# API Endpoints for Hall of Fame
@app.post("/add_to_HOF/")
def add_to_HOF(ss: Create_Hall_of_Famer):
    HOF = SessionLocal()
    
    HOF_entry = HallOfFame(
        name = ss.name,
        year_inducted = ss.year_inducted,
        age = ss.age,
        years_active = ss.years_active,
        still_active = ss.still_active,
        total_titles_won = ss.total_titles_won
    )
    
    HOF.add(HOF_entry)
    HOF.commit()
    HOF.refresh(HOF_entry)
    HOF.close()
    
    return {"message": f"{ss.name} has been added to the Hall of Fame!"}


@app.get("/search_in_HOF/{id}") 
def search_in_HOF(id: int):
    HOF = SessionLocal()
    HOF_search = HOF.query(HallOfFame).filter(HallOfFame.id == id).first()
    
    if not HOF_search:
        HOF.close()
        return {"message": "No Hall of Famer found with the provided ID."}
    
    return {
        "id": HOF_search.id,
        "name": HOF_search.name,
        "year_inducted": HOF_search.year_inducted,
        "age": HOF_search.age,
        "years_active": HOF_search.years_active,
        "still_active": HOF_search.still_active,
        "total_titles_won": HOF_search.total_titles_won
    }
    
@app.post("/update_HOF")
def update_HOF(ss: Update_Hall_of_Famer):
    HOF = SessionLocal()
    HOF_update = HOF.query(HallOfFame).filter(HallOfFame.id == ss.id).first()
    
    if not HOF_update:
        HOF.close()
        return {"message": "No Hall of Famer found with the provided ID."}
    
    if ss.name is not None:
        HOF_update.name = ss.name
    if ss.year_inducted is not None:
        HOF_update.year_inducted = ss.year_inducted
    if ss.age is not None:
        HOF_update.age = ss.age
    if ss.years_active is not None:
        HOF_update.years_active = ss.years_active
    if ss.still_active is not None:
        HOF_update.still_active = ss.still_active
    if ss.total_titles_won is not None:
        HOF_update.total_titles_won = ss.total_titles_won
    
    HOF.commit()
    HOF.refresh(HOF_update)
    HOF.close()
    
    return {"message": f"{HOF_update.name} has been updated in the Hall of Fame!"}

@app.post("/delete_from_HOF")
def delete_from_HOF(ss: Delete_Hall_of_Famer):
    HOF = SessionLocal()
    HOF_delete = HOF.query(HallOfFame).filter(HallOfFame.id == ss.id).first()
    
    if not HOF_delete:
        HOF.close()
        return {"message": "No Hall of Famer found with the provided ID."}
    
    HOF.delete(HOF_delete)
    HOF.commit()
    HOF.close()
    
    return {"message": f"{HOF_delete.name} has been removed from the Hall of Fame!"}


# API Endpoints for Superstars
@app.post("/add_Superstar/")
def add_Superstar(ss: Create_Superstar):
    Superstar = SessionLocal()
    
    Superstar_entry = Superstars(
        name = ss.name,
        debut_year = ss.debut_year,
        age = ss.age,
        is_currently_active = ss.is_currently_active,
        total_titles_won = ss.total_titles_won,
        current_brand = ss.current_brand
    )
    
    Superstar.add(Superstar_entry)
    Superstar.commit()
    Superstar.refresh(Superstar_entry)
    Superstar.close()
    
    return {"message": f"{ss.name} has been added to the Superstars!"}

@app.get("/search_in_Superstars/{id}")
def search_in_Superstars(id: int):
    Superstar = SessionLocal()
    Superstar_search = Superstar.query(Superstars).filter(Superstars.id == id).first()
    
    if not Superstar_search:
        Superstar.close()
        return {"message": "No Superstar found with the provided ID."}
    
    return {
        "id": Superstar_search.id,
        "name": Superstar_search.name,
        "debut_year": Superstar_search.debut_year,
        "age": Superstar_search.age,
        "is_currently_active": Superstar_search.is_currently_active,
        "total_titles_won": Superstar_search.total_titles_won,
        "current_brand": Superstar_search.current_brand
    }
    
@app.post("/update_Superstar")
def update_Superstar(ss: Update_Superstar):
    Superstar = SessionLocal()
    Superstar_update = Superstar.query(Superstars).filter(Superstars.id == ss.id).first()
    
    if not Superstar_update:
        Superstar.close()
        return {"message": "No Superstar found with the provided ID."}
    
    if ss.name is not None:
        Superstar_update.name = ss.name
    if ss.debut_year is not None:
        Superstar_update.debut_year = ss.debut_year
    if ss.age is not None:
        Superstar_update.age = ss.age
    if ss.is_currently_active is not None:
        Superstar_update.is_currently_active = ss.is_currently_active
    if ss.total_titles_won is not None:
        Superstar_update.total_titles_won = ss.total_titles_won
    if ss.current_brand is not None:
        Superstar_update.current_brand = ss.current_brand
    
    Superstar.commit()
    Superstar.refresh(Superstar_update)
    Superstar.close()
    
    return {"message": f"{Superstar_update.name} has been updated in the Superstars!"}

@app.post("/delete_from_Superstars")
def delete_from_Superstars(ss: Delete_Superstar):
    Superstar = SessionLocal()
    Superstar_delete = Superstar.query(Superstars).filter(Superstars.id == ss.id).first()
    
    if not Superstar_delete:
        Superstar.close()
        return {"message": "No Superstar found with the provided ID."}
    
    Superstar.delete(Superstar_delete)
    Superstar.commit()
    Superstar.close()
    
    return {"message": f"{Superstar_delete.name} has been removed from the Superstars!"}



# API Endpoints for Next Generation
@app.post("/add_Next_Generation/")
def add_Next_Generation(ss: Create_Next_Generation):
    NextGen = SessionLocal()
    
    NextGen_entry = Next_Generation(
        name = ss.name,
        debut_year = ss.debut_year,
        age = ss.age,
        total_titles_won = ss.total_titles_won,
        current_brand = ss.current_brand
    )
    
    NextGen.add(NextGen_entry)
    NextGen.commit()
    NextGen.refresh(NextGen_entry)
    NextGen.close()
    
    return {"message": f"{ss.name} has been added to the Next Generation!"}

@app.get("/search_in_Next_Generation/{id}")
def search_in_Next_Generation(id: int):
    NextGen = SessionLocal()
    NextGen_search = NextGen.query(Next_Generation).filter(Next_Generation.id == id).first()
    
    if not NextGen_search:
        NextGen.close()
        return {"message": "No Next Generation Superstar found with the provided ID."}
    
    return {
        "id": NextGen_search.id,
        "name": NextGen_search.name,
        "debut_year": NextGen_search.debut_year,
        "age": NextGen_search.age,
        "total_titles_won": NextGen_search.total_titles_won,
        "current_brand": NextGen_search.current_brand
    }
    
@app.post("/update_Next_Generation")
def update_Next_Generation(ss: Update_Next_Generation):
    NextGen = SessionLocal()
    NextGen_update = NextGen.query(Next_Generation).filter(Next_Generation.id == ss.id).first()
    
    if not NextGen_update:
        NextGen.close()
        return {"message": "No Next Generation Superstar found with the provided ID."}
    
    if ss.name is not None:
        NextGen_update.name = ss.name
    if ss.debut_year is not None:
        NextGen_update.debut_year = ss.debut_year
    if ss.age is not None:
        NextGen_update.age = ss.age
    if ss.total_titles_won is not None:
        NextGen_update.total_titles_won = ss.total_titles_won
    if ss.current_brand is not None:
        NextGen_update.current_brand = ss.current_brand
    
    NextGen.commit()
    NextGen.refresh(NextGen_update)
    NextGen.close()
    
    return {"message": f"{NextGen_update.name} has been updated in the Next Generation!"}

@app.post("/delete_from_Next_Generation")
def delete_from_Next_Generation(ss: Delete_Next_Generation):    
    NextGen = SessionLocal()
    NextGen_delete = NextGen.query(Next_Generation).filter(Next_Generation.id == ss.id).first()
    
    if not NextGen_delete:
        NextGen.close()
        return {"message": "No Next Generation Superstar found with the provided ID."}
    
    NextGen.delete(NextGen_delete)
    NextGen.commit()
    NextGen.close()
    
    return {"message": f"{NextGen_delete.name} has been removed from the Next Generation!"}


@app.get("/")
def root():
    return {"Message" : "Add Your Favourite WWE Superstar to the Database using the /docs endpoint!"}
