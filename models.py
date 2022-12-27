from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()


class People(Base):
    __tablename__ = 'people'

    id = Column(Integer, primary_key=True, autoincrement=True)
    people_id = Column(Integer)
    birth_year = Column(String(15))
    eye_color = Column(String(15))
    films = Column(String())
    gender = Column(String(20))
    hair_color = Column(String(15))
    height = Column(String(10))
    homeworld = Column(String(100))
    mass = Column(String(10))
    name = Column(String(200), nullable=False)
    skin_color = Column(String(25))
    species = Column(String())
    vehicles = Column(String())
    starships = Column(String())
