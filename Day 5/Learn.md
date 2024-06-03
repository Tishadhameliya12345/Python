# NumPy

NumPy is a Python library.
NumPy is used for working with arrays.
NumPy is short for "Numerical Python".

# What is NumPy?

NumPy is a Python library used for working with arrays.
It also has functions for working in domain of linear algebra, fourier transform, and matrices.
NumPy was created in 2005 by Travis Oliphant. It is an open source project and you can use it freely.
NumPy stands for Numerical Python.

# Installation of NumPy
write code in cmd:
        pip install numpy

# Import NumPy 
use Import statment

    Import numpy

# NumPy as np
NumPy is usually imported under the np alias.
        import numpy as np

# check numpy version
    print(np.__version__)

# Numpy Datatype
Below is a list of all data types in NumPy and the characters used to represent them.

i - integer
b - boolean
u - unsigned integer
f - float
c - complex float
m - timedelta
M - datetime
O - object
S - string
U - unicode string
V - fixed chunk of memory for other type ( void )

# Iterating Arrays

Iterating means going through elements one by one.
As we deal with multi-dimensional arrays in numpy, we can do this using basic for loop of python.
If we iterate on a 1-D array it will go through each element one by one.

# Splitting NumPy Arrays

Splitting is reverse operation of Joining.
Joining merges multiple arrays into one and Splitting breaks one array into multiple.
We use array_split() for splitting arrays, we pass it the array we want to split and the number of splits.

# Search Sorted
There is a method called searchsorted() which performs a binary search in the array, and returns the index where the specified value would be inserted to maintain the search order.