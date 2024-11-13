import products
import promotions
import store
from util import order_product, validate_order_util, print_products

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


def list_products(best_buy: store.Store):
    """
    List all active products available in the store.

    Parameter:
        best_buy (Store): The store instance with products.
    """
    print_products(best_buy)

    select_options(call_menu(), best_buy)


def show_items_in_store(best_buy):
    """
    Display the total quantity of items available in the store.

    Parameter:
        best_buy (Store): The store instance with products.
    """
    print(f"Total of {best_buy.get_total_quantity()} items in store\n")

    select_options(call_menu(), best_buy)


def make_order(best_buy: store.Store):
    list_products_for_order = order_product(best_buy)

    best_buy = validate_order_util(best_buy, list_products_for_order)

    select_options(call_menu(), best_buy)


def quit_app(best_buy: store.Store):
    """
    Function to exit application
    """
    best_buy = []


def select_options(user_choice: str, best_buy: store.Store) -> None:
    """
    Execute the function based on the user's menu selection.

    Parameters:
        user_choice (str): The menu option chosen by the user.
        best_buy (Store): The store instance with products.
    """
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


def return_options() -> list:
    """
    Returns the list of valid menu options.

    Returns:
        list: A list of menu options as strings.
    """
    return [
        LIST_PRODUCTS, LIST_ITEMS, MAKE_ORDER, EXIT_APP
    ]


def call_menu() -> str:
    """
    Display the menu and get user input for menu selection.

    Returns:
        str: The user's chosen menu option.
    """
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
            print()
        else:
            break

    return input_available_commands


def start(best_buy: store.Store):
    """
    Start the menu selection loop for the store.

    Parameter:
        best_buy (Store): The store instance with products.
    """
    select_options(call_menu(), best_buy)


def main():
    """
    Main function to initialize products and start the store application.
    """
    # setup initial stock of inventory
    product_list = [
        products.Product("MacBook Air M2", price=1450, quantity=100),
        products.Product("Bose QuietComfort Earbuds", price=250,
                         quantity=500),
        products.Product("Google Pixel 7", price=500, quantity=250),
        products.NonStockedProduct("Windows License", price=125),
        products.LimitedProduct("Shipping", price=10, quantity=250, maximum=1)
    ]

    # Create promotion catalog
    second_half_price = promotions.SecondHalfPrice("Second Half price!")
    third_one_free = promotions.ThirdOneFree("Third One Free!")
    thirty_percent = promotions.PercentDiscount("30% off!", percent=30)

    # Add promotions to products
    product_list[0].set_promotion(second_half_price)
    product_list[1].set_promotion(third_one_free)
    product_list[3].set_promotion(thirty_percent)

    best_buy = store.Store(product_list)

    start(best_buy)


if __name__ == '__main__':
    main()
