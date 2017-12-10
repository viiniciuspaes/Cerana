from sqlalchemy import create_engine, Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy_utils import database_exists, create_database
from db import db_constants as cons

Base = declarative_base()


class User(Base):
    __tablename__ = cons.TABLE_USER

    id = Column(cons.USER_ID, Integer, primary_key=True)
    password = Column(cons.USER_PASSWORD, String, nullable=False)
    user_type = Column(cons.USER_TYPE, String, nullable=False)


class Profile(Base):
    __tablename__ = cons.TABLE_PROFILE

    id = Column(cons.PROFILE_ID, Integer, primary_key=True)
    id_user = Column(cons.USER_ID, Integer, ForeignKey(User.id), nullable=False)
    town = Column(cons.TOWN, String, nullable=True)
    level = Column(cons.PROFILE_LEVEL, Integer, nullable=True)
    occupation = Column(cons.OCCUPATION, String, nullable=True)
    telephone = Column(cons.TELEPHONE, String, nullable=True)
    specialty = Column(cons.SPECIALTY, String, nullable=True)


class Tag(Base):
    __tablename__ = cons.TABLE_TAG

    id = Column(cons.TAG_ID, Integer, primary_key=True)
    name = Column(cons.TAG_NAME, String, nullable=False)


class Question(Base):
    __tablename__ = cons.TABLE_QUESTION

    id = Column(cons.QUESTION_ID, Integer, primary_key=True)
    id_user = Column(cons.USER_ID, Integer, ForeignKey(User.id), nullable=False)
    id_tag = Column(cons.USER_ID, Integer, ForeignKey(Tag.id), nullable=False)
    question = Column(cons.QUESTION, String, nullable=False)
    description = Column(cons.DESCRIPTION, String, nullable=False)


class Comment(Base):
    __tablename__ = cons.TABLE_COMMENT

    id = Column(cons.COMMENT_ID, Integer, primary_key=True)
    id_question = Column(cons.QUESTION_ID, Integer, ForeignKey(User.id), nullable=False)
    id_user = Column(cons.USER_ID, Integer, ForeignKey(User.id), nullable=False)
    likes = Column(cons.N_LIKES, Integer, nullable=False)
    mark = Column(cons.RIGHT_MARK, Boolean, nullable=True)
    answer = Column(cons.ANSWER, String, nullable=False)


class StudyLevel(Base):
    __tablename__ = cons.TABLE_STUDY_LEVEL

    id = Column(cons.STUDY_ID, Integer, primary_key=True)
    id_user = Column(cons.USER_ID, Integer, ForeignKey(User.id), nullable=False)
    degree = Column(cons.DEGREE_LEVEL, String, nullable=False)
    detail = Column(cons.DETAILS, String, nullable=True)


class Report(Base):
    __tablename__ = cons.TABLE_REPORT

    id = Column(cons.REPORT_ID, Integer, primary_key=True)
    id_user = Column(cons.USER_ID, Integer, ForeignKey(User.id), nullable=False)
    id_question = Column(cons.QUESTION_ID, Integer, ForeignKey(User.id), nullable=False)


def get_engine():

    user = "root"
    password = "password"
    address = "localhost"
    database_name = cons.DATABASE
    engine = create_engine('mysql+pymysql://%s:%s@%s/%s' % (user, password, address, database_name), echo=True)
    # engine = create_engine('mssql+pymssql://%s:%s@%s:5000/%s' %(user, password, address, database_name), echo=True)

    return engine


def init():
    engine = get_engine()
    if not database_exists(engine.url):
        create_database(engine.url)
    Base.metadata.create_all(bind=engine)
    return sessionmaker(bind=engine)
