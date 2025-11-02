"""
correlations.py
----------------
Compute correlations between product prices, discounts, and sales.
"""

import numpy as np
import pandas as pd

# Simulated dataset
np.random.seed(42)
data = pd.DataFrame({
    "price": np.random.uniform(100, 1000, 50),
    "discount": np.random.uniform(0, 0.5, 50),
    "quantity_sold": np.random.randint(10, 500, 50)
})

print("Sample data:\n", data.head(), "\n")

# Compute correlations
corr = data.corr(numeric_only=True)
print("Correlation Matrix:\n", corr)

# Interpret example
print("Insights:")
if corr.loc["price", "quantity_sold"] < 0:
    print("- Higher prices may reduce quantity sold.")
if corr.loc["discount", "quantity_sold"] > 0:
    print("- Discounts may boost sales.")
