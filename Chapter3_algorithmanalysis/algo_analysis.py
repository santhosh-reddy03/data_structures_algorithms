import csv
import math

# R-3.1
"""
8n, 4n log n, 2n**2, n**3, 2**n functions graph on x = log n  and y = log(func)
"""
out_list = []

for i in range(2, 7):
    x = math.log(i)
    out_list.append(('8n', x, math.log(8*i)))
    out_list.append(('4nlog n', x, math.log(4 * i * x)))
    out_list.append(('2n**2', x, math.log(2*(i**2))))
    out_list.append(('n**3', x, math.log(i**3)))
    out_list.append(('2**n', x, math.log(2**i)))
out_list.sort(key=lambda ele: ele[0])

with open('out_put.csv', 'w', newline='') as csvfile:
    out_writer = csv.writer(csvfile, delimiter=',',
                            quotechar='|', quoting=csv.QUOTE_MINIMAL)
    out_writer.writerow(('function', 'x-value', 'y-value'))
    out_writer.writerows(out_list)


# R-3.2
"""
f(n) = 8nlog n
g(n) = 2n**2
find n where g(n) starts performing slower than f(n)
"""
num = 2
while True:
    f_func = 8*num * math.log(num, 2)
    g_func = 2*math.pow(num, 2)
    if g_func > f_func:
        print(num)
        break
    num += 1
