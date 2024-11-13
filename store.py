from products import Product, LimitedProduct, NonStockedProduct
from collections import defaultdict


class Store:
    """
    A class to represent a store with a collection of products.

    Instance Variable:
              __products (list[Product]): Private instance variables, a list
              of Product objects available in the store.
    """

    def __init__(self, product_list: list[Product]):
        """
        Initializes a Store object with a list of products.

        Parameter:
            product_list (list[Product]): A list of Product objects to
            initialize the store's inventory. (Private Instance)
        """
        self.__products: list = product_list

    def add_product(self, product):
        """
        Adds a product to the store's inventory.

        Parameter:
            product (Product): The product to add to the inventory.
        """
        self.get_products().append(product)

    def remove_product(self, product):
        """
        Removes a product from the store's inventory.

        Parameter:
            product (Product): The product to remove from the inventory.
        """
        self.get_products().remove(product)

    def get_total_quantity(self) -> int:
        """
        Calculates the total quantity of all products in the store.

        Returns:
            int: The total quantity of all products in the store.
        """
        total_quantities: int = 0
        for product in self.get_products():
            total_quantities += product.get_quantity()
        return total_quantities

    def get_all_products(self) -> list[Product]:
        """
        Retrieves a list of all active products in the store.

        Returns:
            list[Product]: A list of active Product objects.
        """
        total_products: list[Product] = list()
        for product in self.get_products():
            if product.is_active():
                total_products.append(product)
        return total_products

    def order(self, shopping_list: list[tuple[Product, int]]) -> float:
        """
        Places an order for a list of products and quantities, updating
        product quantities.

        Parameter:
            shopping_list (list[tuple[Product, int]]): A list of tuples where
            each tuple contains a Product and the quantity ordered.

        Returns:
            float: The total cost of the order.
        """
        total_cost: float = 0.0
        for product, order in shopping_list:
            total_cost += product.buy(order)
        return total_cost

    def validate_order(self,
                       shopping_list: list[tuple[Product, int]]) -> None:
        """
        Validates that the quantities in the order are available in stock.

        Parameter:
            shopping_list (list[tuple[Product, int]]): A list of tuples where
            each tuple contains a Product and the quantity ordered.

        Raises:
            ValueError: If the requested quantity exceeds available
                        stock for any product.
        """
        aggregated = defaultdict(int)

        for product, order in shopping_list:
            if not isinstance(product, NonStockedProduct) and product.get_quantity() < order:
                raise ValueError(
                    "Error while making order! Quantity larger than what exists\n")

            if isinstance(product, LimitedProduct):
                aggregated[product] += order

        for product in aggregated:
            if isinstance(product, LimitedProduct) and aggregated[
                product] > product.get_maximum():
                raise ValueError(
                    f"Error while making order! The maximum order is {product.get_maximum()}\n")

    def get_products(self):
        """
        Retrieves the store's list of products.

        Returns:
            list[Product]: The store's product inventory.
        """
        return self.__products

    def set_products(self, products):
        """
        Sets the store's inventory with a new list of products.

        Parameter:
            products (list[Product]): A new list of products.

        Raises:
            ValueError: If the provided products argument is not a non-empty
            list of Product objects.
        """
        if isinstance(products, list) and products:
            self.__products = products
        else:
            raise ValueError("Products must be a list of products")
