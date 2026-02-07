# NumPy Advanced Concepts

import numpy as np

# --------------------------------------------------
# 1. Advanced Indexing & Slicing
# --------------------------------------------------

arr = np.array([10, 20, 30, 40, 50])

print("Original array:", arr)
print("Indexing:", arr[2])
print("Slicing:", arr[1:4])


# --------------------------------------------------
# 2. Boolean Masking
# --------------------------------------------------

numbers = np.array([5, 10, 15, 20, 25])

mask = numbers > 15
print("\nBoolean mask:", mask)
print("Filtered values:", numbers[mask])


# --------------------------------------------------
# 3. Reshaping Arrays
# --------------------------------------------------

matrix = np.array([1, 2, 3, 4, 5, 6])
reshaped = matrix.reshape(2, 3)

print("\nReshaped array:\n", reshaped)


# --------------------------------------------------
# 4. Broadcasting
# --------------------------------------------------

arr1 = np.array([1, 2, 3])
arr2 = np.array([[10], [20], [30]])

result = arr1 + arr2
print("\nBroadcasting result:\n", result)


# --------------------------------------------------
# 5. Vectorized Operations
# --------------------------------------------------

values = np.array([1, 2, 3, 4])

print("\nVectorized multiplication:", values * values)
print("Vectorized addition:", values + 5)


# --------------------------------------------------
# 6. Axis-based Operations
# --------------------------------------------------

data = np.array([[1, 2, 3],
                 [4, 5, 6]])

print("\nSum of all elements:", np.sum(data))
print("Row-wise sum:", np.sum(data, axis=1))
print("Column-wise sum:", np.sum(data, axis=0))


# --------------------------------------------------
# 7. Stacking Arrays
# --------------------------------------------------

a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

print("\nVertical stack:\n", np.vstack((a, b)))
print("Horizontal stack:", np.hstack((a, b)))


# --------------------------------------------------
# 8. Splitting Arrays
# --------------------------------------------------

big_array = np.array([1, 2, 3, 4, 5, 6])

split_arrays = np.split(big_array, 3)
print("\nSplitted arrays:", split_arrays)


print("\nNumPy advanced examples completed.")

