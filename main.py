from fastapi import FastAPI, HTTPException, Depends, status
from pydantic import BaseModel
from typing import Annotated
import models
from database import engine, SessionLocal
from sqlalchemy.orm import Session

app = FastAPI()
# models.Base.metadata.create_all(bind=engine)

@app.on_event("startup")
async def create_tables():
    models.Base.metadata.create_all(bind=engine)
class CountryBase(BaseModel):
    name: str
    continent: str

class ProduceBase(BaseModel):
    name: str
    type: str

class SeasonalityBase(BaseModel):
    produce_id: int
    country_id: int
    month: str
    in_season: bool

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

db_dependency = Annotated[Session, Depends(get_db)]

@app.post("/seasonalities/", status_code=status.HTTP_201_CREATED)
async def create_seasonality(seasonality: SeasonalityBase, db: db_dependency):
    db_seasonality = models.Seasonality(**seasonality.dict())
    db.add(db_seasonality)
    db.commit()
    return {"message": "Seasonality record created successfully"}

@app.get("/seasonalities/{produce_id}/{country_id}/{month}", status_code=status.HTTP_200_OK)
async def read_seasonality(produce_id: int, country_id: int, month: str, db: db_dependency):
    db_seasonality = db.query(models.Seasonality).filter(
        models.Seasonality.produce_id == produce_id,
        models.Seasonality.country_id == country_id,
        models.Seasonality.month == month
    ).first()
    if db_seasonality is None:
        raise HTTPException(status_code=404, detail="Seasonality record not found")
    return db_seasonality

@app.delete("/seasonalities/{produce_id}/{country_id}/{month}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_seasonality(produce_id: int, country_id: int, month: str, db: db_dependency):
    db_seasonality = db.query(models.Seasonality).filter(
        models.Seasonality.produce_id == produce_id,
        models.Seasonality.country_id == country_id,
        models.Seasonality.month == month
    ).first()
    if db_seasonality is None:
        raise HTTPException(status_code=404, detail="Seasonality record not found")
    db.delete(db_seasonality)
    db.commit()

@app.post("/produce/", status_code=status.HTTP_201_CREATED)
async def create_produce(produce: ProduceBase, db: db_dependency):
    db_produce = models.Produce(**produce.dict())
    db.add(db_produce)
    db.commit()

@app.get("/produce/{produce_id}", status_code=status.HTTP_200_OK)
async def read_produce(produce_id: int, db: db_dependency):
    db_produce = db.query(models.Produce).filter(models.Produce.id == produce_id).first()
    if db_produce is None:
        raise HTTPException(status_code=404, detail="Produce not found")
    return db_produce

@app.delete("/produce/{produce_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_produce(produce_id: int, db: db_dependency):
    db_produce = db.query(models.Produce).filter(models.Produce.id == produce_id).first()
    if db_produce is None:
        raise HTTPException(status_code=404, detail="Produce not found")
    db.delete(db_produce)
    db.commit()

@app.post("/countries/", status_code=status.HTTP_201_CREATED)
async def create_country(country: CountryBase, db: db_dependency):
    db_country = models.Country(**country.dict())
    db.add(db_country)
    db.commit()

@app.get("/countries/{country_id}", status_code=status.HTTP_200_OK)
async def read_country(country_id: int, db: db_dependency):
    db_country = db.query(models.Country).filter(models.Country.id == country_id).first()
    if db_country is None:
        raise HTTPException(status_code=404, detail="Country not found")
    return db_country

@app.delete("/countries/{country_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_country(country_id: int, db: db_dependency):
    db_country = db.query(models.Country).filter(models.Country.id == country_id).first()
    if db_country is None:
        raise HTTPException(status_code=404, detail="Country not found")
    db.delete(db_country)
    db.commit()