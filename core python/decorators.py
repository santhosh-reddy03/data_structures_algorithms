"""
use cases of decorators
memoization
trace recursion
"""


"""
currying is concept of transforming multiple parameters into individual nested unary function
unary function is the one that has single parameter
"""


def curry(f):
    argc = f.__code__.co_argcount
    f_args = []
    f_kwargs = {}

    def g(*args, **kwargs):
        nonlocal f_args, f_kwargs
        f_args += args
        f_kwargs.update(kwargs)
        if len(f_args) + len(f_kwargs) == argc:
            return f(*f_args, **f_kwargs)
        else:
            return g
    return g


@curry
def deco(msg_before, msg_after, f):
    # a decorator is a closure that takes function as parameter in higher order function and then perform
    # some operation and executes the function
    def g(*args, **kwargs):
        print("perform some operations", f.__name__)
        print(msg_before)
        result = f(*args, **kwargs)
        print(msg_after)
        # return f(*args, **kwargs)
        return result
    return g


# without currying
def deco2(msg_before, msg_after):
    def org_deco(f):
        def g(*args, **kwargs):
            print(msg_before, f.__name__)
            result = f(*args, **kwargs)
            print(msg_after, f.__name__)
            return result
        return g
    return org_deco


@deco("before", "after")
def func(x):
    return 2*x


# func = deco(func)
print(func.__name__)
print(func(2))


def memoize(f: any) -> any:
    memo = {}

    def memoized_func(n):
        # print(f.__name__, "inside emo")
        if n not in memo:
            memo[n] = f(n)
        return memo[n]
    return memoized_func

#
# fib = memoize(fib)
# print(fib(2))
# print(fib(30))


def trace(f):
    level = 1

    def helper(*arg):
        nonlocal level
        # the tracing happen because the fib will be referring to helper after being decorated
        print((level-1)*"  │",  "  ┌",  f.__name__,
              "(", ",".join(map(str, arg)), ")", sep="")
        level += 1
        result = f(*arg)
        level -= 1
        print((level-1)*"  │", "  └",  result, sep="")
        return result
    return helper


# we can also more clean way of calling decorator using @decorator name over function, can also multiple decorators
# to use params we have to do currying of the decorator so that we can pass params separately without issues
# the below is possible only because of currying
@memoize
@trace
def fib(n):
    # print("inside fib")
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        # bad recursion though
        return fib(n-1) + fib(n-2)


# fib = trace(fib)
print(fib(4))
