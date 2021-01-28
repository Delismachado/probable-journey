import sys
sys.path.append('.')
from src.models.category import Category

def test_name_is_not_null():
    try:
        category = Category(None, 'desc001')
    except Exception as error:
        assert isinstance(error, TypeError)
        
        
def test_name_is_str():
    try:
        category = Category(0, 'desc002')
    except Exception as error:
        assert isinstance(error, TypeError)
        
def test_empty_name():
    try:
        category = Category('', 'desc003')
    except Exception as error:
        assert isinstance(error, ValueError)
        
def test_name_len():
    try:
        category = Category('name'*21, 'desc004')
    except Exception as error:
        assert isinstance(error, ValueError)                
 
def test_description_is_str():
    try:
        category = Category('name', 1.0)
    except Exception as error:
        assert isinstance(error, TypeError)

def test_description_len():
    try:
        category = Category('name', 'desc005')
    except Exception as error:
        assert isinstance(error, ValueError)