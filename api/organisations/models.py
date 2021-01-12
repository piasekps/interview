from sqlalchemy import Boolean, Column, Integer, String
from sqlalchemy.orm import relationship

from core.db.base import Base
from organisations.enums import OrganisationStatus


class Organisation(Base):
    __tablename__ = 'organisations'

    name = Column(String(128), nullable=False)
    status = Column(Integer, nullable=False, default=OrganisationStatus.ENABLED.value)
    users = relationship('User')
    enable_user_login = Column(Boolean, default=False)

    @property
    def status_name(self):
        """
        Map status to name.

        Returns:
            (str) status name
        """
        return OrganisationStatus.get_name_by_value(self.status)
