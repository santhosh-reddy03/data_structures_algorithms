"""a stack is an abstract data type"""
"""
the adapter design pattern
The adapter design pattern applies to any context where we effectively want to modify an existing class so that its methods 
match those of a related, but different, class or interface. One general way to apply the adapter pattern is to define a 
new class in such a way that it contains an instance of the existing class as a hidden field, and then to implement each 
method of the new class using methods of this hidden instance variable. By applying the adapter pattern in this way, 
we have created a new class that performs some of the same functions as an existing class, but repackaged in a more convenient way.

We can ADAPT python list class to implement stack
"""


class Empty(Exception):
    """Error attempting to access from an empty container"""
    pass


class ArrayStack:

    def __init__(self):
        self._inner = []

    def push(self, element):
        self._inner.append(element)

    def top(self):
        try:
            top = self._inner[-1]
            return top
        except IndexError:
            raise Empty('stack is empty')

    def pop(self):
        # try:
        #     self._inner.pop()
        # except IndexError:
        #     raise Empty
        if self.is_empty():
            raise Empty('stack is empty')
        return self._inner.pop()

    def __len__(self):
        return len(self._inner)

    def is_empty(self):
        # if len(self._inner) == 0:
        #     return True
        # return False
        return len(self._inner) == 0


s = ArrayStack()
s.push(5)
print(s.top())


def is_matched(expr):
    """returns true if all the delimiters are properly matched"""
    lefty = "({["
    righty = ")}]"
    a_s = ArrayStack()
    for c in expr:
        if c in lefty:
            a_s.push(c)
        elif c in righty:
            if a_s.is_empty():
                return False
            elif lefty.index(c) != righty.index(a_s.pop()):
                return False
    return a_s.is_empty()


def is_matched_html(raw):
    a_s = ArrayStack()
    j = raw.find('<')
    while j != -1:
        k = raw.find('>', j+1)
        if k == -1:
            return False
        tag = raw[j+1: k]
        if not tag.startswith('/'):
            a_s.push(tag)
        else:
            if a_s.is_empty():
                return False
            elif tag[1:] != a_s.pop():
                return False
        j = raw.find('<', k+1)
    return a_s.is_empty()
