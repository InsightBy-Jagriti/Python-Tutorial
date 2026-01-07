# Functions in Python
# -------------------
# A function is a block of code that runs only when it is called.

# -------------------------------------------------------
# 1. Simple function without parameters
# -------------------------------------------------------

def greet():
    print("Hello! Welcome to Python functions.")

greet()
greet()


# -------------------------------------------------------
# 2. Function with parameters
# -------------------------------------------------------

def greet_user(name):
    print("Hello", name)

greet_user("Jagriti")
greet_user("Alex")


# -------------------------------------------------------
# 3. Function with return value
# -------------------------------------------------------

def add_numbers(a, b):
    return a + b

result = add_numbers(10, 5)
print("Sum:", result)


# -------------------------------------------------------
# 4. Function with default parameter
# -------------------------------------------------------

def country_name(country="India"):
    print("Country:", country)

country_name()
country_name("Canada")


# -------------------------------------------------------
# 5. Function calling another function
# -------------------------------------------------------

def square(num):
    return num * num

def show_square(value):
    result = square(value)
    print("Square is:", result)

show_square(4)

print("\nFunction examples completed.")
