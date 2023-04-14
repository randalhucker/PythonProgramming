## Lab 8: Trees ##

import doctest
_author_ = "Randy Hucker"
_credits_ = ["Me"]
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

    "*** YOUR CODE HERE ***"


##############
# Generators #
##############

# RQ3
def evens():
    """A generator function that yields the infinite sequence of all even natural
    numbers, starting at 1.

    >>> m = evens()
    >>> type(m)

    >>> [next(m) for _ in range(5)]
    [2, 4, 6, 8, 10]
    """
    "*** YOUR CODE HERE ***"

# RQ4


def scale(s, k):
    """Yield elements of the iterable s scaled by a number k.

    >>> s = scale([1, 5, 2], 5)
    >>> type(s)

    >>> list(s)
    [5, 25, 10]

    >>> m = scale(naturals(), 2)
    >>> [next(m) for _ in range(5)]
    [2, 4, 6, 8, 10]
    """
    "*** YOUR CODE HERE ***"

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
    "*** YOUR CODE HERE ***"


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
    "*** YOUR CODE HERE ** *
