from sqlalchemy.ext.declarative import declarative_base
import sqlalchemy
from db import get_oracle_engine

DeclarativeBase = declarative_base(
    metadata=sqlalchemy.MetaData(
        bind=get_oracle_engine(),
        schema='lcs2train'
    )
)


class Facility(DeclarativeBase):
    __tablename__ = 'facility'

    closureid = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True)
    facilityid = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True)
    recordnum = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True)
    lanedetails = sqlalchemy.Column(sqlalchemy.Integer)
    duration = sqlalchemy.Column(sqlalchemy.VARCHAR(1))
    startdate = sqlalchemy.Column(sqlalchemy.DateTime)
    enddate = sqlalchemy.Column(sqlalchemy.DateTime)
    geojson = sqlalchemy.Column(sqlalchemy.Text)
