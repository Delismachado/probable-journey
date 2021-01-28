import sys

sys.path.append('.')

from sqlalchemy import Column, String
from sqlalchemy.orm import validates
from src.models.base_model import BaseModel


class Category(BaseModel):
    __tablename__ = 'category'
    name = Column('name', String(length=200), nullable=False)
    description = Column('description', String(length=200), nullable=True)

    def __init__(self, name: str, description: str = None) -> None:
        self.name = name
        self.description = description

    @validates('name')
    def validate_name(self, key, name):
        if  name is None:
            raise ValueError('Name cannot be null.')
        if not isinstance(name, str):
            raise TypeError('Name should be str.')
        if not name.strip():
            raise ValueError('Name cannot be empty.')
        if len(name) > 200:
            raise ValueError('Name cannot larger then 200 characters.')
        return name

    @validates('description')
    def validate_description(self, key, description):
        if not isinstance(description, str):
            raise TypeError('Description must be str.')
        if len(description) > 200:
            raise ValueError('Description can not more then 200.')
        return description
