# Local and Global Scope in Python
# --------------------------------
# Scope defines where a variable can be accessed.

# Global variable
count = 10


def show_count():
    # Local variable
    local_count = 5
    print("Inside function:")
    print("Local count:", local_count)
    print("Global count:", count)


show_count()


def update_global():
    # Using global keyword to modify global variable
    global count
    count = count + 5
    print("\nGlobal count updated inside function:", count)


update_global()

print("\nGlobal count outside function:", count)


# Variable shadowing example
value = 100

def shadow_example():
    value = 50  # local variable shadows global one
    print("\nInside function value:", value)

shadow_example()
print("Outside function value:", value)
