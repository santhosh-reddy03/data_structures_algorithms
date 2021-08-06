import random


def is_multiple(n, m):
    if n % m == 0:
        return True
    else:
        return False


def is_even(n):
    even_list = (0, 2, 4, 6, 8)
    if int(str(n)[-1]) in even_list:
        return True
    else:
        return False


def minmax(data):
    data = sorted(data)
    return data[0], data[-1]


def sum_squares(n):
    s = 0
    for i in range(n):
        s += i*i
    return s


def sum_squares1(n):
    return sum([i*i for i in range(n)])


def sum_odd(n):
    return sum([i*i for i in range(n) if i % 2 != 0])


def sum_odd1(n):
    s = 0
    for i in range(n):
        if i % 2 != 0:
            s += i*i
    return s


# k is negative index in a string
# j = abs(k) - 1


def choice(r):
    return random.randrange(r)


print(list(range(50, 90, 10)))
print(list(range(8, -10, -2)))
print([2**i for i in range(9)])
# print(random.choice(list(random.randrange(1, 10, 1))))
print(choice(5))
