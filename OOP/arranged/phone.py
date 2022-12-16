from arranged.item import Item


class Phone(Item):

    def __init__(self, name: str, price: float, quantity=0, broken_phones = 1):
        super().__init__(
            name, price, quantity
        )

        # running validation for the received parameters
        assert broken_phones >= 0, f"the broken phone {broken_phones} is not greater than or equal to zero"

        # assign to self object
        self.broken_phone = broken_phones