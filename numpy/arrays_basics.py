## arrays_basics.py
## Intro to NumPy arrays: creation, indexing, reshaping.

import numpy as np


# 1️⃣ Create arrays
arr = np.array([10, 20, 30 ,40, 50,])
print("Array:", arr)

# 2️⃣ Inspect
print("Shape:", arr.shape)
print("Data type:", arr.dtype)
print("Dimensions:", arr.ndim)

# 3️⃣ Reshape a 1D array into 2D
arr_reshaped = np.arange(1, 13).reshape(3, 4)
print("\nReshaped Array:\n", arr_reshaped)

# 4️⃣ Slicing
print("\nFirst Row:", arr_reshaped[0])
print("Element(Second Row, Third Column):", arr_reshaped[1, 2])

# 5️⃣ Boolean indexing
mask = arr_reshaped > 5
print("\nMask (Values>5):\n", mask)
print("Filtered Values (Values>5):", arr_reshaped[mask])
