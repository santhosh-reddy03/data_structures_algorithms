import asyncio
import threading
from multiprocessing import Pool
import time

"""
in non asynchronous programs context switching happens in non-deterministic way when determined by os

in asynchronous programs, the application determines at what point context switching should happen
i.e context is switched only at pre-defined points in program
asyncio also scales well

callback oriented ones are difficult to maintain as the program gets bigger and bigger
asyncio eases this with using coroutines , than can be paused and executed at will
"""

"""
concurrency:
multiple thread of execution can be run on a single CPU core. only one thread is active at a time
threading module is used for concurrency
Parallelism:
multiple threads of execution can be run on multiple cores of the cpu at same time. each thread must have 
a separate set of resources to work
multiprocessing module can be used for this work
Asynchronous:
initiate a task and while waiting for the task to be finished we can do some other tasks
asyncio module is used for this
"""
# print(help(asyncio))


def s_func(*args):
    for i in args:
        time.sleep(0.2)
        print(i*i)
    print("square done")


def c_func(*args):
    for n in args:
        time.sleep(0.2)
        print(n*n*n)
    print("cube done")


t = threading.Thread(target=s_func, args=(5, 6, 7,))
t2 = threading.Thread(target=c_func, args=(5, 6, 7,))
# threading is limited by global interpreter lock(gil) of cpython which locks python interpreter and effectively only uses one thread
# so threading is less suited for asynchronous programming
# t.start()
# t2.start()
# t.join()
# t2.join()

po = Pool(5)
print(po.map(s_func, [1, 2, 3]))
print(po.starmap(s_func, [(1, 2), (2, 3)]))
# we can call start and join on process similar to thread, join waits for the completion of other process
# start will trigger the run method

"""
multiprocessing processes can be started in 3 ways
spawn
fork
forkserver
set_start_method() of multiprocessing is used to change the default method as all are not supported in each oses
and this method need to be called only once per program so it is kept inside mail block

spawn is default in windows and available for linux and it is slowest way of starting process and takes required params from parent 
process and creates new python interpreter for each child process

fork is available only in unix and it copies all the params from parent .
safe forking of multi threaded process is difficult

for forkserver a server process is created, for each new process the parent request the server to create child process
it is single threaded so os.fork() is safely done and child imports only required resources
available on unix-like platform
"""