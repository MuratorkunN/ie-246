import numpy as np

nest_list = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
    ]

arr = np.array(nest_list)
print(arr)
print(type(arr))

print (arr[0:2,0:2])

arr[0,0] = 100
print(arr)

arr1 = arr + 2
print(arr1)

arr1 = arr * 2
print(arr1)

arr1 = arr ** 2
print(arr1)

arr1 = arr + arr1
print (arr1)

print(arr)
print(np.sum(arr))
print(np.sum(arr, axis = 0))
print(np.sum(arr, axis = 1))

print(arr.T)
print(np.linalg.det(arr))

print (arr > 4)

print(arr[arr > 4])
