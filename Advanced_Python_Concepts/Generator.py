# Generators in Python

# --------------------------------------------------
# 1. Simple generator example
# --------------------------------------------------

def count_up(limit):
    num = 1
    while num <= limit:
        yield num
        num += 1

print("Counting using generator:")
for number in count_up(5):
    print(number)


# --------------------------------------------------
# 2. Generator with next()
# --------------------------------------------------

gen = count_up(3)

print("\nUsing next():")
print(next(gen))
print(next(gen))
print(next(gen))


# --------------------------------------------------
# 3. Generator expression
# --------------------------------------------------

squares = (x * x for x in range(1, 6))

print("\nSquares using generator expression:")
for sq in squares:
    print(sq)


print("\nGenerator examples completed.")
