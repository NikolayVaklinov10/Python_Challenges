"""
**shape**

The shape tool gives a tuple of array dimensions and can be used to change the dimensions of an array.
(a). Using shape to get array dimensions

import numpy

my__1D_aaray = numpy.array([1, 2, 3, 4, 5])
print my_1D_array.shape #(5,) -> 5 rows and 0 columns

my__2D_array = numpy.array([[1,2],[3,4], [6,5]])
print my_2D_aaray.shape    #(3,2) -> 3 rows and 2 columns

(b). Using shape to change array dimensions

import numpy

change_array = numpy.array([1,2,3,4,5,6])
change_array.shape = (3,2)
print(change_array)

# Output
[[1 2]
[3 4]
[5 6]]


reshape

The reshape tool gives a new shape to an array without
changing its data. It creates a new array and does not modify
the origin array itself.

import numpy

my_array = numpy.array([1,2,3,4,5,6])
print numpy.reshape(my_array, (3,2))


# Output
[[1 2]
[3 4]
[5 6]]

Task







"""

import numpy as np

# my solution
my_array = np.array([1,2,3,4,5,6,7,8,9])
my_array.shape = (3,3)
print(my_array)

# solution 2
print(np.array(input().split(), int).reshape(3,3))


# solution 3

import numpy as np
a=np.array(list(map(int,input().split())))
a.shape=(3,3)
print(a)


# solution 4

import numpy

print (numpy.fromstring(input(), dtype=int, sep=" ").reshape(3,3))

























