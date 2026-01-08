# *args and **kwargs example

# Using *args
def add_numbers(*nums):
    total = 0
    for n in nums:
        total += n
    return total

print("Sum:", add_numbers(1, 2, 3, 4))


# Using **kwargs
def student_details(**info):
    for key, value in info.items():
        print(key, ":", value)

student_details(name="Jagriti", age=22, course="Python")
