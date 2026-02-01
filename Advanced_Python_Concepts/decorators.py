# Decorators in Python

# --------------------------------------------------
# 1. Basic decorator example
# --------------------------------------------------

def simple_decorator(func):
    def wrapper():
        print("Before function execution")
        func()
        print("After function execution")
    return wrapper


@simple_decorator
def say_hello():
    print("Hello!")

say_hello()


# --------------------------------------------------
# 2. Decorator with arguments
# --------------------------------------------------

def smart_divide(func):
    def wrapper(a, b):
        if b == 0:
            print("Cannot divide by zero")
            return
        return func(a, b)
    return wrapper


@smart_divide
def divide(a, b):
    return a / b

print("\nDivision result:", divide(10, 2))
divide(10, 0)


# --------------------------------------------------
# 3. Multiple decorators
# --------------------------------------------------

def uppercase(func):
    def wrapper():
        return func().upper()
    return wrapper

def exclaim(func):
    def wrapper():
        return func() + "!!!"
    return wrapper


@uppercase
@exclaim
def greet():
    return "hello"

print("\nMultiple decorators result:", greet())


print("\nDecorator examples completed.")
