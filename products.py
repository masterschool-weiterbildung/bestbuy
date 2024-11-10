class Product:
    def __init__(self, name: str, price: float, quantity: int):
        self.__name = name  # Private attribute, encapsulation
        self.__price = price
        self.__quantity = quantity
        self.__is_active = True

    def get_name(self):
        return self.__name

    def set_name(self, name: str):
        if isinstance(name, str) and name.strip():
            self.__name = name
        else:
            raise ValueError("Name must be a non-empty string")

    def get_price(self):
        return self.__price

    def set_price(self, price: float):
        if isinstance(price, float) and price >= 0.0:
            self.__price = price
        else:
            raise ValueError("Price must be a float")

    def get_quantity(self):
        return self.__quantity

    def set_quantity(self, quantity: int):
        if isinstance(quantity, int) and quantity >= 0:
            self.__quantity = quantity
        else:
            raise ValueError("Quantity must be a int")

        if self.get_quantity() == 0:
            self.deactivate()

    def is_active(self):
        return self.__is_active

    def set_is_active(self, is_active: bool):
        if isinstance(is_active, bool):
            self.__is_active = is_active
        else:
            raise ValueError("Is_active must be a bool")

    def activate(self):
        self.set_is_active(True)

    def deactivate(self):
        self.set_is_active(False)

    def __buy_product(self, given_quantity: int):
        self.set_quantity(self.get_quantity() - given_quantity)

    def buy(self, quantity: int):
        try:
            # Buys a given quantity of the product.
            self.__buy_product(quantity)
        except ValueError as e:
            print(f"Value Error: {e}")
        except Exception as e:
            print(f"An error occurred: {e}")
        else:
            return quantity * self.get_price()

    def show(self):
        return self.__str__()

    def __str__(self):
        return (f"{self.get_name()}, Price: {self.get_price()},"
                f" Quantity: {self.get_quantity()}")

    def __eq__(self, other):
        if isinstance(other, Product):
            return (self.get_name() == other.get_name()
                    and self.get_price() == other.get_price()
                    )
        return False
