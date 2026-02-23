# Вектор-рядок

import pandas as pd
import numpy as np

v_row = np.array([[1, 2, 3, 4]])
print(f"Вектор-рядок shape: {v_row.shape}")
print(v_row)

# Транспонуємо у вектор-стовпець
v_col = v_row.T
print(f"Вектор-стовпець shape: {v_col.shape}")
print(v_col)


# Вектор-рядок shape: (1, 4)
# [[1 2 3 4]]

# Вектор-стовпець shape: (4, 1)
# [[1]
#  [2]
#  [3]
#  [4]]
