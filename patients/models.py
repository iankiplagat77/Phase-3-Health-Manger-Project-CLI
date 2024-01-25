from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import declarative_base, relationship

Base = declarative_base()


#table for patients
class Patient(Base):
    __tablename__ = 'patients'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False, unique=True)
    room_id = Column(Integer, ForeignKey('rooms.id'))
    room = relationship('Room', back_populates='patients')


#table for rooms, will be created if not available
class Room(Base):
    __tablename__ = 'rooms'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False, unique=True)
    patients = relationship('Patient', back_populates='room')
