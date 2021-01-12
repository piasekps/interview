from sqlalchemy import (
    Column,
    ForeignKey,
    Integer,
    String,
)
from sqlalchemy.orm import Session, relationship

from core.db.base import Base


class User(Base):
    __tablename__ = 'users'

    first_name = Column(String(128), nullable=True)
    last_name = Column(String(128), nullable=True)
    email = Column(String(128))
    organisation_id = Column(Integer, ForeignKey('organisations.id'))
    organisation = relationship('Organisation', back_populates='users')

    @property
    def name(self):
        return f'{self.first_name} {self.last_name}'





