from sqlalchemy import create_engine, Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy_utils import database_exists, create_database
from db import db_constants as cons

Base = declarative_base()


class User(Base):
    __tablename__ = cons.TABLE_USER

    id = Column(cons.USER_ID, Integer, primary_key=True)
    login = Column(cons.USER_LOGIN, String(60), nullable=False, unique=True)
    password = Column(cons.USER_PASSWORD, String(60), nullable=False)
    user_type = Column(cons.USER_TYPE, String(60), nullable=False)
    active = Column(cons.USER_ACTIVE, Boolean, nullable=False)

    @property
    def is_authenticated(self):
        return True

    @property
    def is_active(self):
        return True

    @property
    def is_anonymous(self): #usuario logado reto
        return False

    def get_id(self):
        return str(self.id)

class Profile(Base):
    __tablename__ = cons.TABLE_PROFILE

    id = Column(cons.PROFILE_ID, Integer, primary_key=True)
    id_user = Column(cons.USER_ID, Integer, ForeignKey(User.id), nullable=False)
    name = Column(cons.PROFILE_NAME, String(60), nullable=False)
    city = Column(cons.CITY, String(60), nullable=True)
    level = Column(cons.PROFILE_LEVEL, Integer, nullable=True)
    occupation = Column(cons.OCCUPATION, String(60), nullable=True)
    telephone = Column(cons.TELEPHONE, String(60), nullable=True)
    specialty = Column(cons.SPECIALTY, String(60), nullable=True)


class Tag(Base):
    __tablename__ = cons.TABLE_TAG

    id = Column(cons.TAG_ID, Integer, primary_key=True)
    name = Column(cons.TAG_NAME, String(60), nullable=False)


# class Question(Base):
#     __tablename__ = cons.TABLE_QUESTION
#
#     id = Column(cons.QUESTION_ID, Integer, primary_key=True)
#     id_user = Column(cons.USER_ID, Integer, ForeignKey(User.id), nullable=False)
#     id_tag = Column(cons.TAG_ID, Integer, ForeignKey(Tag.id), nullable=False)
#     question = Column(cons.QUESTION, String(260), nullable=False, unique=True)
#     description = Column(cons.DESCRIPTION, String(600), nullable=False)
#
#
# class Comment(Base):
#     __tablename__ = cons.TABLE_COMMENT
#
#     id = Column(cons.COMMENT_ID, Integer, primary_key=True)
#     id_question = Column(cons.QUESTION_ID, Integer, ForeignKey(Question.id), nullable=False)
#     id_user = Column(cons.USER_ID, Integer, ForeignKey(User.id), nullable=False)
#     likes = Column(cons.N_LIKES, Integer, nullable=False)
#     mark = Column(cons.RIGHT_MARK, Boolean, nullable=True)
#     answer = Column(cons.ANSWER, String(600), nullable=False, unique=True)


class StudyLevel(Base):
    __tablename__ = cons.TABLE_STUDY_LEVEL

    id = Column(cons.STUDY_ID, Integer, primary_key=True)
    id_user = Column(cons.USER_ID, Integer, ForeignKey(User.id), nullable=False)
    degree = Column(cons.DEGREE_LEVEL, String(60), nullable=False)
    detail = Column(cons.DETAILS, String(120), nullable=True)


class Report(Base):
    __tablename__ = cons.TABLE_REPORT

    id = Column(cons.REPORT_ID, Integer, primary_key=True)
    id_user = Column(cons.USER_ID, Integer, ForeignKey(User.id), nullable=False)
    id_question = Column(cons.QUESTION_ID, Integer, ForeignKey(User.id), nullable=False)


class Animal(Base):
    __tablename__ = cons.TABLE_ANIMALS

    id = Column(cons.ANIMAL_ID, Integer, primary_key=True)
    scientific_name = Column(cons.ANIMAL_SCIENTIFIC_NAME, String(60), nullable=False)
    popular_name = Column(cons.ANIMALS_COMMON_NAME, String(60), nullable=False)
    family = Column(cons.ANIMALS_FAMILY, String(60), nullable=False)
    kingdom = Column(cons.ANIMALS_KINGDOM, String(60), nullable=False)
    phylum = Column(cons.ANIMALS_PHYLUM, String(60), nullable=False)
    description = Column(cons.ANIMALS_DESCRIPTION, String(260), nullable=False)


class Plant(Base):
    __tablename__ = cons.TABLE_PLANTS

    id = Column(cons.PLANT_ID, Integer, primary_key=True)
    scientific_name = Column(cons.PLANT_SCIENTIFIC_NAME, String(60), nullable=False)
    popular_name = Column(cons.PLANT_COMMON_NAME, String(60), nullable=False)
    family = Column(cons.PLANT_FAMILY, String(60), nullable=False)
    kingdom = Column(cons.PLANT_KINGDOM, String(60), nullable=False)
    phylum = Column(cons.PLANT_PHYLUM, String(60), nullable=False)
    description = Column(cons.PLANT_DESCRIPTION, String(260), nullable=False)


def get_engine():

    user = "root"
    password = ""
    address = "localhost"
    database_name = cons.DATABASE
    engine = create_engine('mysql+pymysql://%s:%s@%s/%s' % (user, password, address, database_name), echo=True)
    # engine = create_engine('mysql+pymysql://%s:%s@%s:3000/%s' %(user, password, address, database_name), echo=True)

    return engine


def get_session():
    engine = get_engine()
    return sessionmaker(bind=engine)


def init():
    engine = get_engine()
    if not database_exists(engine.url):
        create_database(engine.url)
    Base.metadata.create_all(bind=engine)
    return sessionmaker(bind=engine)