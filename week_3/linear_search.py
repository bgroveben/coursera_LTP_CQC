def linear_search(L, v):
    """
    (list, object) -> int

    Return the index of the first occurrence of v in L, or return -1 if v is not in L.

    >>> linear_search([2, 3, 5, 3], 2)
    0
    >>> linear_search([2, 3, 5, 3], 5)
    2
    >>> linear_search([2, 3, 5, 3], 8)
    -1
    """
    i = 0

    while i != len(L) and v != L[i]:
        i = i + 1

    if i == len(L):
        return -1
    else:
        return i


# The while loop has two conditions for when to end the loop:
# 1. We will continue looping while the index i is not equal to the length of the list.
#    Since the index starts from 0, we will be examining each item in the list in a forward manner.
# 2. We will continue looping as long as v is not in the current position of the list (v != L[i]).
#    In other words, if v is in the current position of the list, then we know we have found what we're looking for
#    and we can exit the while loop.

# There is an if statement after the while loop ends.
# This is because there are two possible reasons why the while loop could have exited.
# First is the case where we have not found what we're looking for, and this happens when the index i is equal to the
# length of the list (i == len(L)).
# In this case, we return -1.
# Otherwise, if i is not equal to the length of the list, then i is less than the length of the list, so we must return i.
# This is because i is the index at which we found the value v, which is why the while loop ended before i became
# equal to the length of the list.
