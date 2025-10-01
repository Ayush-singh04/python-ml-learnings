import numpy as np

str = np.array([['cat', 'dog', 'bird'],
                ['fish', 'lion', 'tiger'],
                ['bear', 'wolf', 'fox']])


num = np.array([[1, 2, 3],
                [4, 5, 6],
                [7, 8, 9]])


# print(str[0])
# print(str[-1])
# print(str[0 ,1]) # gives specific item
# print(str[2 ,2]) # gives specific item
# print(num[1 ,0]) # gives specific item

# print(num[1 ,0] == 10) # checks specific item

# print(num > 5) # Returns bolean array 
# print(num[num > 5]) # Gives all the elements greater than 5


# Sclicing In Numpy

# print(str[0:1]) # Start : end (end will be excluded)
# print(str[0:1,2]) # Will Sclice the elements of first row
# print(str[0:1,2])

# print(np.take(num, [0, 2], axis=0)) # Take row no. 0 & 2 (If we don't write axis so it will only take the elements of row ,not a complete row)


# new_num = np.put(num, [0, 1], [99, 88]) # Modify specific indices

print(np.delete(num ,0 , axis=0)) # Deletes a particular given index or row/col