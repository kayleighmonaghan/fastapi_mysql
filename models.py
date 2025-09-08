from sqlalchemy import Boolean, Column, Integer, String, Enum, ForeignKey
from database import Base

class Country(Base):
    __tablename__ = "countries"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(50), unique=True, index=True)
    continent = Column(String(50), index=True)

class Produce(Base):
    __tablename__ = "produce"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(50), unique=True)
    type = Column(Enum('Fruit', 'Vegetable'), index=True)

class Seasonality(Base):
    __tablename__ = "seasonalities"

    id = Column(Integer, primary_key=True)
    produce_id = Column(Integer, ForeignKey('produce.id'), index=True)
    country_id = Column(Integer, ForeignKey('countries.id'), index=True)
    month = Column(Enum('January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December'), index=True)
    in_season = Column(Boolean, index=True)

