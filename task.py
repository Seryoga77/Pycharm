from app import Base
from sqlalchemy import Column, ForeignKey, INTEGER, String, BOOLEAN
from sqlalchemy.orm import relationship
from app import user


class Task(Base):
    __tablename__ = "tasks"
    __table_args__ = {'keep_existing': True}
    id = Column(INTEGER, primary_key=True, index=True)
    title = Column(String)
    content = Column(String)
    priority = Column(INTEGER, default=0)
    completed = Column(BOOLEAN, default=False)
    user_id = Column(INTEGER, ForeignKey('users.id'), nullable=False, index=True)
    slug = Column(String, unique=True, index=True)

    user = relationship('User', back_populates='tasks')




from  sqlalchemy.schema import CreateTable
print(CreateTable(user.__table__))