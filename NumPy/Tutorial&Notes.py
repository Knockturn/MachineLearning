import numpy as np

'''
CREATING One Dimensional ARRAYS IN NUMPY 3 easy ways:
'''
' import list as array '
a = np.array([2,3,4])

' arrange from 1 to 12 in a space of 2 '
b = np.arange(1,12,2)

' Linear spacing from 1.0 to 12.0 and 6 elements (evenly spaced) '
c = np.linspace(1,12,6)

print("array: ", a, type(a))
print("arrange: ", b, type(b))
print("linspace: ", c, type(c))
print("\n")
'''
Reshape One Dimensional Array Into Two Dimensional ARRAYS IN NUMPY:
    3 lists, 2 in each.
'''
print("linspace, reshaped: ", c.reshape(3,2))
print("\n")

'''
Get the size of the array.
Doesnt care if two or one dimenional. Rehsaped linspace is also 6.
'''
print("Size of linspace array: ", c.size)
print("\n")

'''
Get the shape of an array:
'''
print("Shape of linspace array: ", c.shape)
print("Shape of two dimensional linspace array: ", c.reshape(3,2).shape)
print("\n")

'''
Get the datatype
'''
print("Datatype of linspace: ", c.dtype)
print("\n")

'''
How much data in bytes does each element take: (float64 = 64 bits = 8 bytes)
'''
print("linspace each item byte size: ", c.itemsize)
print("\n")

'''
() and [] example - creating an array (2D)
'''
d = np.array([(1.5,2,3), (4,5,6)])
print("2D array: ", d)
print("\n")

'''
Compare each item in array to see if it is less than 4
'''
print("Is any in 2D array < 4: ", d < 4)
print("\n")
'''
Multiply each item in the array by 3
'''
print("2D array multiplied by 3: ", d * 3)
print("\n")
'''
In order to store the new values on D do the following:
'''
d *= 3
print("See new saved values on 2D array: ", d)
print("\n")
'''
ADVANCED CREATIONS
'''
e = np.zeros((3,2))
print("2D array filled with 0: ", e)
f = np.ones((2,3))
print ("2D array filled with 1: ", f)
print("\n")
'''
You can also pass in the dataType that you want
'''
g = np.array([2,3,4], dtype=np.int16)

print("Array: ",g," Type: ", g.dtype)
print("\n")
'''
You can also create a random array. "random.random" gives values from 0 to 1
'''
h = np.random.random((2,3))
print("Random array: ", h)
print("\n")
'''
You can also set print options if you dont want so many decimals to show.
These settings are kept now until changed again. "suppress" = (scientific notions)
'''
np.set_printoptions(precision=2, suppress=True)
print("Random array(rounded): ", h)
print("\n")
'''
Random integers in the array.
From 0 to 10, 5 elements
'''
i = np.random.randint(0, 10, 5)
print("Random integers: ",i)
print("\n")
'''
Get the sum of i
'''
print("sum of i: ", i.sum())
print("\n")
'''
Extract data values from i
'''
print("Minimum value in i: ",i.min())
print("Maximum value in i: ", i.max())
print("Average of i: ", i.mean())
print("Variants of i: ", i.var())
print("Standard deviation of i: ", i.std())
print("\n")
'''
create a new list, reshape it and get the axis of 1 (the pairs)
axis is like rows or columns in the array.
These can be done for multiple types of the array (sum, std etc.)
'''
j = np.random.randint(1,10,6)
j = j.reshape(3,2)
print("j array: ", j)
print("Sum, axis 1 of j: ",j.sum(axis=1))
print("Sum, axis 0 of j: ",j.sum(axis=0))
print("Standard Deviation, axis 1 of j: ",j.std(axis=0))
print("\n")

'''
Work with CSV files in an easy way
loadtxt doesnt handle exceptions very well like missing values, random chars, letters.
For better usage: genfromtxt (will handle exceptions better)
'''
data = np.loadtxt("data.txt", dtype=np.uint8, delimiter=",", skiprows=1)
print("data.txt csv type: ", data)
print("\n")
'''
Random shuffle on range
'''
k = np.arange(10)
print("array - k: ", k)
print("shuffle the array - k: ", np.random.shuffle(k))
print("\tDEBUG: shuffle command should NOT be None. It does not seem to work.")
print("random choice on item in k: ", np.random.choice(k))