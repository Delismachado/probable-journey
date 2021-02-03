import pytest

from src.controllers.base_controller import BaseController
from src.controllers.category_controller import CategoryController
from src.models.category import Category


class TestCategoryController:
    @pytest.fixture
    def controller_instance(self):
        return CategoryController()

    def test_category_controller_instance(self, controller_instance):
        assert isinstance(controller_instance, BaseController)
        assert isinstance(controller_instance, CategoryController)

    def test_read_all_should_return_list(self, controller_instance):
        result = controller_instance.read_all()

        assert isinstance(result, list)

    def test_create_category(self, controller_instance):
        name = 'Category'
        description = 'Test'
        category = Category(name, description)

        result = controller_instance.create(category)

        assert result.id_ is not None
        assert result.name == name
        assert result.description == description

        controller_instance.delete(result)

    def test_update_category(self, controller_instance):
        name = 'Category'
        description = 'Test'
        category = Category(name, description)
        created = controller_instance.create(category)

        created.name = 'Category 2'
        created.description = 'Test 2'
        result = controller_instance.update(created)

        assert result.id_ is not None
        assert result.name == 'Category 2'
        assert result.description == 'Test 2'

        controller_instance.delete(result)

    def test_delete_category(self, controller_instance):
        name = 'Category'
        description = 'Test'
        category = Category(name, description)
        created = controller_instance.create(category)

        controller_instance.delete(created)

        with pytest.raises(Exception) as exc:
            controller_instance.read_by_id(created.id_)
            assert exc.value == 'Object not found in the database.'

    def test_read_by_id_should_return_category(self, controller_instance):
        name = 'Category'
        description = 'Test'
        category = Category(name, description)
        created = controller_instance.create(category)

        result = controller_instance.read_by_id(created.id_)

        assert isinstance(result, Category)
        assert result.name == name
        assert result.description == description

        controller_instance.delete(created)

    def test_read_by_id_with_invalid_id_should_raise_exception(self, controller_instance):
        with pytest.raises(Exception) as exc:
            controller_instance.read_by_id(71289379)
            assert exc.value == 'Object not found in the database.'
