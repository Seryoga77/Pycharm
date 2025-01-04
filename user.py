from app import Base
from  sqlalchemy import Column, INTEGER, String
from sqlalchemy.orm import relationship

from app import task


class User(Base):
    __tablename__="users"
    __table_args__ = {'keep_existing': True}
    id = Column(INTEGER, primary_key=True, index=True)
    username = Column(String)
    firstname = Column(String)
    lastname = Column(String)
    age = Column(INTEGER)
    slug = Column(String, unique=True, index=True)

    tasks = relationship('Task', back_populates='user')


    category = relationship('category', back_populates='products')

from  sqlalchemy.schema import CreateTable
print(CreateTable(task.__table__))

