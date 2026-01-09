# return vs print in Python
# ------------------------
# print() is used to display output on the screen
# return is used to send a value back from a function


# Function using print
def show_sum(a, b):
    print("Sum using print:", a + b)


# Function using return
def get_sum(a, b):
    return a + b


# Calling function with print
show_sum(5, 3)

# Calling function with return
result = get_sum(5, 3)
print("Sum using return:", result)


# Difference in usage
# print() just shows the result
# return gives the result back so it can be reused

final_result = get_sum(10, 20) * 2
print("Using returned value in calculation:", final_result)
