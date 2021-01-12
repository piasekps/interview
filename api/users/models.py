from sqlalchemy import (
    Boolean,
    Column,
    ForeignKey,
    Integer,
    String,
)
from sqlalchemy.orm import Session, relationship

from core.db.base import Base
from users.enums import UserState


class User(Base):
    __tablename__ = 'users'

    first_name = Column(String(128), nullable=True)
    last_name = Column(String(128), nullable=True)
    email = Column(String(128))
    organisation_id = Column(Integer, ForeignKey('organisations.id'))
    organisation = relationship('Organisation', back_populates='users')
    state = Column(Integer, default=UserState.ENABLED.value)

    @property
    def name(self):
        return f'{self.first_name} {self.last_name}'

    @property
    def state_name(self):
        """
        Map state to name.

        Returns:
            (str) state name
        """
        return UserState.get_name_by_value(self.state)
