"""
performance_comparison.py
-------------------------
Compare performance of Python lists vs NumPy arrays.
"""

import numpy as np
import time

# Create large datasets
N = 10_000_000
py_list = list(range(N))
np_array = np.arange(N)

# 1️⃣ Pure Python
start = time.time()
sum_py = sum(x * 2 for x in py_list)
end = time.time()
print(f"Python time: {end - start:.4f}s")

# 2️⃣ NumPy
start = time.time()
sum_np = np.sum(np_array * 2)
end = time.time()
print(f"NumPy time: {end - start:.4f}s")
