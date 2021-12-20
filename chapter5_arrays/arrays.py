import array
import sys
# creating a compact array of type int, this format is only supported for native c data types
arr = array.array('i', [1, 2, 3])

# dynamic array
data = []
n = 30
for i in range(n):
    a = len(data)
    b = sys.getsizeof(data)
    print('Length: {0:3d}; Size in bytes: {1:4d}'.format(a, b))
    data.append(None)
