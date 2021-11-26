import sys

print(sys.getrecursionlimit())

# to change recursion limit use
# sys.setrecursionlimit(10)


def binary_search(series, n, low, high):
    """
    binary search algorithm example of linear search as it initiates a single recursion each time
    :param series: sorted series
    :param n: can be any value to be searched in series
    :param low: can be any index where the search begin
    :param high: can be any index where the search ends
    :return: either position or the not found
    """
    mid = (low + high)//2
    if series[mid] == n:
        return mid
    elif low == high:
        return "value not found"
    elif series[mid] > n:
        return binary_search(series, n, low, mid-1)
    elif series[mid] < n:
        return binary_search(series, n, mid+1, high)


print(binary_search([1, 2, 3, 4], 1, 0, 3))


def reverse_f(series, start, stop):
    if start < stop - 1:
        series[start], series[stop-1] = series[stop], series[start]
        return reverse_f(series, start + 1, stop - 1)


def power(x, n):
    if n == 0:
        return 1
    else:
        partial = power(x, n//2)
        result = partial * partial
        if n % 2 == 1:
            result *= result
        return result


# bianry recursion
def binary_recuruion_sum(series, start, stop):
    # here the space occupied is log(n) as the input reduces by half each time but the run time is O(n) = 2n - 1
    # as each function invokes two other functions
    # having constant operations
    if start > stop:
        return 0
    elif start == stop - 1:
        return series[start]
    else:
        mid = (start + stop)//2
        return binary_recuruion_sum(series, start, mid) + binary_recuruion_sum(series, mid, stop)
