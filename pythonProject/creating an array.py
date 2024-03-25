# from numpy import *
# arr = logspace(1,40,5)
# print('%.2f' %arr[4])
# print(arr)
#
#
# from numpy import *
# arr = ones(5,int)
# print(arr)
#
# from numpy import *
# arr = zeros(5,int)
# print(arr)

# from numpy import *
# arr = array([1,2,3,4,5])
# arr = arr +5
# print(arr)
#
# from numpy import *
# arr1 = array([1,2,3,4,5])
# arr2 = array([6,7,8,9,3])
# arr3 = arr1 + arr2
# print(arr3)
#
# from numpy import *
# arr = array([1,2,3,4,5])
# print((arr))
#
# from numpy import *
# arr1 = array([1,2,3,4,5])
# arr1 = arr.view()
# print(arr1)
# print(id(arr))
# print(id(arr1))
#
# # shallow copy
# from numpy import *
# arr1 = array([1,2,3,4,5])
# arr1 = arr.view()
#
# arr1[1] = 7
# print(arr1)
# print(arr)
#
# # deep copy
# from numpy import *
# arr1 = array([1,2,3,4,5])
# arr1 = arr.copy()
#
# arr1[1] = 8
# print(arr1)
# print(arr)
#

# Multi dimensional array

# from numpy import *
#
# arr = array([
#           [1,2,3,6,8,9],
#           [4,5,6,5,6,7]
#              ])
#
# print(arr.ndim)
# print(arr.shape)
# print(arr.flatten())
# print(arr.ndim)
# print(arr.reshape(2,2,3))


#matrix
# from numpy import *
# m1 = matrix('1,2,3 ;2,3,4;3,4,5')
# m2 = matrix('1,2,3 ;2,3,4;3,4,5')
# m3 = m1 * m2;
# print(m3)
# print(m1.__mul__(m2))
