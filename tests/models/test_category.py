import pytest

from src.models.base_model import BaseModel
from src.models.category import Category


@pytest.mark.parametrize('name,description', [('cat0001', 'desc0001'), ('A' * 100, 'B' * 200)])
def test_category_model(name, description):
    category = Category(name, description)

    assert isinstance(category, Category)
    assert isinstance(category, BaseModel)
    assert category.name == name
    assert category.description == description


def test_name_is_not_null():
    with pytest.raises(TypeError) as exc:
        Category(None, 'desc001')
        assert 'must be str' in exc.value


def test_name_is_str():
    with pytest.raises(TypeError) as exc:
        Category(0.1, 'desc002')
        assert 'must be str' in exc.value


def test_empty_name():
    with pytest.raises(ValueError) as exc:
        Category('', 'desc003')
        assert 'cannot be empty' in exc.value


def test_name_len():
    with pytest.raises(ValueError) as exc:
        Category('x' * 201, 'desc004')
        assert 'cannot have more than' in exc.value


def test_description_is_str():
    with pytest.raises(TypeError) as exc:
        Category('name', 1.0)
        assert 'must be str' in exc.value


def test_description_len():
    with pytest.raises(ValueError) as exc:
        Category('name', 'desc005' * 500)
        assert 'cannot have more than' in exc.value
