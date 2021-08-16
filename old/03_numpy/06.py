import numpy as np 

data1 = [1, 2, 3, 4]
data2 = [
    [1, 2],
    [3, 4]
]

arr1 = np.array(data1)
arr2 = np.array(data2)

print(arr1, type(arr1))
print(arr2, type(arr2))
print(arr2.shape)