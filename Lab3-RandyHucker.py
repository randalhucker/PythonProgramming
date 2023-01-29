# CS2023 - Lab 3 Required Questions
# All functions should be written using recursion.

import doctest
_author_ = "Randy Hucker"
_credits_ = ["Me"]
_email_ = "huckerre@mail.uc.edu"  # Your email address

# RQ1


def doubletime(i, n):
    """Returns the result of repeatedly doubling the number i a total of n times
    >>> doubletime(3, 1)
    6
    >>> doubletime(2, 0)
    2
    >>> doubletime(2, 9)
    1024
    """
    if n == 0:
        return i  # If we've exhausted n, return
    else:
        return doubletime((i*2), (n-1))  # If n>0, double and call self.


# RQ2
def skip2_add(n):
    """ Takes a number x and returns x + x-3 + x-6 + x-9 + ... + 0.
    >>> skip2_add(5)  # 5 + 2  + 0
    7
    >>> skip2_add(10) # 10 + 7 + 4 + 1 + 0
    22
    """
    if (n - 3 < 0):
        return n  # If n can't be subtracted to > 0, begin to return
    else:
        # Add and call self to add subtraction statement
        return (n+skip2_add(n-3))

# RQ3


def a(n):
    """Return the number in the sequence defined by a(1) = 1;
    a(n) = (3/2)*a(n-1) if a(n-1) is even; a(n) = (3/2)*(a(n-1)+1) if a(n-1) is odd.
    (see, http://oeis.org/A070885)
    >>> a(1)
    1
    >>> a(2) 
    3
    >>> a(3)
    6
    >>> a(10)
    123
    """
    if (n == 1):
        return 1  # If n == 1 return out of loop.
    if (a(n-1) % 2 != 0):
        return int(1.5*(a(n-1)+1))  # If odd case - use given
    else:
        return int(1.5*a(n-1))  # If even case - use given

# RQ4


def paths(m, n):
    """Return the number of paths from one corner of an
    M by N grid to the opposite corner.
    >>> paths(2, 2)
    2
    >>> paths(3, 3)
    6
    >>> paths(5, 7)
    210
    >>> paths(117, 1)
    1
    >>> paths(1, 157)
    1
    """
    if (m == 1 or n == 1):
        return 1  # If reached path maximum for that (row | col), begin return
    else:
        # Call two seperate instances for each option (up and right) - calling each reduces grid size by 1 (row | col)
        return paths((m-1), n) + paths(m, (n-1))


if __name__ == "__main__":
    doctest.testmod(verbose=True)
