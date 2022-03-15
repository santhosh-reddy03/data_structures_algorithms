from queues import ArrayQueue
from queues import Empty


class ArrayDeque(ArrayQueue):
    """this is also available in python collections modules with bit of additional features"""

    # def __init__(self):
    #     super(ArrayQueue, self).__init__()

    def last(self):
        if self.is_empty():
            raise Empty('Deque is empty')
        back = (self._f + self._size - 1) % len(self._data)
        return self._data[back]

    def add_last(self, e):
        super().enqueue(e)

    def del_first(self):
        return super().dequeue()

    def add_first(self, e):
        if self._size == len(self._data):
            self._resize(2 * len(self._data))
        self._f = (self._f - 1) % len(self._data)
        self._data[self._f] = e
        self._size += 1

    def del_last(self):
        if self._size == 0:
            raise Empty('dq is empty')
        back = (self._f + self._size - 1) % len(self._data)
        answer = self._data[back]
        self._data[back] = None
        self._size -= 1
        return answer


dq = ArrayDeque()
dq.add_first(5)
print(dq.is_empty())
print(dq.del_last())
print(dq.is_empty())
