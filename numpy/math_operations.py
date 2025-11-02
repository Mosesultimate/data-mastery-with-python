##--Explore NumPy arithmetic, aggregation, and broadcasting.

import numpy as np

data = np.array([[2, 4, 6], [1, 3, 5,], [7, 9, 11]])

# 1️⃣ Arithmetic Operations
print("Add 10:\n", data + 10)
print("Multiply by 2:\n", data * 2)
print("Square Root:\n", np.sqrt(data))

# 2️⃣ Aggregation Functions
print("Sum:", np.sum(data))
print("\nMean:", data.mean())
print("Sum by Row:", data.sum(axis=1))
print("Sum by Column:", data.sum(axis = 0))
print("Max Value:", np.max(data))

# 3️⃣ Broadcasting example
x = np.array([1, 2, 3])
y = np.array([[10], [20], [30]])
print("\nBroadcasting result:\n", x + y)
