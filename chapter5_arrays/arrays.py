import array
import sys
import ctypes
# creating a compact array of type int, this format is only supported for native c data types
arr = array.array('i', [1, 2, 3])

# dynamic array
data = []
n = 30
for i in range(n):
    a = len(data)
    byte_size = sys.getsizeof(data)
    print('Length: {0:3d}; Size in bytes: {1:4d}'.format(a, byte_size))
    data.append(None)


class DynamicArray:
    """dynamic array implementation"""

    def __init__(self):
        self._n = 0
        self._capacity = 1
        self._A = self._make_array(self._capacity)

    @staticmethod
    def _make_array(c) -> any:
        return (c*ctypes.py_object)()

    def __len__(self) -> int:
        return self._n

    def __getitem__(self, item) -> any:
        if not 0 <= item < self._n:
            raise IndexError("index out of range")
        return self._A[item]

    def append(self, obj) -> None:
        if self._n == self._capacity:
            self._resize(2*self._capacity)
        self._A[self._n] = obj
        self._n += 1

    def _resize(self, c) -> None:
        b = self._make_array(c)
        for k in self._A:
            b[k] = self._A[k]
        self._A = b
        self._capacity = c
