# -*- coding: utf-8 -*-
"""Assignment#2(Numpy Fundamentals.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1MmtaDVeHFIy1OJLuQgmytxS_u3Xf4_kE

# Numpy_Assignment_2::

## Question:1

### Convert a 1D array to a 2D array with 2 rows?

#### Desired output::

array([[0, 1, 2, 3, 4],
        [5, 6, 7, 8, 9]])
"""

import numpy as np
x = np.arange(10).reshape(2,5)
x

"""## Question:2

###  How to stack two arrays vertically?

#### Desired Output::

array([[0, 1, 2, 3, 4],
        [5, 6, 7, 8, 9],
       [1, 1, 1, 1, 1],
       [1, 1, 1, 1, 1]])
"""

x = np.arange(10).reshape(2,5)
y = np.ones(10, dtype='int').reshape(2,5)
z = np.vstack((x,y))
z

"""## Question:3

### How to stack two arrays horizontally?

#### Desired Output::

array([[0, 1, 2, 3, 4, 1, 1, 1, 1, 1],
       [5, 6, 7, 8, 9, 1, 1, 1, 1, 1]])
"""

z = np.hstack((x,y))
z

"""## Question:4

### How to convert an array of arrays into a flat 1d array?

#### Desired Output::

array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
"""

z = x.flatten()
z

"""## Question:5

### How to Convert higher dimension into one dimension?

#### Desired Output::

array([ 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14])
"""

a = np.arange(15).reshape(5,3)
b = a.flatten()
b

"""## Question:6

### Convert one dimension to higher dimension?

#### Desired Output::

array([[ 0, 1, 2],
[ 3, 4, 5],
[ 6, 7, 8],
[ 9, 10, 11],
[12, 13, 14]])
"""

c = b.reshape(5,3)
c

"""## Question:7

### Create 5x5 an array and find the square of an array?
"""

d = np.random.random((5,5))
np.square(d)

"""## Question:8

### Create 5x6 an array and find the mean?
"""

e = np.random.random((5,6))
np.mean(e)

"""## Question:9

### Find the standard deviation of the previous array in Q8?
"""

np.std(e)

"""## Question:10

### Find the median of the previous array in Q8?
"""

np.median(e)

"""## Question:11

### Find the transpose of the previous array in Q8?
"""

np.transpose(e)

"""## Question:12

### Create a 4x4 an array and find the sum of diagonal elements?
"""

f = np.random.random((4,4))
diag = np.diagonal(f)
np.sum(diag)

"""## Question:13

### Find the determinant of the previous array in Q12?
"""

np.linalg.det(f)

"""## Question:14

### Find the 5th and 95th percentile of an array?
"""

a = np.arange(100)
p = np.percentile(a, 5)
q = np.percentile(a, 95)
print(p)
q

"""## Question:15

### How to find if a given array has any null values?
"""

c = [[1,2,3],[np.nan,2,2]] 
np.isnan(c)

