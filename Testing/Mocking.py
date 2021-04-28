# Mocking test
from unittest.mock import Mock

pizza = Mock()
print(pizza)
print(type(pizza))

pizza.size = "Large"
pizza.price = 19.99
pizza.toppings = ["Pepperoni", "Mushroom", "Sausage"]

print(pizza.size)
print(pizza.price)
print(pizza.toppings)

print(pizza.anything)
print(pizza.testMethod())


# Setting return value
mock = Mock(return_value = 25)

print(mock())

stuntman = Mock()
stuntman.jump_off_building.return_value = "My leg hurts"
stuntman.light_on_fire.return_value = "It burns!"

print(stuntman.jump_off_building())
print(stuntman.light_on_fire())