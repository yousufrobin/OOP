from item import Item


item1 = Item("Dell", 1000, 5)
print(item1.name)
# after setting @property decorator we need to set @setter decorator to change an attribute in an instance
item1.name = "HP"
print(item1.name)


