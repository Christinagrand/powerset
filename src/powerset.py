"""Module for computing power sets."""

from typing import Any


def power(x: list[Any]) -> list[list[Any]]:
    """
    Compute the power-set of x.

    Returns the power-set of x as a list of lists.
    """
    subset = [[]]
    for i in range(len(x)+1):
        for j in range(i+1,len(x)+1):
            ny = x[i:j]
            subset.append(ny)
    return subset  # FIXME: you need to add some code here.

# print(power([1,2,3]))

# y = [1,2]
# print(y[0:1])
