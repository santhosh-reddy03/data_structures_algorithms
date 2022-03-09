import array
import sys
import ctypes
from time import time
# creating a compact array of type int, this format is only supported for native c data types
arr = array.array('i', [1, 2, 3])

# dynamic array
data = []
n = 30
for i in range(n):
    a = len(data)
    byte_size = sys.getsizeof(data)
    print('Length: {0:3d}; Size in bytes: {1:4d}'.format(a, byte_size))
    data.append(None)


class DynamicArray:
    """dynamic array implementation"""

    def __init__(self):
        self._n = 0
        self._capacity = 1
        self._A = self._make_array(self._capacity)

    @staticmethod
    def _make_array(c: int) -> any:
        """Returns new array of length c"""
        # ctypes is used for creating low level arrays
        return (c*ctypes.py_object)()

    def __len__(self) -> int:
        """Returns length of array"""
        return self._n

    def __getitem__(self, item: int) -> any:
        """Returns element at index item"""
        if not 0 <= item < self._n:
            raise IndexError("index out of range")
        return self._A[item]

    def append(self, obj: any) -> None:
        """add an object to end of array"""
        if self._n == self._capacity:
            self._resize(2*self._capacity)
        self._A[self._n] = obj
        self._n += 1

    def _resize(self, c: int) -> None:
        """Resize internal array to size c"""
        b = self._make_array(c)
        for k in self._A:
            b[k] = self._A[k]
        self._A = b
        self._capacity = c


def compute_average(num: int) -> float:
    """To measure the amortized cost for each append operation"""
    ar = []
    start = time()
    for _ in range(num):
        ar.append(None)
    end = time()
    return (end - start) / num


print(compute_average(10000))


class GameEntry:

    def __init__(self, name, score):
        self._name = name
        self._score = score

    def get_name(self):
        return self._name

    def get_score(self):
        return self._score

    def __str__(self):
        return "({0}, {1})".format(self._name, self._score)


class ScoreCard:
    """storing the high score of a game"""

    def __init__(self, capacity=10):
        self._board = [None]*capacity
        self._n = 0

    def __getitem__(self, item):
        return self._board[item]

    def __str__(self):
        return '\n'.join(str(self._board[entry]) for entry in range(self._n))

    # noinspection PyUnresolvedReferences
    def add_entry(self, entry):
        score = entry.get_score()
        good = self._n < len(self._board) or score > self._board[-1].get_score()

        if good:
            if self._n < len(self._board):
                self._n += 1
            j = self._n - 1
            while j > 0 and score > self._board[j].get_score():
                self._board[j] = self._board[j-1]
                j -= 1
            self._board[j] = entry


a = [3, 41, 2, 1, 8]
for i in range(len(a)):
    for m in range(len(a)):
        if a[i] < a[m]:
            temp = a[i]
            a[i] = a[m]
            a[m] = temp
print(a, "sorted")


class CeaserCipher:

    def __init__(self, shift):
        encoder = [''] * 26
        decoder = [''] * 26
        for k in range(26):
            encoder[k] = chr((k+shift) % 26 + ord('A'))
            decoder[k] = chr((k-shift) % 26 + ord('A'))
        self._forward = ''.join(encoder)
        self._backward = ''.join(decoder)

    def encrypt(self, message):
        return self._transform(message, self._forward)

    def decrypt(self, secret):
        return self._transform(secret, self._backward)

    @staticmethod
    def _transform(original, code):
        msg = list(original)
        for letter in range(len(msg)):
            if msg[letter].isupper():
                msg[letter] = code[ord(msg[letter]) - ord('A')]
        return ''.join(msg)


class TicTacToe:
    def __init__(self):
        self._board = [['']*3 for _ in range(3)]
        self._player = 'x'

    def move(self, x, y):
        if not 0 <= x <= 2 and not 0 <= y <= 2:
            raise ValueError("out of scope")
        if self._board[x][y] != '':
            raise ValueError("position already filled")
        if self.winner() is not None:
            raise ValueError("Game over")
        self._board[x][y] = self._player
        if self._player == 'x':
            self._player = 'o'
        else:
            self._player = 'x'

    def _win(self, mark):
        board = self._board
        return (mark == board[0][0] == board[0][1] == board[0][2] or
                mark == board[1][0] == board[1][1] == board[1][2] or
                mark == board[2][0] == board[2][1] == board[2][2] or
                mark == board[0][0] == board[1][0] == board[2][0] or
                mark == board[0][1] == board[1][1] == board[2][1] or
                mark == board[0][2] == board[1][2] == board[2][2] or
                mark == board[0][0] == board[1][1] == board[2][2] or
                mark == board[0][2] == board[1][1] == board[2][0])

    def winner(self):
        for mark in 'xo':
            if self._win(mark):
                return mark
        return None

    def __str__(self):
        rows = ['|'.join(r) for r in self._board]
        return '\n------\n'.join(rows)


if __name__ == '__main__':
    cipher = CeaserCipher(3)
    exp = "THE EAGLE IS IN PLAY; MEET AT JOE'S"
    coded = cipher.encrypt(exp)
    print(coded)
    answer = cipher.decrypt(coded)
    print("result", answer)
    tic = TicTacToe()
    print(tic)
