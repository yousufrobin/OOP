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
        self.__name = name # the underscore is added because of the @property decorator
        self.price = price
        self.quantity = quantity

        # storing an instance to the list immediately after the instance is executed.
        Item.all.append(self) # self means the instance which is created everytime

    @property
    # property decorator = read only attribute
    def name(self):
        # add underscore before name in self.name in the __init__ constructor
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value

    def calculate_total_price(self):
        return self.price * self.quantity

    def apply_discount(self):
        self.price = self.price * self.pay_rate # if we use Item.pay_rate, it will refer to the Class Attribute

    @classmethod
    def instantiate_from_csv(cls): # D:\OOP_FCC_Jim\items.csv
        with open('D:\OOP_FCC_Jim\items.csv', 'r') as f:
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