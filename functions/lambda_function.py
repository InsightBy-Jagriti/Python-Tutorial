# Lambda Functions in Python
# --------------------------
# A lambda function is a small anonymous function.
# It is written in a single line and used for simple operations.

# Normal function
def square(num):
    return num * num

print("Square using normal function:", square(4))


# Lambda function
square_lambda = lambda x: x * x
print("Square using lambda function:", square_lambda(4))


# Lambda with multiple arguments
add = lambda a, b: a + b
print("Addition using lambda:", add(5, 3))


# Lambda used inside another function
def apply_operation(func, value):
    return func(value)

result = apply_operation(lambda x: x * 3, 10)
print("Lambda inside function:", result)


# Lambda with conditional expression
check_even = lambda n: "Even" if n % 2 == 0 else "Odd"
print("Number check:", check_even(7))
