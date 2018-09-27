# Project Euler Problem 1 Solution
#
# Problem statement:
# Each new term in the Fibonacci sequence is generated by adding
# the previous two terms. By starting with 1 and 2, the first 10
# terms will be:
#
# 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...
#
# By considering the terms in the Fibonacci sequence whose values
# do not exceed four million, find the sum of the even-valued terms.
#
# Solution description:
#
# Author: Daniel Schuette
# Date: 2018/09/24
# License: MIT (see ../LICENSE.md)
import time


def slow_fibonacci(n):
    """
    this function calculates the fibonacci sequence up to the n'th
    member
    """
    x = 0
    y = 1
    if n == 1:
        return 1
    for i in range(n):
        _tmp = x  # the current `x' is stored in a tmp variable
        x = y  # `x' becomes the previous `y'
        y = _tmp + x  # `y' becomes the sum of the previous `x' and `y'
    return y


def fast_fibonacci(n):
    """
    """
    pass


if __name__ == "__main__":
    # start timing
    start = time.time()

    # define looping variables
    i = 0
    sum = 0
    target = 4000000

    # loop until `fibonacci()' returns an integer > target
    while True:
        i += 1
        _tmp = slow_fibonacci(i)
        if _tmp > target:
            break
        if (_tmp % 2) == 0:
            sum += _tmp

    # stop timing and print results
    end = time.time()
    print("result: {}".format(sum))
    print("elapsed: {}s".format(end - start))
