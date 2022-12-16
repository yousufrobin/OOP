import csv


class Item:
    pay_rate = 0.8
    all = []

    def __init__(self, name: str, price: float, quantity=0):
        # we used quantity=0 to pass a default value
        # because of this default value(quantity=0),
        # we don't need to pass the value for quantity while creating an object
        # but if we pass a value, the default value will be overwritten


        # running validation for the received parameters
        assert price >= 0, f"the price {price} is not greater than or equal to zero"
        assert quantity >= 0, f"the quantity {quantity} is not greater than or equal to zero"

        # assign to self object
        self.name = name
        self.price = price
        self.quantity = quantity

        # storing an instance to the list immediately after the instance is executed.
        Item.all.append(self) # self means the instance which is created everytime

    def calculate_total_price(self):
        return self.price * self.quantity

    def apply_discount(self):
        self.price = self.price * self.pay_rate # if we use Item.pay_rate, it will refer to the Class Attribute

    @classmethod
    def instantiate_from_csv(cls):
        with open('items.csv', 'r') as f:
            reader = csv.DictReader(f)
            items = list(reader)

        for item in items:
            Item(
                name=item.get('name'),
                price=float(item.get('price')),
                quantity=int(item.get('quantity'))
            )


    # staticmethod is like a regular function that receives parameters.
    # notice that the parameter color is different to other class-function or method

    @staticmethod
    def check_integer(num):
        # when the num parameter is a float with point zero or point some other number,
        # it will go through the if statement. if statement will check whether it is point zero or not
        # if it is point zero, the is_integer() function will return it True
        # if it is not point zero but point some other number, the is_integer() function will return False
        # note that is_integer() itself is a function which check whether the float is with point zero or not
        if isinstance(num, float):
            return num.is_integer()
        elif isinstance(num, int):
            return True
        else:
            return False

    # when we want to print the whole class, it will be printed in an unknown manner
    #  But after using __repr__ magic method, the whole class will be printed as determined inside __repr__
    #  that means the following method will represent the whole class in following way
    def __repr__(self):
        # return f"Item('{self.name}', {self.price}, {self.quantity})" class name was hardcoded
        # now class name is dynamic
        return f"{self.__class__.__name__}('{self.name}', {self.price}, {self.quantity})"

class Phone(Item):

    def __init__(self, name: str, price: float, quantity=0, broken_phones = 1):
        super().__init__(
            name, price, quantity
        )

        # running validation for the received parameters
        assert broken_phones >= 0, f"the broken phone {broken_phones} is not greater than or equal to zero"

        # assign to self object
        self.broken_phone = broken_phones


# item1 = Item("Phone", 100)
# item2 = Item("Laptop", 1000, 3)
# print(item2.calculate_total_price())

# if we need some attributes for an instance
# but we dont want the attributes to be in the constructor(__init__)
# item2.has_numpad = False
# item2.has_keyboard_backlight = True
# print(item2.has_numpad, item2.has_keyboard_backlight)

# print(Item.pay_rate)
# print(Item1.pay_rate)
# print(Item2.pay_rate)

# print(Item.__dict__) # all the attributes for class level
# print(item1.__dict__) # all the attributes for instance level
# print(item2.__dict__)# all the attributes for instance level



# item1.apply_discount()
# print(item1.price)
# how to use Class Attribute without over-writing it
# item2 = Item("Laptop", 1000, 3)
# item2.pay_rate = 0.7
# item2.apply_discount()
# print(item2.price)

# # we are going to instantiate the following instances from the items.csv file
# item1 = Item("Phone", 100, 1)
# item2 = Item("Laptop", 1000, 3)
# item3 = Item("Cable", 10, 5)
# item4 = Item("Mouse", 50, 5)
# item5 = Item("Keyboard", 75, 5)
# print(Item.all)
# for i in Item.all:
#     print(i.price)


# Item.instantiate_from_csv()
# print(Item.all)

# print(Item.check_integer(7))

phone1 = Phone("Bashtol", 500, 5, 1)
print(phone1.calculate_total_price())
phone2 = Phone("Bashtol", 700, 5, 1)

print(Phone.all)
print(Item.all)
