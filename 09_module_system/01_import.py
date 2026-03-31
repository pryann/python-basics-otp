# import module
# import math

# print(math.pi)
# print(math.sin(90))

# import whole module, not need to use math.
# from math import *

# import only what you need
import random
from math import pi, sin

print(pi)
print(sin(90))

num = random.randint(1, 100)
print(num)

numbers = [1, 2, 3, 4, 5]
random.shuffle(numbers)
print(numbers)

print(random.choice(numbers))
