from products import Product


class Store:
    def __init__(self, product_list: list[Product]):
        self.__products: list = product_list

    def add_product(self, product):
        self.get_products().append(product)

    def remove_product(self, product):
        self.get_products().remove(product)

    def get_total_quantity(self) -> int:
        total_quantities: int = 0
        for product in self.get_products():
            total_quantities += product.get_quantity()
        return total_quantities

    def get_all_products(self) -> list[Product]:
        total_products: Product = []
        for product in self.get_products():
            if product.is_active():
                total_products.append(product)
        return total_products

    def order(self, shopping_list: list[tuple[Product, int]]) -> float:
        total_cost: float = 0.0
        for product, order in shopping_list:
            total_cost += product.get_price() * order
            product.buy(order)
        return total_cost

    def validate_order(self, shopping_list: list[tuple[Product, int]]) -> None:
        for product, order in shopping_list:
            if product.get_quantity() < order:
                raise ValueError(
                    "Error while making order! Quantity larger than what exists\n")

    def get_products(self):
        return self.__products

    def set_products(self, products):
        if isinstance(products, list) and products:
            self.__products = products
        else:
            raise ValueError("Products must be a list of products")
