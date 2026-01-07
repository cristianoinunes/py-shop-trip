import datetime
from typing import Dict


class Shop:
    def __init__(
        self,
        name: str,
        location: list[float],
        products: Dict[str, float],
    ) -> None:
        self.name = name
        self.location = location
        self.products = products

    def products_cost(self, cart: Dict[str, int]) -> float:
        return sum(
            self.products[product] * quantity
            for product, quantity in cart.items()
        )

    @staticmethod
    def _format_price(value: float) -> float | int:
        if value.is_integer():
            return int(value)
        return value

    def print_receipt(
        self,
        customer_name: str,
        cart: Dict[str, int],
    ) -> None:
        now = datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        print(f"\nDate: {now}")
        print(f"Thanks, {customer_name}, for your purchase!")
        print("You have bought:")

        for product, quantity in cart.items():
            price = self.products[product] * quantity
            price = self._format_price(price)
            print(f"{quantity} {product}s for {price} dollars")

        total = self._format_price(self.products_cost(cart))
        print(f"Total cost is {total} dollars")
        print("See you again!\n")
