# Divide and conquer with binary search.
# The binary search algorithm is used to find a value in a sorted list.
# Instead of searching the list in sequence, binary search starts in the middle and eliminates half
# of the search items in each subsequent iteration until it finds (or doesn't find) the target value.

def binary_search(L, v):
    """
    (list, object) -> int

    Precondition: L is sorted from smallest to largest, and all of the items in L can be compared to v.

    Return the index of the first occurrence of v in L, or return -1 if v is not in L.

    >>> binary_search([2, 3, 5, 7], 2)
    0
    >>> binary_search([2, 3, 5, 7], 5)
    2
    >>> binary_search([2, 3, 5, 7], 8)
    -1
    """
    # b = beginning
    # e = end
    # m = middle
    b = 0
    e = len(L) // 2

    while b <= e:
        m = (b + e) // 2
        if L[m] < v:
            b = m + 1
        else:
            e = m - 1

    if b == len(L) or L[b] != v:
        return -1
    else:
        return b


if __name__ == '__main__':
    import doctest
    doctest.testmod()

# In the above function, the main while loop continues to loop as long as b is less than e.
# Once b is greater than e, our search is complete.
# Inside of the while loop, we first set m to the middle index between index b and index e.
# Then we have an if statement.
# If the item at position m is less than v, then we advance b to be the index just to the right of m.
# However, if the item at index m is greater than v, then we decrease e so that it is the index to the left of m.

# At the end of the function we have one more if statement.
# When the while loop ends, there are two reasons why it might have ended.
# First, if all of the items in the list are less than v, then b will end up being equal to the length of the list,
# and will refer to an index outside of the list.
# If that is the case, we check to see whether b is equal to the length of L, and if it is, return -1.
# Second, we check the item at location b.
# After all, it is possible that v is not contained in the list.
# If L[b] is equal to v, then we return b.
# Otherwise, we will return -1.
