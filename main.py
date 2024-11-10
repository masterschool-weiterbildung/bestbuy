import products
import store
from products import Product
from store import Store

LIST_PRODUCTS = "1"
LIST_ITEMS = "2"
MAKE_ORDER = "3"
EXIT_APP = "4"


def print_menu() -> None:
    """Display the menu options for the user."""
    print("   Store Menu")
    print("   ----------")
    print("1. List all products in store")
    print("2. Show total amount in store")
    print("3. Make an order")
    print("4. Quit\n")


def list_products(best_buy: Store):
    list_products_for_order: dict = print_products(best_buy)

    select_options(call_menu(), best_buy)


def show_items_in_store(best_buy):
    print(f"Total of {best_buy.get_total_quantity()} items in store\n")

    select_options(call_menu(), best_buy)


def print_products(best_buy: Store) -> dict:
    list_products_for_order = dict()
    print("------")
    for count, product in enumerate(best_buy.get_all_products(), start=1):
        if product.is_active():
            print(f"{str(count)}. {product}")
            list_products_for_order[str(count)] = product
    print("------\n")
    return list_products_for_order


def make_order(best_buy: Store):
    dict_products_for_order: dict = print_products(best_buy)
    print("When you want to finish order, enter empty text.")
    list_products_for_order = []

    while True:
        try:
            input_product: str = input("Which product # do you want? ")
            input_quantity_order: str = input("What amount do you want? ")

            if input_product == "" or input_quantity_order == "":
                break

            if input_product not in dict_products_for_order.keys():
                raise ValueError()

            order = (
                dict_products_for_order[input_product],
                int(input_quantity_order))

            list_products_for_order.append(order)

            print("Product added to list!\n")
        except ValueError:
            print("Error adding product!\n")

    try:
        best_buy.validate_order(list_products_for_order)
    except ValueError as e:
        print(e)
    else:
        if list_products_for_order != "":
            print("********")
            print(
                f"Order made! Total payment: ${best_buy.order(list_products_for_order)}\n")

    select_options(call_menu(), best_buy)


def quit_app(best_buy: Store):
    pass


def select_options(user_choice: str, best_buy: Store) -> None:
    func_dict = {
        f"{LIST_PRODUCTS}":
            list_products,
        f"{LIST_ITEMS}":
            show_items_in_store,
        f"{MAKE_ORDER}":
            make_order,
        f"{EXIT_APP}":
            quit_app
    }

    option = return_options()

    if user_choice in option:
        func_dict[user_choice](best_buy)


def return_options():
    return [
        LIST_PRODUCTS, LIST_ITEMS, MAKE_ORDER, EXIT_APP
    ]


def call_menu() -> str:
    while True:
        try:
            print_menu()

            input_available_commands = input("Please choose a number: ")

            if input_available_commands == 4:
                break

            option = return_options()

            if input_available_commands not in option:
                raise ValueError()

        except ValueError:
            print("Invalid choice\n")
        else:
            break

    return input_available_commands


def start(best_buy: Store):
    select_options(call_menu(), best_buy)


def main():
    product_list = [
        products.Product("MacBook Air M2", price=1450, quantity=100),
        products.Product("Bose QuietComfort Earbuds", price=250,
                         quantity=500),
        products.Product("Google Pixel 7", price=500, quantity=250)
    ]

    best_buy = store.Store(product_list)

    start(best_buy)


if __name__ == '__main__':
    main()
