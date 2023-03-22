import random
import miniprojects.simple.my_module as my_module
random_integer = random.randint(1, 10)
print(random_integer)

print(my_module.pi)  # we have imported another python file

random_float = random.random()
print(random_float)

print(random_float*5)
