class Product:
    """
    A class to represent a product with attributes for name, price, and quantity.
    Handles product activation, deactivation, buying, and basic inventory control.

    Private Instance Variables:
        __name (str): The name of the product.
        __price (float): The price of the product.
        __quantity (int): The available quantity of the product.
        __is_active (bool): Status of product availability.
    """

    def __init__(self, name: str, price: float, quantity: int):
        """
        Initializes a Product with a name, price, quantity, and sets it as active.

        Parameters:
            name (str): The name of the product.
            price (float): The price of the product.
            quantity (int): The available quantity of the product.
        """
        self.__name = name  # Private attribute, encapsulation
        self.__price = price
        self.__quantity = quantity
        self.__is_active = True

    def get_name(self):
        """Returns the product's name."""
        return self.__name

    def set_name(self, name: str):
        """
        Sets the product's name.

        Parameter:
            name (str): The new name for the product.

        Raises:
            ValueError: If name is not a non-empty string.
        """
        if isinstance(name, str) and name.strip():
            self.__name = name
        else:
            raise ValueError("Name must be a non-empty string")

    def get_price(self):
        """Returns the product's price."""
        return self.__price

    def set_price(self, price: float):
        """
        Sets the product's price.

        Parameter:
            price (float): The new price for the product.

        Raises:
            ValueError: If price is not a float or is negative.
        """
        if isinstance(price, float) and price >= 0.0:
            self.__price = price
        else:
            raise ValueError("Price must be a float")

    def get_quantity(self):
        """Returns the product's quantity."""
        return self.__quantity

    def set_quantity(self, quantity: int):
        """
        Sets the product's quantity. If quantity is zero, the product is deactivated.

        Parameter:
            quantity (int): The new quantity for the product.

        Raises:
            ValueError: If quantity is not a non-negative integer.
        """
        if isinstance(quantity, int) and quantity >= 0:
            self.__quantity = quantity
        else:
            raise ValueError("Quantity must be a int")

        if self.get_quantity() == 0:
            self.deactivate()

    def is_active(self):
        """Returns True if the product is active, otherwise False."""
        return self.__is_active

    def set_is_active(self, is_active: bool):
        """
        Sets the active status of the product.

        Parameter:
            is_active (bool): The active status of the product.

        Raises:
            ValueError: If is_active is not a boolean.
        """
        if isinstance(is_active, bool):
            self.__is_active = is_active
        else:
            raise ValueError("Is_active must be a bool")

    def activate(self):
        """Activates the product by setting is_active to True."""
        self.set_is_active(True)

    def deactivate(self):
        """Deactivates the product by setting is_active to False."""
        self.set_is_active(False)

    def __buy_product(self, given_quantity: int):
        """
        Private method that reduces the product's quantity by the given amount.

        Parameter:
            given_quantity (int): The quantity to reduce from stock.
        """
        self.set_quantity(self.get_quantity() - given_quantity)

    def buy(self, quantity: int) -> float:
        """
        Buys a given quantity of the product and updates inventory.

        Parameter:
            quantity (int): The quantity to purchase.

        Returns:
            float: The total cost of the purchase.

        Raises:
            ValueError: If quantity is invalid or exceeds stock.
        """
        try:
            # Buys a given quantity of the product.
            self.__buy_product(quantity)
        except ValueError as value_error:
            print(f"Value Error: {value_error}")
        else:
            return quantity * self.get_price()

    def show(self):
        """Returns a string representation of the product."""
        return self.__str__()

    def __str__(self):
        """
        Returns:
            str: A formatted string with the product's name, price, and quantity.
        """
        return (f"{self.get_name()}, Price: {self.get_price()},"
                f" Quantity: {self.get_quantity()}")

    def __eq__(self, other):
        """
        Checks equality with another Product based on name and price.

        Parameter:
            other (Product): Another product to compare.

        Returns:
            bool: True if the products are equal, otherwise False.
        """
        if isinstance(other, Product):
            return (self.get_name() == other.get_name()
                    and self.get_price() == other.get_price()
                    )
        return False
