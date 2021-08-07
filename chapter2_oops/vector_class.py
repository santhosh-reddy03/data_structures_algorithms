"""
this contains all inbuilt class methods definitions
from R 2.9 to R 2.15
"""


class Vector:
    def __init__(self, d):
        # R 2.15
        if isinstance(d, int):
            self.__coords = [0]*d
        else:
            self.__coords = [0]*len(d)
            for j in range(len(d)):
                self[j] = d[j]

    def __len__(self):
        return len(self.__coords)

    def __getitem__(self, item):
        return self.__coords[item]

    def __setitem__(self, key, value):
        self.__coords[key] = value

    def __add__(self, other):
        if len(self) != len(other):
            raise ValueError("dimensions must be same")
        result = Vector(len(self))
        for j in range(len(self)):
            result[j] = self[j] + other[j]
        return result

    def __sub__(self, other):
        # R 2.9
        if len(self) != len(other):
            raise ValueError("dimensions must be same")
        result = Vector(len(self))
        for j in range(len(self)):
            result[j] = self[j] - other[j]
        return result

    def __eq__(self, other):
        return self.__coords == other.__coords

    def __ne__(self, other):
        """
        checks if self is equal to other using __eq__ method of the vector class and return a
        negation of it
        """
        return not self == other

    def __neg__(self):
        # R 2.10
        result = Vector(len(self))
        for j in range(len(self)):
            result[j] = -self[j]

    def __radd__(self, other):
        """
        R 2.11
        when the user is adding a list and vector, it execute list add method instead, as the vector add method doesnt come into action
        since the add will be invoked on list object, we provide a look around 'right add' method in vector class so that this generates new vector
        by referring the type of instances
        :param other:
        :return: should return vector sum of self and other
        """
        # always implement self in first when its radd, because it would go under recursion
        # as it would keep on calling radd if you are implementing other + self
        return self + other

    def __mul__(self, other):
        result = Vector(len(self))
        if isinstance(other, int):
            # R 2.12
            for j in range(len(self)):
                result[j] = self[j] * other
        elif isinstance(other, Vector):
            # R 2.14
            result = 0
            for j in range(len(self)):
                result += self[j]*other[j]
        return result

    def __rmul__(self, other):
        # R 2.13
        return self.__mul__(other)

    def __str__(self):
        return '< ' + str(self.__coords)[1:-1] + ' >'


if __name__ == '__main__':
    """
    to get main use ctrl+j and look for main 
    """
    # trail and testing
    a = Vector(3)
    for i in range(3):
        a[i] = 2*i
    print(a)
    print(a + [1, 2, 3])
    print([1, 2, 3] + a)
    # print(str([1, 23, 34])[1:-1])
    # print([1, 2, 3]*3)
    print("mul", a*4)
    print(Vector([1, 2, 3]))
