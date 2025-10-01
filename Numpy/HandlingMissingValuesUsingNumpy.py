import numpy as np

arr = np.array([[1,2,3],
               [4,np.nan,6],
               [np.nan,np.nan,9]])

# print(np.isnan(arr)) # To find the Nan(Not a Number) value

# print(np.nan_to_num(arr)) # To fill the Nan Value with number(default it will fill 0)

print(np.nan_to_num(arr , nan=100)) # To fill a specific value at Nan place
