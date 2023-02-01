##Lab04 Required Questions ##

#########
# Lists #
#########

# RQ1
import doctest
_author_ = "Randy Hucker"
_credits_ = ["Me", "https://www.geeksforgeeks.org/any-all-in-python/"]
_email_ = "huckerre@mail.uc.edu"


def cascade(lst):
    """Returns the cascade of the given list running forward and back.

    >>> cascade([1, 2, 3, 4])
    [1, 2, 3, 4, 4, 3, 2, 1]
    """
    returnArray = []
    for x in range(2):
        for y in range(len(lst)):
            returnArray.append(lst[y])
        lst.reverse()
    return returnArray
# RQ2


def maptwice(fn, seq):
    """Applies fn twice onto each element in seq and returns the resulting list.

    >>> maptwice(lambda x: x*x, [1, 2, 3])
    [1, 16, 81]
    """
    returnArray = []
    for num in seq:
        returnArray.append(fn(num)*fn(num))
    return returnArray


# RQ3


def filterout(pred, seq):
    """Keeps elements in seq only if they do not satisfy pred.

    >>> filterout(lambda x: x % 2 == 0, [1, 2, 3, 4])
    [1, 3]
    """
    for num in seq:
        if (pred(num) != 0):
            seq.remove(num)
    return seq

# RQ4


def comp(n, pred):
    """ Uses a one line list comprehension to return list of the first n integers (0...n-1) which satisfy the predicate pred.
    >>> comp(7, lambda x: x%2 == 0)
    [0, 2, 4, 6]
    """
    returnArray = []
    for x in range(n):
        if pred(x):
            returnArray.append(x)
    return returnArray

# RQ5


def flatten(lst):
    """ Takes a nested list and "flattens" it.

    >>> flatten([1, 2, 3]) 
    [1, 2, 3]
    >>> x = [1, [2, 3], 4]      
    >>> flatten(x)
    [1, 2, 3, 4]
    >>> x = [[1, [1, 1]], 1, [1, 1]] 
    >>> flatten(x)
    [1, 1, 1, 1, 1, 1]
    >>> lst = [1, [[2], 3], 4, [5, 6]]
    >>> flatten(lst)
    [1, 2, 3, 4, 5, 6]
    """
    returnArray = []
    for element in lst:
        if isinstance(element, list):
            returnArray.extend(element)
            continue
        returnArray.append(element)
    if (any(isinstance(element, list) for element in returnArray)):
        returnArray = flatten(returnArray)
    return returnArray


if __name__ == "__main__":
    doctest.testmod(verbose=True)
