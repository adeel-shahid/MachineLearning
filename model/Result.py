# import sqlalchemy as db
# from sqlalchemy.ext.declarative import declarative_base
# import Engine as e
# Base = declarative_base()
#
# class Result(Base):
#     __tablename__ = 'Result'
#
#     arid = db.Column(db.Integer, foreign_key=True)
#     course = db.Column(db.String(100))
#     grade = db.Column(db.String(50))
#     marks = db.Column(db.Integer)
#
# Base.metadata.create_all(e.engine)

from sqlalchemy.orm import declarative_base
import sqlalchemy as db
import database as dt

Base=declarative_base()

class Result(Base):
    __tablename__ = 'Result'
    id=db.Column(db.Integer, primary_key=True)
    arid_number = db.Column(db.Integer, primary_key=True)
    course=db.Column(db.String)
    grade=db.Column(db.String)
    marks=db.Column(db.Integer)

session=dt.returnSession()
S=[Result(arid_number=1,course="PDC",grade="A",marks=80),
Result(arid_number=2,course="CC",grade="A",marks=80)

   ]

dt.updateTables(Base)
session.add_all(S)
session.commit()