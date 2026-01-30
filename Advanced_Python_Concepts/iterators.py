# Iterators in Python

# --------------------------------------------------
# 1. Using built-in iterator
# --------------------------------------------------

numbers = [1, 2, 3, 4]

iterator = iter(numbers)

print("Using built-in iterator:")
print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))


# --------------------------------------------------
# 2. Creating a custom iterator
# --------------------------------------------------

class CountUp:
    def __init__(self, limit):
        self.num = 1
        self.limit = limit

    def __iter__(self):
        return self

    def __next__(self):
        if self.num <= self.limit:
            value = self.num
            self.num += 1
            return value
        else:
            raise StopIteration


print("\nCustom iterator output:")
counter = CountUp(5)

for number in counter:
    print(number)


print("\nIterator examples completed.")
