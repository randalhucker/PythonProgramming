## Lab 12: Generators and Iterators ##

import doctest
_author_ = "Randy Hucker"
_credits_ = ["Me, myself, and I, and Ch 11 of PYTHON PROGRAMMING"]
_email_ = "huckerre@mail.uc.edu"

# RQ1


class Cheer:
    """
    >>> UC = Cheer("Bearcats")
    >>> for c in UC:
    ...     print(c)
    ...
    Give me an B
    Give me an e
    Give me an a
    Give me an r
    Give me an c
    Give me an a
    Give me an t
    Give me an s
    """

    def __init__(self, word):
        self.word = word
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index >= len(self.word):
            raise StopIteration
        else:
            letter = self.word[self.index]
            self.index += 1
            return "Give me an " + letter


# RQ2
class Countdown:
    """
    An iterator that counts down from N to 0.
    >>> for number in Countdown(5):
    ...     print(number)
    ...
    5
    4
    3
    2
    1
    0
    >>> for number in Countdown(2):
    ...     print(number)
    ...
    2
    1
    0
    """

    def __init__(self, n):
        self.n = n
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index >= self.n+1:
            raise StopIteration
        else:
            self.index += 1
            return self.n - self.index + 1

##############
# Generators #
##############

# RQ3


def evens():
    """A generator function that yields the infinite sequence of all even natural
    numbers, starting at 1.

    >>> m = evens()
    >>> type(m)
    <class 'generator'>
    >>> [next(m) for _ in range(5)]
    [2, 4, 6, 8, 10]
    """
    x = 0
    while True:
        x += 2
        yield x

# RQ4


def scale(s, k):
    """Yield elements of the iterable s scaled by a number k.

    >>> s = scale([1, 5, 2], 5)
    >>> type(s)
    <class 'generator'>
    >>> list(s)
    [5, 25, 10]

    >>> m = scale(naturals(), 2)
    >>> [next(m) for _ in range(5)]
    [2, 4, 6, 8, 10]
    """
    for i in s:
        yield i * k

# RQ5


def countdown(n):
    """
    A generator that counts down from N to 0.
    >>> for number in countdown(5):
    ...     print(number)
    ...
    5
    4
    3
    2
    1
    0
    >>> for number in countdown(2):
    ...     print(number)
    ...
    2
    1
    0
    """
    for i in range(n, -1, -1):
        yield i


# RQ6
def hailstone(n):
    """
    >>> for num in hailstone(10):
    ...     print(num)
    ...
    10
    5
    16
    8
    4
    2
    1
    """
    while n > 1:
        yield n
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1
    yield n


def naturals():
    i = 1
    while True:
        yield i
        i += 1


if __name__ == '__main__':
    doctest.testmod(verbose=True)
