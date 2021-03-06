from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
#import for creating a hash and verify a password
from passlib.apps import custom_app_context as pwd_context
 
Base = declarative_base()

class Category(Base): 
    __tablename__ = 'category'
   
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)

    @property
    def serialize(self):
       """Return object data in easily serializeable format"""
       return {
           'name'         : self.name,
           'id'           : self.id,
       }
 
class Item(Base):
    __tablename__ = 'item'


    id = Column(Integer, primary_key = True)
    name =Column(String(80), nullable = False)
    description = Column(String(250))
    category_id = Column(Integer,ForeignKey('category.id'))
    category = relationship(Category)

    @property
    def serialize(self):
       """Return object data in easily serializeable format"""
       return {
           'name'         : self.name,
           'id'           : self.id,
           'description'  : self.description,
           'category_id'  : self.category_id,
       }

class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    username = Column(String(32), index=True)
    password_hash = Column(String(64))

    @property
    def serialize(self):
       """Return object data in easily serializeable format"""
       return {
           'username'         : self.username,
           'id'           : self.id,
           'password_hash'  : self.password_hash,
       }

    def hash_password(self, password):
        self.password_hash = pwd_context.encrypt(password)

    def verify_password(self, password):
	return pwd_context.verify(password, self.password_hash)


engine = create_engine('sqlite:///categorymenu.db')
 

Base.metadata.create_all(engine)
