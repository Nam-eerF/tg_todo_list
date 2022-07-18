from sqlalchemy import (Column, Integer, BigInteger, String,
                        Sequence, TIMESTAMP, Boolean, JSON, Text)
from sqlalchemy import sql
from tgbot.services.db_api.database import db


class User(db.Model):
    __tablename__ = 'user'
    query: sql.Select

    id = Column(BigInteger, Sequence('user_id_sequence'), primary_key=True)
    email = Column(String(50), primary_key=True)
    password = Column(String(250))


class Tasks(db.Model):
    __tablename__ = 'tasks'
    query: sql.Select

    id = Column(BigInteger, Sequence('user_id_sequence'), primary_key=True)
    name = Column(String(150))
    description = Column(Text)
    status = Column(Boolean, default=False)
