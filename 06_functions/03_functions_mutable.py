# def add_item_to_basket(item: str, basket: list[str] = []) -> list[str]:
def add_item_to_basket(item: str, basket: list[str] | None = None) -> list[str]:
    # better if you crete a copy
    if basket is None:
        basket = []
    basket.append(item)
    return basket


my_basket = []
# print(add_item_to_basket("apple", my_basket))
# print(add_item_to_basket("banana", my_basket))
# print(add_item_to_basket("orange", my_basket))
print(add_item_to_basket("apple"))
print(add_item_to_basket("banana"))
print(add_item_to_basket("orange"))
