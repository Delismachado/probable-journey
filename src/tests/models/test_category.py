from src.models.category import Category
from src.models.base_model import BaseModel

import pytest


def test_category_model():
    category = Category("cat0001", "desc0001")

    assert isinstance(category, Category)
    assert isinstance(category, BaseModel)


def test_category_name_empty():
    with pytest.raises(ValueError):
        category = Category("", "description")


def test_category_name_len():
    with pytest.raises(ValueError):
        category = Category("name" * 200, "description")


def test_category_name_int():
    with pytest.raises(TypeError):
        category = Category(100, "description")


def test_category_description_int():
    with pytest.raises(TypeError):
        category = Category("Nome", 10)


def test_category_description_len():
    with pytest.raises(ValueError):
        category = Category("Nome", "phone" * 200)
