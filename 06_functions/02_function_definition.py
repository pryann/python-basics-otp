def greetings(name):
    return f"Hello {name}!"


print(greetings("Alice"))
print(greetings("John"))
print(greetings("Jane"))


def calculate_gross_price(net_price: int | float, tax_rate: float = 0.27) -> float:
    return net_price * (1 + tax_rate)


print(calculate_gross_price(100))
print(calculate_gross_price(100.99, 0.05))
# print(calculate_gross_price(tax_rate=0.05, net_price=100))


def calculate_total_price(basket: list[int | float]) -> float:
    total_price = 0
    for item in basket:
        total_price += item
    return total_price


basket = [100, 121, 99]

print(calculate_total_price(basket))
