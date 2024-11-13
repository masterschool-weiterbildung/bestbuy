from abc import ABC, abstractmethod


class Promotion(ABC):
    """
    Abstract base class for promotions applied to products. Defines the
    structure for various promotion types.

    Attributes:
        __name (str): The name of the promotion.
        __percent (int): The percentage discount (default is 0)
                         for applicable promotions.
    """

    def __init__(self, name: str, percent=0):
        """
        Initializes the Promotion with a name and optional percentage discount.

        Parameters:
            name (str): The name of the promotion.
            percent (int, optional): The discount percentage. Defaults to 0.
        """
        self.__name = name  # Private attribute, encapsulation
        self.__percent = percent

    def get_name(self):
        """
        Retrieves the name of the promotion.

        Returns:
            str: The name of the promotion.
        """
        return self.__name

    def set_name(self, name: str):
        """
        Sets the name of the promotion.

        Parameter:
            name (str): The new name for the promotion.

        Raises:
            ValueError: If name is not a non-empty string.
        """
        if isinstance(name, str) and name.strip():
            self.__name = name
        else:
            raise ValueError("Name must be a non-empty string")

    def get_percent(self):
        """
        Retrieves the discount percentage of the promotion.

        Returns:
            int: The percentage discount.
        """
        return self.__percent

    def set_percent(self, percent: int):
        """
        Sets the discount percentage for the promotion.

        Parameter:
            percent (int): The discount percentage to set.

        Raises:
            ValueError: If percent is not a non-negative integer.
        """
        if isinstance(percent, int) and percent >= 0:
            self.__percent = percent
        else:
            raise ValueError("Percent must be a int")

    @abstractmethod
    def apply_promotion(self, product, quantity) -> float:
        """
        Abstract method to calculate the total price after applying the promotion.

        Parameter:
            product: The product to which the promotion is applied.
            quantity (int): The quantity of the product.

        Returns:
            float: The total price after applying the promotion.
        """
        pass


class SecondHalfPrice(Promotion):
    """
    Promotion where every second product is at half price.
    """

    def apply_promotion(self, product, quantity) -> float:
        """
        Applies the second-half-price promotion.

        Parameters:
            product: The product to which the promotion is applied.
            quantity (int): The quantity of the product.

        Returns:
            float: The total price after applying the second-half-price promotion.
        """
        half = quantity // 2
        return (((quantity - half) * product.get_price())
                + product.get_price() * .50 * half)


class ThirdOneFree(Promotion):
    """
    Promotion where every third product is free.
    """

    def apply_promotion(self, product, quantity) -> float:
        """
        Applies the third-one-free promotion.

        Parameters:
            product: The product to which the promotion is applied.
            quantity (int): The quantity of the product.

        Returns:
            float: The total price after applying the third-one-free promotion.
        """
        return product.get_price() * (quantity - (quantity // 3))


class PercentDiscount(Promotion):
    """
    Promotion that applies a percentage discount to the total price.
    """

    def apply_promotion(self, product, quantity) -> float:
        """
        Applies a percentage discount to the total price of the product.

        Parameters:
            product: The product to which the promotion is applied.
            quantity (int): The quantity of the product.

        Returns:
            float: The total price after applying the percentage discount.
        """
        gross_total = (product.get_price() * quantity)
        return gross_total - (gross_total * (self.get_percent() / 100))
