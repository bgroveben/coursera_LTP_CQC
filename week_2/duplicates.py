### Testing Functions that Mutate Values ###

# The Problem : given two lists, remove the items from the first list that appear in the second list.
# The Algorithm: for each item in the second list, if that item appears in the first list, remove it.

def remove_shared(L1, L2):
    """
    (list, list) -> NoneType

    Remove items from L1 that are in both L1 and L2.

    >>> list_1 = [1, 2, 3, 4, 5, 6]
    >>> list_2 = [2, 4, 5, 7]
    >>> remove_shared(list_1, list_2)
    >>> list_1
    [1, 3, 6]
    >>> list_2
    [2, 4, 5, 7]
    """
    for v in L2:
        if v in L1:
            L1.remove(v)


if __name__ == '__main__':
    import doctest
    print(doctest.testmod())
