"""
Q1
three life critical software
# the software used in operation theatres
# software used in space maneuvers
# software used in military operations
"""

"""
Q2
software application in which adaptability can mean the difference between a prolonged lifetime of sales and bankruptcy
office365, social media
"""

"""
Q3
describe a text editor gui component and the method that it encapsulates
bold component, it encapsulates the change of text style.
"""


class Flower:
    """
    R-2.4
    """
    def __init__(self, name, petals, price):
        self.name = name
        self.petals = petals
        self.price = price

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if isinstance(name, str):
            self._name = name
        else:
            raise TypeError("name has to be string")

    @property
    def petals(self):
        return self._petals

    @petals.setter
    def petals(self, petals):
        if isinstance(petals, int):
            self._petals = petals
        else:
            raise TypeError("petals has to be integer")

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, price):
        if isinstance(price, float):
            self._price = price
        else:
            raise TypeError("price has to be a float value")


class CreditCard(object):
    """
    R-2.5 TO R-2.8
    """
    def __init__(self, customer, bank, account, limit, balance=0):
        self._customer = customer
        self._bank = bank
        self._account = account
        self._limit = limit
        self._balance = balance

    def get_customer(self):
        return self._customer

    def get_bank(self):
        return self._bank

    def get_account(self):
        return self._account

    def get_limit(self):
        return self._limit

    def get_balance(self):
        return self._balance

    def charge(self, price):
        if isinstance(price, (int, float)):
            if price + self._balance > self._limit:
                return False
            else:
                self._balance += price
                return self._balance
        else:
            raise TypeError("price cannot be other than number")

    def make_payment(self, amount):
        if isinstance(amount, (float, int)):
            if amount < 0:
                raise ValueError("amount can not be less than zero")
            else:
                self._balance -= amount
        else:
            raise TypeError("amount should be a number")


class Progression:
    def __init__(self, start=0):
        self._current = start

    def advance(self):
        self._current += 1

    def __next__(self):
        if self._current is None:
            raise StopIteration
        else:
            answer = self._current
            self.advance()
            return answer

    def __iter__(self):
        return self

    def print_progression(self, n):
        return ' '.join(str(next(self)) for _ in range(n))


class Fibonacci(Progression):

    def __init__(self, start, step):
        super(Progression, self).__init__(start)
        self.previous = step - start

    def advance(self):
        self.previous, self._current = self._current, self.previous + self._current

    def __getitem__(self, item):
        return self[item]


if __name__ == "__main__":

    """
    R 2.16
    range class is a arithmetic progression in which last = a+ (n-1)d
    by rearranging it we get (stop - start /d) + 1
    but when we do max(0, stop-start+step-1)//step this gives the number of factors of step that lies between start and stop
    which will be our length of range, the number of elements of range 
    """

    wallet = list()
    wallet.append(CreditCard('John', 'SBI', '5391 0376 9387 5309', 2500))
    wallet.append(CreditCard('Dave', 'SBI', '5391 0376 9387 1953', 3500))
    wallet.append(CreditCard('Scott', 'SBI', '5391 0376 9387 5309', 5000))

    for val in range(1, 58):
        wallet[0].charge(val)
        wallet[1].charge(2*val)
        wallet[2].charge(3*val)

    for c in range(3):
        print(wallet[c].get_customer())
        print(wallet[c].get_limit())
        print(wallet[c].get_balance(), end="\n\n")
