# random number from a range generator
from random import randint

number = randint(1, 100)

print(number)

# figlet

from pyfiglet import figlet_format

result = figlet_format("Hi", font="isometric2")

print(result)
