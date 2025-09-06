from sqlalchemy import Boolean, Column, Integer, String, ENUM, foreignKey
from database import Base

class Country(Base):
    __tablename__ = "countries"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)
    continent = Column(String, index=True)

class Seasonality(Base):
    __tablename__ = "seasonalities"

    id = Column(Integer, primary_key=True)
    produce_id = Column(Integer, foreignKey('produce.id'), index=True)
    country_id = Column(Integer, foreignKey('countries.id'), index=True)
    month = Column(ENUM('January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December'), index=True)
    in_season = Column(Boolean, index=True)

class Produce(Base):
    __tablename__ = "produce"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True)
    type = Column(ENUM('fruit', 'vegetable'), index=True)