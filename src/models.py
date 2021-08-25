import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, Date, Numeric
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    last_name=Column(String, nullable= False)
    _password=Column(String, nullable=False)
    nickname=Column(String, nullable=False)
    email=Column(String, unique=True, nullable=False)
    fav = relationship("Favorite")

class Favorite(Base):
    __tablename__ = 'favorite'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship("User")
    people_id = Column(Integer, ForeignKey('people.id'))
    people = relationship("People")
    planets_id = Column(Integer, ForeignKey('planets.id'))
    planets = relationship("Planets")
    starships_id = Column(Integer, ForeignKey('starships.id'))
    starships = relationship("Starships")

class People(Base):
    __tablename__ = 'people'
    id = Column(Integer, primary_key=True)
    url=Column(String, nullable=False)
    height=Column(Numeric, nullable=True)
    mass=Column(Numeric, nullable=True)
    hair_color=Column(String, nullable=True)
    skin_color=Column(String, nullable=True)
    eye_color=Column(String, nullable=True)
    birth_year=Column(String, nullable=True)
    gender=Column(String, nullable=True)
    name=Column(String, nullable=True)
    created=Column(String, nullable=True)
    edited= Column(String, nullable=True)

class Planets(Base):
    __tablename__ = 'planets'
    id = Column(Integer, primary_key=True)
    url=Column(String, nullable=False)
    name=Column(String, nullable=False)
    diameter=Column(Numeric, nullable=False)
    orbital_period=Column(Numeric, nullable=False)
    gravity=Column(Numeric, nullable=False)
    population=Column(Numeric, nullable=False)
    terrain=Column(String, nullable=False)
    surface_water=Column(Numeric, nullable=False)
    rotation_period=Column(Numeric, nullable=False)
    climate=Column(String, nullable=False)
    create=Column(String, nullable=True)
    edited=Column(String, nullable=True)
    description=Column(String, nullable=False)

class Starships(Base):
    __tablename__ = 'starships'
    id = Column(Integer, primary_key=True)
    url=Column(String, nullable=False)
    model=Column(String, nullable=True)
    consumables=Column(String, nullable=True)
    manufacturer=Column(String, nullable=True)
    crew=Column(Numeric, nullable=True)
    passengers=Column(Numeric, nullable=True)
    starship_class=Column(String, nullable=True)
    length=Column(Numeric, nullable=True)
    cargo_capacity=Column(Numeric, nullable=True)
    consumables=Column(String, nullable=True)
    created=Column(String, nullable=True)
    edited= Column(String, nullable=True)

def get_all(): 
    user = User.query.all()
    return user

def get_by_id(id):
    user = User.query.get(id).one_or_None()
    return user

def get_by_nick(nick):
    user = User.query.filter_by(nick = nick).one_or_None()
    return user

render_er(Base, 'diagram.png')