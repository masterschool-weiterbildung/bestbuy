from products import Product, LimitedProduct, NonStockedProduct
from collections import defaultdict


class Store:
    """
    Represents a store that manages a collection of products and handles orders.

    Attributes:
        __products (list[Product]): A private list containing the store's products.
    """

    def __init__(self, product_list: list[Product]):
        """
        Initializes the Store with a list of products.

        Parameter:
            product_list (list[Product]): A list of Product objects to
                                          initialize the store's inventory.
        """
        self.__products: list = product_list

    def add_product(self, product):
        """
        Adds a product to the store's inventory.

        Parameter:
            product (Product): The product to add to the store's inventory.
        """
        self.get_products().append(product)

    def remove_product(self, product):
        """
        Removes a product from the store's inventory.

        Parameter:
            product (Product): The product to remove from the store's inventory.
        """
        self.get_products().remove(product)

    def get_total_quantity(self) -> int:
        """
        Calculates the total quantity of all products in the store.

        Returns:
            int: The sum of quantities for all products in the store.
        """
        total_quantities: int = 0
        for product in self.get_products():
            total_quantities += product.get_quantity()
        return total_quantities

    def get_all_products(self) -> list[Product]:
        """
        Retrieves a list of all active products in the store.

        Returns:
            list[Product]: A list of active products in the store.
        """
        total_products: list[Product] = list()
        for product in self.get_products():
            if product.is_active():
                total_products.append(product)
        return total_products

    def order(self, shopping_list: list[tuple[Product, int]]) -> float:
        """
         Processes an order based on the provided shopping list, calculating
         the total cost.

         Parameter:
             shopping_list (list[tuple[Product, int]]):
                                A list of tuples where each tuple consists of
                                a Product and the quantity to be purchased.

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
        Validates the provided shopping list to ensure it meets quantity
        and order limits.

        Parameter:
            shopping_list (list[tuple[Product, int]]):
                                A list of tuples, each containing a Product
                                and the quantity to be ordered.

        Raises:
            ValueError: If any product quantity exceeds the available quantity
            or maximum order limit.
        """
        aggregated = defaultdict(int)

        for product, order in shopping_list:
            if not isinstance(product,
                              NonStockedProduct) and product.get_quantity() < order:
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
        Retrieves the store's product list.

        Returns:
            list[Product]: The list of products in the store's inventory.
        """
        return self.__products

    def set_products(self, products):
        """
        Sets the store's product list to a new list of products.

        Parameter:
            products (list[Product]): The new list of products to set.

        Raises:
            ValueError: If products is not a list or is empty.
        """
        if isinstance(products, list) and products:
            self.__products = products
        else:
            raise ValueError("Products must be a list of products")
