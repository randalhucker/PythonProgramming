import doctest
from math import sin, cos

_author_ = "Randy Hucker"
_credits_ = ["Me", "https://www.geeksforgeeks.org/any-all-in-python/"]
_email_ = "huckerre@mail.uc.edu"

# # def approx_fixed_point(f, x) should
# # return True if and only if f(x) is very close (distance < 1e-15) to x.


def approx_newton_point(f, x):
    test = f(x)
    # difference = test + 1
    if (abs(test) == 1):
        return True
    return False


def newton_find_zero(f, f_prime, x):
    """
    # >>> newton_find_zero(lambda x: sin(x) , lambda x: cos(x), 3.0) 
    # (3.141592653589793, 3)
    >>> newton_find_zero(lambda x: cos(x) - x , lambda x: -sin(x)-1, 1.0)
    (0.7390851332151606, 7)
    """
    step = 0
    while not (approx_newton_point(f_prime, x)):
        x = x - (f(x)/f_prime(x))
        step += 1
    x = x-(f(x)/(-1))
    step += 1
    return x, step


def approx_fixed_point(f, x):
    if (abs(f(x)-x) < 1e-15):
        return True
    return False


def fixed_point_iteration(f_arg, x=1.0):
    """
    >>> fixed_point_iteration(lambda x: sin(x) + x, 3.0) 
    (3.141592653589793, 3)
    >>> fixed_point_iteration(lambda x: cos(x), 1.0)
    (0.7390851332151611, 86)
    """
    step = 0
    while not approx_fixed_point(f_arg, x):
        x = f_arg(x)
        step += 1
    return x, step


if __name__ == "__main__":
    doctest.testmod(verbose=True)
