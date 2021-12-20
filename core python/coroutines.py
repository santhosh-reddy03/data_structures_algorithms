
# coroutines are mainly used for data processing pipelines


def deco(func):
    def wrapper(*args, **kwargs):
        co = func(*args, **kwargs)
        next(co)
        return co
    return wrapper


@deco
def coroutine_one(task=0):
    try:
        while True:
            name = yield
            print("task", task, name)
            task += 1
    except GeneratorExit:
        print("end of coroutine last task", task)


# coroutines are initialized by called next(coroutine)
# and data is sent to function by using send
# we can eliminate calling next by using decorator
c = coroutine_one()
# next(c)
c.send('first')
c.send('second')
c.close()
