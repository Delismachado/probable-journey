import pytest
from sqlalchemy.orm.exc import UnmappedInstanceError

from src.dao.base_dao import BaseDao
from src.dao.category_dao import CategoryDao
from src.models.category import Category


class TestCategoryDao:
    @pytest.fixture
    def dao_instance(self):
        return CategoryDao()

    def test_instance(self, dao_instance):
        assert isinstance(dao_instance, CategoryDao)
        assert isinstance(dao_instance, BaseDao)

    def test_save(self, dao_instance):
        category = Category('Um nome', 'Uma descrição')
        category_saved = dao_instance.save(category)

        assert category_saved.id_ is not None
        dao_instance.delete(category_saved)

    def test_not_save(self, dao_instance):
        with pytest.raises(UnmappedInstanceError):
            dao_instance.save('category')

    def test_read_by_id(self, dao_instance):
        category = Category('Um nome', 'Uma descrição')
        category_saved = dao_instance.save(category)
        category_read = dao_instance.read_by_id(category_saved.id_)

        assert isinstance(category_read, Category)
        dao_instance.delete(category_saved)

    def test_not_read_by_id(self, dao_instance):
        with pytest.raises(TypeError):
            dao_instance.read_by_id('category_saved.id_')

    def test_read_all(self, dao_instance):
        category_read = dao_instance.read_all()

        assert isinstance(category_read, list)

    def test_delete(self, dao_instance):
        category = Category('Um nome', 'Uma descrição')
        category_saved = dao_instance.save(category)
        category_read = dao_instance.read_by_id(category_saved.id_)
        dao_instance.delete(category_read)
        category_read = dao_instance.read_by_id(category_saved.id_)

        assert category_read is None

    def test_not_delete(self, dao_instance):
        with pytest.raises(UnmappedInstanceError):
            dao_instance.delete('category_read')
