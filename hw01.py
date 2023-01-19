import doctest
_author_ = "Randy Hucker"
_credits_ = ["Me", "https://en.wikipedia.org/wiki/Greedy_algorithm_for_Egyptian_fractions#:~:text=In%20mathematics%2C%20the%20greedy%20algorithm,%3D%2012%20%2B%2013. - Was used to understand the greedy algorithm and use the related expansions to get a base for the computations"]
_email_ = "huckerre@mail.uc.edu"  # Your email address


def egypt(n, d):
    """
    >>> egypt(3,4)
    '1/2 + 1/4 = 3/4'
    >>> egypt(11,12)
    '1/2 + 1/3 + 1/12 = 11/12'
    >>> egypt(123,124)
    '1/2 + 1/3 + 1/7 + 1/64 + 1/8333 + 1/347186112 = 123/124'
    >>> egypt(103,104)
    '1/2 + 1/3 + 1/7 + 1/71 + 1/9122 + 1/141449381 + 1/100039636784966424 = 103/104'
    """
    nO = n # A Placeholder for the original numerator
    dO = d # A Placeholder for the original denominator
    denArray = []
    while n != 0: # Builds solution array.
        den = ((d-1)//n)+1 # Solution for the computation being to long for float, since "//" does int division to floor, need to add 1 for the floor adjustment
        denArray.append(den) # add to array
        n = (den * n) - d # move to next numerator value for algo
        d = (d * den) # move to next demenator value

    print("'", end='')

    for i in range(len(denArray)):
        if i != len(denArray) - 1:
            print(f"1/{abs(denArray[i])} +", end=" ") # Solution for non conclusion print statements
        else:
            print(f"1/{abs(denArray[i])}", end="") # Solution for adding correct end characters

    print(f" = {nO}/{dO}'", end='')
    
    # Old Algo Code before using wikipedia to find a more elegant algo.
    
    # remainder = Fraction(n, d)
    # remainderCount = 2
    # if (remainder == 1):
    #     raise (ValueError)

    # remainder -= Fraction(1, remainderCount)
    # print(f"'1/{remainderCount}", end='')
    # remainderCount += 1

    # if (remainder != 0):
    #     while (remainder != 0):
    #         temp = remainder
    #         temp -= Fraction(1, remainderCount)
    #         if (temp < 0):
    #             remainderCount += 1
    #             continue
    #         remainder -= Fraction(1, remainderCount)
    #         print(" + ", end='')
    #         print(f"1/{remainderCount}", end='')
    #         remainderCount += 1
    #     print(f" = {n}/{d}'", end='')
    # return

# Partial credit will be given for code that passes the two given doctests.
# For full credit on HW1 you should test your solutions to egypt(103,104) and  egypt(123,124)
# These are more difficult and may require you to develop faster, more efficient code.
# Hint: you may consider using code for gcd function for greatest common divisor:
# https://www.geeksforgeeks.org/gcd-in-python/


if __name__ == "__main__":
    doctest.testmod(verbose=True)

