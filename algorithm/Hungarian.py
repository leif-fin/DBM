import numpy as np
from scipy.optimize import linear_sum_assignment

# Define the cost matrix
cost_matrix = np.array([[4, 1, 3], [2, 0, 5], [3, 2, 2]])

# Using the Hungarian algorithm
row_ind, col_ind = linear_sum_assignment(cost_matrix)


print("Distribution results：")
print("Work -> Worker")
for r, c in zip(row_ind, col_ind):
    print(f"{r} -> {c}")

print("Minimum total cost：", cost_matrix[row_ind, col_ind].sum())
