from store import Store
from products import Product


def main():
    product_list = [
        Product("MacBook Air M2", price=1450, quantity=100),
        Product("Bose QuietComfort Earbuds", price=250,
                         quantity=500),
        Product("Google Pixel 7", price=500, quantity=250),
        ]

    store = Store(product_list)
    products = store.get_all_products()
    print(store.get_total_quantity())
    print(store.order([(products[0], 10), (products[1], 15)]))
    products = store.get_all_products()
    print(store.get_total_quantity())


if __name__ == '__main__':
    main()