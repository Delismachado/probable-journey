import sys

sys.path.append('.')
from src.models.category import Category
from src.models.base_model import BaseModel


def test_category_model():
    name = 'cat0001'
    description = 'desc0001'

    category = Category(name, description)

    assert isinstance(category, Category)
    assert isinstance(category, BaseModel)
    assert category.name == name
    assert category.description == description


def test_name_is_not_null():
    try:
        category = Category(None, 'desc001')
        raise AssertionError('The exception was not raised.')
    except Exception as error:
        assert isinstance(error, ValueError)
        assert error.args == ('Name cannot be null.',)


def test_name_is_str():
    try:
        category = Category(0.1, 'desc002')
        raise AssertionError('The exception was not raised.')
    except Exception as error:
        assert isinstance(error, TypeError)
        assert error.args == ('Name should be str.',)


def test_empty_name():
    try:
        category = Category('', 'desc003')
        raise AssertionError('The exception was not raised.')
    except Exception as error:
        assert isinstance(error, ValueError)
        assert error.args == ('Name cannot be empty.',)


def test_name_len():
    try:
        category = Category('x' * 201, 'desc004')
        raise AssertionError('The exception was not raised.')
    except Exception as error:
        assert isinstance(error, ValueError)
        assert error.args == ('Name cannot larger then 200 characters.',)


def test_description_is_str():
    try:
        category = Category('name', 1.0)
        raise AssertionError('The exception was not raised.')
    except Exception as error:
        assert isinstance(error, TypeError)
        assert error.args == ('Description cannot be str.',)


def test_description_len():
    try:
        category = Category('name', 'desc005' * 500)
        raise AssertionError('The exception was not raised.')
    except Exception as error:
        assert isinstance(error, ValueError)
        assert error.args == ('Description can not more then 200.',)
