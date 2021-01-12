from datetime import datetime

from sqlalchemy import Column, DateTime, Integer
from sqlalchemy.ext.declarative import as_declarative, declared_attr
from sqlalchemy.orm.attributes import flag_modified
from sqlalchemy.schema import MetaData


# Constraint naming convention for alembic
convention = {
    'ix': 'ix_%(column_0_label)s',
    'uq': 'uq_%(table_name)s_%(column_0_name)s',
    'ck': 'ck_%(table_name)s_%(constraint_name)s',
    'fk': 'fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s',
    'pk': 'pk_%(table_name)s'
}


@as_declarative(metadata=MetaData(naming_convention=convention))
class Base:
    id = Column(Integer, primary_key=True)
    created_at = Column(DateTime, default=datetime.utcnow)

    @declared_attr
    def __tablename__(cls):
        return cls.__name__.lower()

    @staticmethod
    def _commit(commit, db_session):
        """
        Commit changes.

        Args:
            commit (bool): Indicates wheather to commit session or not
            db_session (Session): DB Session object
        """
        if commit:
            db_session.commit()
        else:
            db_session.flush()

    @classmethod
    def create(cls, db_session, commit=True, **kwargs):
        """
        Create an object with the given kwargs.

        Args:
            db_session (Session): DB Session object
            commit (bool): Indicates whether to commit session or not
            **kwargs: Keyword arguments to model class constructor

        Returns:
            Instance of the newly created model object
        """
        instance = cls(**kwargs)

        db_session.add(instance)
        cls._commit(commit, db_session)
        return instance

    def convert_object_to_dict(self, keys):
        """
        Create dict with object attribute, values as key and value.

        Args:
            keys (tuple): Object attribute names

        Returns:
            (dict) Object data as dict
        """
        return {key: getattr(self, key) for key in keys if hasattr(self, key)}

    def update(self, db_session, commit=True, **kwargs):
        """
        Update an object with the given kwargs.

        Args:
            db_session (Session): DB Session object
            commit (bool): Indicates whether to commit session or not

        Return:
            updated instance
        """
        self._update_instance(self, db_session, commit=commit, **kwargs)

        return self

    def _update_instance(self, instance, db_session, tuple_name=[], json_name=[], commit=True, **kwargs):
        """
        Update only new values to instance

        Args:
            instance: Model Instance
            db_session (Session): DB Session object
            tuple_name (tuple): Attribute field of SQLAlchemy ARRAY
            json_name (list): Contains a list of names which represents
                JSON fields on the instance
            commit (bool): Indicates whether to commit session or not

        Returns:
            Model Instance
        """
        for name, value in kwargs.items():
            if getattr(instance, name) == value:
                continue

            if name in tuple_name:
                value.extend(getattr(instance, name))

            if name in json_name:
                if getattr(instance, name) is not None:
                    current_value = getattr(instance, name)
                    current_value.update(value)
                    value = current_value

                flag_modified(instance, name)

            setattr(instance, name, value)

        db_session.add(instance)
        self._commit(commit, db_session)

        return instance

    @classmethod
    def get_by_id(cls, db_session, pk):
        """
        Get object by primary key

        Args:
            db_session (Session): DB Session object
            pk (int): Primary key

        Returns:
            Model instance or None
        """
        return db_session.query(cls).get(pk)

    @classmethod
    def delete_by_id(cls, db_session, instance_id, commit=True):
        """
        Remove item knowing it's ID

        Args:
            db_session (Session): DB Session object
            instance_id (uuid/str/int): Instance ID
            commit (bool): Indicates whether to commit session or not

        Returns:
            (bool)
        """
        instance = cls.get_by_id(db_session, instance_id)
        if not instance:
            return False

        db_session.delete(instance)
        cls._commit(commit, db_session)

        return True
