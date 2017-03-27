import cProfile


def slower_linear_search(L, v):
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



def faster_linear_search(L, v):
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
    # Creating a variable for list length for use in the while loop and if statement will speed up execution.
    length = len(L)

    while i != length and v != L[i]:
        i = i + 1

    if i == length:
        return -1
    else:
        return i



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


L = list(range(10000000))  # Seven zeros == 10 million
print()
print("Slower Linear Search Profile: ")
cProfile.run('slower_linear_search(L, 10000000)')
print()
print("Faster Linear Search Profile: ")
cProfile.run('faster_linear_search(L, 10000000)')
print()
print("Binary Search Profile: ")
cProfile.run('binary_search(L, 10000000)')
