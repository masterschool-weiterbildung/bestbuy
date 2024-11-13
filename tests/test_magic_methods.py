import pytest

import products
import store


@pytest.fixture
def setup_data():
    mac = products.Product("MacBook Air M2", price=1450, quantity=100)
    bose = products.Product("Bose QuietComfort Earbuds", price=250,
                            quantity=500)

    best_buy = store.Store([mac, bose])

    print("\nSetting up resources...")
    yield best_buy  # Provide the data to the test
    # Teardown: Clean up resources (if any) after the test
    print("\nTearing down resources...")


class TestMagicMethods:
    def test_negative_price(self, setup_data):
        with pytest.raises(ValueError,
                           match="Price must be a float"):
            setup_data.get_products()[0].set_price(-100)

    @pytest.mark.parametrize("product",
                             [
                                 products.Product("MacBook Air M2",
                                                  price=1450, quantity=100)
                             ]
                             )
    def test_print_product(self, product, setup_data):
        assert setup_data.get_products()[
                   0] == product

    def test_greater_than_product(self, setup_data):
        assert setup_data.get_products()[0] > setup_data.get_products()[1]

    def test_less_than_product(self, setup_data):
        assert setup_data.get_products()[0] < setup_data.get_products()[1]

    def test_in_store(self, setup_data):
        assert setup_data.get_products()[0] in setup_data.get_products()

    @pytest.mark.parametrize("product",
                             [
                                 products.LimitedProduct("Google Pixel 7",
                                                         price=500,
                                                         quantity=250,
                                                         maximum=1)
                             ]
                             )
    def test_not_in_store(self, product, setup_data):
        assert product not in setup_data.get_products()
