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


class ArithmeticProgression(Progression):

    def __init__(self, common_difference, first=0):
        super().__init__(first)
        self._increment = common_difference

    def advance(self):
        self._current += self._increment


class Fibonacci(Progression):

    def __init__(self, first=0, second=1):
        super().__init__(first)
        self.previous = second - first

    def advance(self):
        self.previous, self._current = self._current, self.previous + self._current

    def __getitem__(self, item):
        answer = Fibonacci(self._current, self._current + self.previous)
        for _ in range(0, item):
            next(answer)
        return answer._current


if __name__ == "__main__":

    """
    R 2.16
    range class is a arithmetic progression in which last = a+ (n-1)d
    by rearranging it we get (stop - start /d) + 1
    but when we do max(0, stop-start+step-1)//step this gives the number of factors of step that lies between start and stop
    which will be our length of range, the number of elements of range 
    
    R 2.20
    multilevel inheritance where B inherits A, C inherits B, D inherits C and so on.. other words "deep inheritance"
    this will create more and more redundancy as we go down the inheritance, as there might be lot of methods that the lower classes 
    would be inheriting without actual needs and increased complexity of handling 
    https://stackoverflow.com/questions/28721913/efficiency-disadvantages-of-having-very-deep-and-very-shallow-inheritance-trees
      
    R 2.21
    "shallow inheritance" the same data of R 2.20 can be used for this as well 
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

    ob = Fibonacci(2, 2)
    print('R 2.18', ob[8])
    ap = ArithmeticProgression(128)
    # using ap last term formula l = a + (n-1)d
    print('R 2.19', ((2**63)//128) + 1, '= 72057594037927937')
