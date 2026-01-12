# Using Built-in and User-Defined Modules

# -----------------------------------------------------
# 1. Using built-in modules
# -----------------------------------------------------

import math
import random
from datetime import date

print("Square root of 25:", math.sqrt(25))
print("Random number:", random.randint(1, 10))
print("Today's date:", date.today())


# -----------------------------------------------------
# 2. Using a user-defined module
# -----------------------------------------------------
# Assume we have a file 'my_module.py' in the same folder
# with a function:  def greet(name): print("Hello", name)

import my_module  # your own module

my_module.greet("Jagriti")


# -----------------------------------------------------
# 3. Importing with alias
# -----------------------------------------------------

import math as m

print("Cosine of 0:", m.cos(0))
