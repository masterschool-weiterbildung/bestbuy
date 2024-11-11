from store import Store


def print_products(best_buy: Store) -> dict:
    """
    Display all active products and return a dictionary for ordering.

    Parameter:
        best_buy (Store): The store instance with products.

    Returns:
        dict: A dictionary mapping product numbers to product instances.
    """
    list_products_for_order = {}
    print("------")
    for count, product in enumerate(best_buy.get_all_products(), start=1):
        if product.is_active():
            print(f"{str(count)}. {product}")
            list_products_for_order[str(count)] = product
    print("------\n")
    return list_products_for_order


def order_product(best_buy):
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
    return list_products_for_order


def validate_order_util(best_buy, list_products_for_order):
    try:
        best_buy.validate_order(list_products_for_order)
    except ValueError as validate_order:
        print(validate_order)
    else:
        if list_products_for_order:
            print("********")
            print(
                f"Order made! Total payment: ${best_buy.order(list_products_for_order)}\n")
        else:
            print("\n")

    return best_buy
