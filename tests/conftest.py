import pytest
from praktikum.database import Database
from unittest.mock import MagicMock
from praktikum.burger import Burger

@pytest.fixture
def burger():
    return Burger()

@pytest.fixture
def database():
    return Database()

@pytest.fixture
def mock_bun():
    bun = MagicMock()
    bun.get_name.return_value = "Test Bun"
    bun.get_price.return_value = 1.5
    return bun

@pytest.fixture
def mock_ingredient():
    """Замоканный ингредиент."""
    ingredient = MagicMock()
    ingredient.get_name.return_value = "Test Ingredient"
    ingredient.get_price.return_value = 0.75
    ingredient.get_type.return_value = "Filling"
    return ingredient




