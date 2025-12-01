# -------------------------------
# Constants in Python
# -------------------------------
# Python does not have real locked constants like some languages do.
# However, developers use CAPITAL LETTER names to mark a value as CONSTANT,
# meaning it shouldn't be changed casually.

PI = 3.14159
APP_VERSION = "1.0.0"
AUTHOR = "Jagriti"
MAX_USERS = 100

print("------- CONSTANT VALUES -------")
print("PI =", PI)
print("App Version =", APP_VERSION)
print("Author =", AUTHOR)
print("Maximum Allowed Users =", MAX_USERS)

# Constants are useful when the value is fixed,
# for example: mathematical values, configuration details, limits, etc.

# -------------------------------
# How constants are used
# -------------------------------

radius = 5

# Using PI in a calculation
circle_area = PI * (radius ** 2)
print("\nArea of Circle =", circle_area)

# -------------------------------
# Even though constants are meant to stay the same,
# Python will still allow changes (but it's not a good practice!)
# -------------------------------

print("\nTrying to modify PI... (Not Recommended)")

PI = 3.14  # This works, but developers avoid doing this.
print("Updated PI =", PI)  # This shows how Python treats constants like simple variables

# -------------------------------
# BEST PRACTICE:
# Never change constants once defined unless logically needed.
# Think of them as values written in permanent marker.
# -------------------------------

