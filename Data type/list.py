# List Example in Python

# A list stores multiple values in one place.
# Items can be changed, added, or removed anytime.

fruits = ["apple", "banana", "mango", "orange"]
print("Original List:", fruits)

# Accessing items by index
print("First fruit:", fruits[0])
print("Last fruit:", fruits[-1])

# Changing an item
fruits[1] = "grapes"
print("After changing second item:", fruits)

# Adding new items
fruits.append("papaya")        # add at end
fruits.insert(1, "kiwi")       # add at specific position
print("After adding new fruits:", fruits)

# Removing items
fruits.remove("mango")         # removes by value
popped_item = fruits.pop()     # removes last item
print("Removed item:", popped_item)
print("List after removals:", fruits)

# Slicing a list
print("First 3 items:", fruits[:3])

# Looping through list
print("\nLooping through list:")
for fruit in fruits:
    print(fruit)

# Checking length
print("\nTotal items:", len(fruits))
