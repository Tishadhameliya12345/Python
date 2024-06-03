# simple program of NumPy
# Crete array in numpy
import numpy as np

arr = np.array([1, 2, 3, 4, 5])
print(arr)
print(type(arr))

# Crete 0-D array
import numpy as np

arr1 = np.array(39)
print(arr1)
print()

# 1-D Array
arr2 = np.array([1,3,5,7,9])
print(arr2)
print()

# 2-D array
arr3 = np.array([[1,2,3],[4,5,6],[7,8,9]])
print(arr3)
print()

# 3-D array
arr4 = np.array([[[1,2,3],[4,5,6]],[[7,8,9],[1,2,3]]])
print(arr4)
print()

#Access Array Elements
print(arr[0])
print(arr[1] + arr[4])
print()

# Access 2-D array
print(arr3[0,2])
print()

# Access 3-D array
print(arr4[0,1,2])
print()

# Nagative Indexing
print(arr[-1])
print()

# Slicing arrays
arr5 = np.array([1,2,3,4,5,6,7,8,9,10])
print(arr5[3:5])
print(arr5[:6])
print(arr5[5:])
print(arr5[-3:-1]) # Nagetive Slicing
print()

# Using steps
print(arr5[1:10:2])
print()

# check datatype in array
print(arr.dtype)
print()

# crete array with a define datatype
import numpy as np

arr = np.array([1, 2, 3, 4], dtype='S')

print(arr)
print(arr.dtype)
print()

# Copy 
import numpy as np

arr = np.array([1, 2, 3, 4, 5])
x = arr.copy()
arr[0] = 42

print(arr)
print(x)

# View
import numpy as np

arr = np.array([1, 2, 3, 4, 5])
x = arr.view()
arr[0] = 42

print(arr)
print(x)

# shape of array
# returns a tuple with each index having the number of corresponding elements.
print(arr4.shape)
print()

# Reshaping array
a1 = np.array([1,2,3,4,5,6,7,8,9,10,11,12])
new_arr = a1.reshape(4,3)
print(new_arr)
print()

# Iterating Arrays
# 1-D array
import numpy as np

arr = np.array([1, 2, 3])

for x in arr:
  print(x)
print()

# 2-D array
import numpy as np

arr = np.array([[1,2,3],[4,5,6],[7,8,9]])

for x in arr:
    print(x)

print()

for x in arr:
    for y in x:
        print(y)
        
print()

#3-D array
import numpy as np

arr = np.array([[[1,2,3],[4,5,6]],[[7,8,9],[10,11,12]]])

for x in arr:
    print(x)
print()

for x in arr:
    for y in x:
        for z in y:
            print(z)
            
print()

# Enumerated Iteration Using ndenumerate()
#1-D
import numpy as np

arr = np.array([1, 2, 3])

for idx, x in np.ndenumerate(arr):
  print(idx, x)
  
print()

#2-D
import numpy as np

arr = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])

for idx, x in np.ndenumerate(arr):
  print(idx, x)

print()
  
# Joining NumPy Arrays
# using concatenate()
import numpy as np

arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])

arr = np.concatenate((arr1, arr2))

print(arr)
print()

#2-D
import numpy as np

arr1 = np.array([[1, 2], [3, 4]])
arr2 = np.array([[5, 6], [7, 8]])

arr = np.concatenate((arr1, arr2), axis=1)

print(arr)
print()

# join using stack()
import numpy as np

arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])

arr = np.stack((arr1, arr2), axis=1)

print(arr)
print()

#Splitting NumPy Arrays
import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6])

newarr = np.array_split(arr, 3)

print(newarr)
print()

# Searching Arrays using where() method
import numpy as np

arr = np.array([1, 2, 3, 4, 5, 4, 4])

x = np.where(arr == 4)

print(x)
print()

# Search Sorted
import numpy as np

arr = np.array([6, 7, 8, 9])

x = np.searchsorted(arr, 7)

print(x)
print()