from sqlalchemy import Column, String
from sqlalchemy.orm import validates

from src.models.base_model import BaseModel
from src.utils.validators import validate_type, validate_empty, validate_len


class Category(BaseModel):
    __tablename__ = 'category'
    name = Column('name', String(length=200), nullable=False)
    description = Column('description', String(length=200), nullable=True)

    def __init__(self, name: str, description: str = None) -> None:
        self.name = name
        self.description = description

    @validates('name')
    def validate_name(self, key, name):
        name = validate_type(name, key, str)
        name = validate_empty(name, key)
        return validate_len(name, key, 200)

    @validates('description')
    def validate_description(self, key, description):
        description = validate_type(description, key, str)
        return validate_len(description, key, 200)
