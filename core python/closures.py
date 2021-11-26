
def high_f(x, y):
    print(x + y)
    # a higher order function is a function that returns other function

    def low_g(z):
        print("inside g", z)
        return z
    return low_g


h = high_f(1, 2)
print(h.__name__)
print(h.__closure__)
i = h(3)


def func_f(x, y):
    # a closure is a function returned by other function, that uses the local variables of the parent function
    def func_g(z):
        return x + y + z
    return func_g


t = func_f(1, 2)
# t is closure
print(t.__name__)
print(t.__closure__)
print(t.__code__.co_freevars)
print(t(3))
