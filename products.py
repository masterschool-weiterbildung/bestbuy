from promotions import Promotion


class Product:
    """
    Represents a product with basic details such as name, price, quantity, and promotion.

    Attributes:
        __name (str): The name of the product.
        __price (float): The price of the product.
        __quantity (int): The quantity available in stock.
        __is_active (bool): Status indicating if the product is active.
        __promotion (Promotion): An optional promotion associated with the product.
    """

    def __init__(self, name: str, price: float, quantity: int):
        """
        Initializes a Product with a name, price, and quantity.

        Parameters:
            name (str): The name of the product.
            price (float): The price of the product.
            quantity (int): The available quantity of the product.
        """
        self.__promotion: Promotion | None = None
        self.__name: str = name  # Private attribute, encapsulation
        self.__price: float = price
        self.__quantity: int = quantity
        self.__is_active: bool = True

    def get_promotion(self):
        """
        Retrieves the promotion associated with the product.

        Returns:
            Promotion: The promotion applied to the product.
        """
        return self.__promotion

    def set_promotion(self, promotion: Promotion):
        """
        Sets the promotion for the product.

        Parameter:
            promotion (Promotion): The promotion to set.

        Raises:
            ValueError: If promotion is not a valid Promotion instance.
        """
        if isinstance(promotion, Promotion) and promotion:
            self.__promotion = promotion
        else:
            raise ValueError("Promotion must be a non-empty")

    def get_name(self):
        """
        Retrieves the name of the product.

        Returns:
            str: The name of the product.
        """
        """Returns the product's name."""
        return self.__name

    def set_name(self, name: str):
        """
        Sets the name of the product.

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
        """
        Retrieves the price of the product.

        Returns:
            float: The price of the product.
        """
        return self.__price

    def set_price(self, price: float):
        """
        Sets the price of the product.

        Parameter:
            price (float): The new price of the product.

        Raises:
            ValueError: If price is not a float or is negative.
        """
        if isinstance(price, float) and price >= 0.0:
            self.__price = price
        else:
            raise ValueError("Price must be a float")

    def get_quantity(self):
        """
        Retrieves the quantity of the product.

        Returns:
            int: The quantity available in stock.
        """
        return self.__quantity

    def set_quantity(self, quantity: int):
        """
        Sets the quantity of the product.

        Parameter:
            quantity (int): The new quantity to set.

        Raises:
            ValueError: If quantity is not an integer or is negative.
        """
        if isinstance(quantity, int) and quantity >= 0:
            self.__quantity = quantity
        else:
            raise ValueError("Quantity must be a int")

        if self.get_quantity() == 0:  # Deactivate if Zero (0)
            self.deactivate()

    def is_active(self):
        """
        Checks if the product is active.

        Returns:
            bool: True if the product is active, False otherwise.
        """
        return self.__is_active

    def set_is_active(self, is_active: bool):
        """
        Sets the active status of the product.

        Parameter:
            is_active (bool): The active status to set.

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
        Decreases the quantity by the given amount.

        Parameter:
            given_quantity (int): The quantity to deduct.
        """
        self.set_quantity(self.get_quantity() - given_quantity)

    def buy(self, quantity: int) -> float:
        """
        Processes the purchase of a given quantity of the product.

        Parameter:
            quantity (int): The quantity to purchase.

        Returns:
            float: The total price after applying promotions, if any.
        """
        try:
            # Buys a given quantity of the product. Skip if NonStockedProduct
            if not isinstance(self, NonStockedProduct):
                self.__buy_product(quantity)
        except ValueError as value_error:
            print(f"Value Error: {value_error}")
        else:
            if self.get_promotion():
                return self.get_promotion().apply_promotion(self, quantity)
            return quantity * self.get_price()

    def show(self):
        """
        Returns a string representation of the product details.

        Returns:
            str: The product details.
        """
        return self.__str__()

    def __str__(self):
        """
        Formats the product's details for display.

        Returns:
            str: The formatted product details.
        """
        if self.get_promotion():
            return (f"{self.get_name()}, Price: {self.get_price()},"
                    f" Quantity: {self.get_quantity()},"
                    f" Promotion: {self.get_promotion().get_name()}")

        elif isinstance(self, LimitedProduct):
            if self.get_promotion():
                return (f"{self.get_name()}, Price: {self.get_price()},"
                        f" Quantity: {self.get_quantity()},"
                        f" Maximum: {self.get_maximum()},"
                        f" Promotion: {self.get_promotion().get_name()}")
            else:
                return (f"{self.get_name()}, Price: {self.get_price()},"
                        f" Quantity: {self.get_quantity()},"
                        f" Maximum: {self.get_maximum()}")

        elif isinstance(self, NonStockedProduct):
            if self.get_promotion():
                return (f"{self.get_name()}, Price: {self.get_price()},"
                        f" Promotion: {self.get_promotion().get_name()}")
            else:
                return (f"{self.get_name()}, Price: {self.get_price()},"
                        f" Quantity: {self.get_quantity()}")
        else:
            return (f"{self.get_name()}, Price: {self.get_price()},"
                    f" Quantity: {self.get_quantity()}")

    def __eq__(self, other):
        """
        Checks if this product is equal to another product.

        Parameter:
            other (Product): The other product to compare.

        Returns:
            bool: True if both products are equal, False otherwise.
        """
        if isinstance(other, Product):
            return (self.get_name() == other.get_name()
                    and self.get_price() == other.get_price()
                    )
        return False

    def __hash__(self):
        """Returns a hash of the product's name."""
        return hash(self.__name)

    def __gt__(self, other):
        """
        Checks if this product's price is greater than another product's price.

        Parameter:
            other (Product): The other product to compare.

        Returns:
            bool: True if this product's price is greater, False otherwise.
        """
        return self.get_price() > other.get_price()

    def __lt__(self, other):
        """
        Checks if this product's price is less than another product's price.

        Parameter:
            other (Product): The other product to compare.

        Returns:
            bool: True if this product's price is less, False otherwise.
        """
        return other.get_price() < self.get_price()

    def __contains__(self, item):
        """
         Checks if this product exists in a collection.

         Parameter:
             item: The collection to check.

         Returns:
             bool: True if the product is in the collection, False otherwise.
         """
        return self in item

    def __add__(self, other):
        """
        Adds the price of this product to another product's price.

        Parameter:
            other (Product): The other product to add.

        Returns:
            float: The sum of the two product prices.
        """
        return self.get_price() + other.get_price()


class NonStockedProduct(Product):
    """
    A product that is non-stocked and has no quantity limit.
    """

    def __init__(self, name: str, price: float):
        """
        Initializes a NonStockedProduct with a name and price, setting quantity to 0.

        Parameters:
            name (str): The name of the non-stocked product.
            price (float): The price of the non-stocked product.
        """
        self.__name = name  # Private attribute, encapsulation
        self.__price = price
        super().__init__(self.__name, self.__price,
                         0)


class LimitedProduct(Product):
    """
    A product that has a maximum order limit.

    Attributes:
        __maximum (int): The maximum order quantity.
    """

    def __init__(self, name: str, price: float, quantity: int, maximum: int):
        """
        Initializes a LimitedProduct with a maximum order limit.

        Parameters:
            name (str): The name of the limited product.
            price (float): The price of the limited product.
            quantity (int): The available quantity in stock.
            maximum (int): The maximum order quantity allowed.
        """
        self.__name = name  # Private attribute, encapsulation
        self.__price = price
        self.__quantity = quantity
        self.__maximum = maximum
        super().__init__(self.__name, self.__price,
                         self.__quantity)

    def get_maximum(self):
        """
        Retrieves the maximum order limit.

        Returns:
            int: The maximum order quantity.
        """
        return self.__maximum

    def set_maximum(self, maximum: int):
        """
        Sets the maximum quantity per order

        Parameter:
            maximum (int): The maximum quantity per order

        Raises:
            ValueError: If maximum is not int or empty
        """
        if isinstance(maximum, int) and maximum >= 0:
            self.__maximum = maximum
        else:
            raise ValueError("Maximum must be a int")

    def __hash__(self):
        return hash(self.__name)
