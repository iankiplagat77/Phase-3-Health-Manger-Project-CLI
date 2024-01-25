#imports
import click
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from patients.models import Base, Patient, Room

engine = create_engine('sqlite:///app.db')
Base.metadata.create_all(bind=engine)
Session = sessionmaker(bind=engine)

@click.group()
def cli():
    pass

@cli.command()
@click.argument('patient_name')
@click.argument('room_name')
def add_patient(patient_name, room_name):
    session = Session()

    # Check if the choosen room exists and if it does not exist, create the specified room
    room = session.query(Room).filter_by(name=room_name).first()
    if not room:
        room = Room(name=room_name)
        session.add(room)
        session.commit()

    # create the room and give the patient the room selected
    patient = Patient(name=patient_name, room=room)
    session.add(patient)
    session.commit()

    print(f'You have given  "{patient_name}"  "{room_name}".')

@cli.command()
def list_patients():
    session = Session()
    patients = session.query(Patient).all()
    for patient in patients:
        print(f'ID for Patient: {patient.id}, Name of Patient: {patient.name}, Patient is in Room: {patient.room.name}')



if __name__ == '__main__':
    cli()
