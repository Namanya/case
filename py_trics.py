products = [
    {'name': 'maize', 'price': 9000},
    {'name': 'mango', 'price': 8000},
    {'name': 'potato', 'price': 6000},
    {'name': 'orange', 'price': 5000}
]


def apply_discount():
    product_discount = int(input("Please enter discount out of 100 "))
    discount = product_discount/100
    for product in products:
        price = product['price'] * (1.0-discount)
        assert 0 <= price <= product['price']
        print(f"{product['name']} costs {price}")


class Indenter:
    def __init__(self):
        self.level = 0

    def __enter__(self):

        self.level += 1
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.level -= 1

    def print(self, text):
        print(' ' * self.level + text)













