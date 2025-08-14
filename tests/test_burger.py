import pytest
from unittest.mock import MagicMock

class TestBurger:

    def test_set_buns(self, burger, mock_bun):
        burger.set_buns(mock_bun)
        assert burger.bun == mock_bun

    def test_add_ingredient(self, burger, mock_ingredient):
        burger.add_ingredient(mock_ingredient)
        assert len(burger.ingredients) == 1
        assert burger.ingredients[0] == mock_ingredient

    def test_remove_ingredient(self, burger, mock_ingredients):
        burger.ingredients = mock_ingredients
        initial_count = len(burger.ingredients)
        burger.remove_ingredient(1)
        assert len(burger.ingredients) == initial_count - 1
        assert "Ingredient 1" not in [ing.get_name() for ing in burger.ingredients]

    def test_move_ingredient(self, burger, mock_ingredients):
        burger.ingredients = mock_ingredients

        burger.move_ingredient(2, 0)
        assert burger.ingredients[0].get_name() == "Ingredient 2"
        assert burger.ingredients[1].get_name() == "Ingredient 0"

    @pytest.mark.parametrize(
        "ingredient_indexes, expected_price",
        [
            ([], 200 * 2),
            ([0, 1], 200 * 2 + 100 + 150),
            ([0, 1, 2], 200 * 2 + 100 + 150 + 200),
        ],
    )
    def test_get_price(self, burger, mock_bun, mock_ingredients, ingredient_indexes, expected_price):
        burger.set_buns(mock_bun)

        for idx in ingredient_indexes:
            burger.add_ingredient(mock_ingredients[idx])

        assert burger.get_price() == expected_price

    def test_get_receipt(self, burger, mock_bun, mock_ingredient):
        burger.set_buns(mock_bun)
        burger.add_ingredient(mock_ingredient)

        expected_receipt = (
            f"(==== {mock_bun.get_name()} ====)\n"
            f"= {mock_ingredient.get_type().lower()} {mock_ingredient.get_name()} =\n"
            f"(==== {mock_bun.get_name()} ====)\n"
            "\n"
            f"Price: {burger.get_price()}"
        )
        assert burger.get_receipt() == expected_receipt



