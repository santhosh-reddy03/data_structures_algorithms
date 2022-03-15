from stacks import Empty


class ArrayQueue:

    DEFAULT_CAPACITY = 10

    def __init__(self):
        self._data = [None] * ArrayQueue.DEFAULT_CAPACITY
        self._f = 0  # front
        self._size = 0

    def __len__(self):
        return self._size

    def is_empty(self):
        return self._size == 0

    def first(self):
        if self.is_empty():
            raise Empty('Queue is empty')
        return self._data[self._f]

    def dequeue(self):
        if self.is_empty():
            raise Empty('Queue is empty')
        # to reduce or shrink the size when the queue is 1/4 of size do actual array
        if 0 < self._size < len(self._data)//4:
            self._resize(len(self._data)//2)
        answer = self._data[self._f]
        self._data[self._f] = None
        self._f = (self._f + 1) % len(self._data)
        self._size -= 1
        return answer

    def enqueue(self, e):
        if self._size == len(self._data):
            self._resize(2 * len(self._data))
        avail = (self._size + self._f) % len(self._data)
        self._size += 1
        self._data[avail] = e

    def _resize(self, new_capacity):
        old = self._data
        self._data = [None] * new_capacity
        walk = self._f
        for k in range(self._size):
            self._data[k] = old[walk]
            walk = (walk + 1) % len(old)
        self._f = 0
