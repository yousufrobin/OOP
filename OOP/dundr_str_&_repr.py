class CustomizedInteger:
    def __init__(self, integer):
        self.integer = integer

    def __str__(self):
        if self.integer == 4:
            return "four"

    def __repr__(self):
        return f"interger {self.integer}"

int1 = CustomizedInteger(4)

print(int1)
print(CustomizedInteger(4))