from sqlalchemy.orm import declarative_base
import sqlalchemy as db
import database as dt

Base=declarative_base()

class Student(Base):
    __tablename__ = 'Student'
    arid=db.Column(db.Integer, primary_key=True)
    name=db.Column(db.String)
    section=db.Column(db.String)
    arid_number=db.Column(db.String)

session=dt.returnSession()
S=[Student(name="Adeel",section="BSC-7",arid_number=1),
Student(name="Aness",section="BSC-7",arid_number=2)

   ]

dt.updateTables(Base)
session.add_all(S)
session.commit()