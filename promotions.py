from abc import ABC, abstractmethod


class Promotion(ABC):
    def __init__(self, name: str, percent=0):
        self.__name = name  # Private attribute, encapsulation
        self.__percent = percent

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

    def get_percent(self):
        """Returns the product's quantity."""
        return self.__percent

    def set_percent(self, percent: int):
        if isinstance(percent, int) and percent >= 0:
            self.__percent = percent
        else:
            raise ValueError("Percent must be a int")

    @abstractmethod
    def apply_promotion(self, product, quantity) -> float:
        pass


class SecondHalfPrice(Promotion):
    def apply_promotion(self, product, quantity) -> float:
        return (((quantity - (quantity // 2)) * product.get_price())
                + product.get_price() * .50 * (quantity // 2))


class ThirdOneFree(Promotion):
    def apply_promotion(self, product, quantity) -> float:
        return product.get_price() * (quantity - (quantity // 3))


class PercentDiscount(Promotion):
    def apply_promotion(self, product, quantity) -> float:
        gross_total = (product.get_price() * quantity)
        return gross_total - (gross_total * (self.get_percent() / 100))
