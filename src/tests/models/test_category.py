from src.models.category import Category
from src.models.base_model import BaseModel

import pytest


def test_category_model():
    name = 'cat0001'
    description = 'desc0001'

    category = Category(name, description)

    assert isinstance(category, Category)
    assert isinstance(category, BaseModel)
    assert category.name == name
    assert category.description == description


def test_name_is_not_null():
    with pytest.raises(ValueError):
        category = Category(None, 'desc001')


def test_name_is_str():
    with pytest.raises(TypeError):
        category = Category(0.1, 'desc002')


def test_empty_name():
    with pytest.raises(ValueError):
        category = Category('', 'desc003')


def test_name_len():
    with pytest.raises(ValueError):
        category = Category('x' * 201, 'desc004')


def test_description_is_str():
    with pytest.raises(TypeError):
        category = Category('name', 1.0)


def test_description_len():
    with pytest.raises(ValueError):
        category = Category('name', 'desc005' * 500)
