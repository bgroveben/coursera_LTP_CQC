import cProfile
import random


def bubble_sort(L):
    """
    (list) - > NoneType

    Sort the items in L from smallest to largest

    >>> L = [7, 3, 5, 2]
    >>> bubble_sort(L)
    >>> L
    [2, 3, 5, 7]
    """
    # The variable end is the index of the last unsorted item.
    end = len(L) - 1

    while end != 0:
        # Bubble once through the unsorted section to move the largest item to index end.
        for i in range(end):
            if L[i] > L[i+1]:
                L[i], L[i+1] = L[i+1], L[i]

        end = end - 1



def get_index_of_smallest(L, i):
    """
    (list, int) -> int

    Return the index of the smallest item in L[i:].

    >>> get_index_of_smallest([2, 7, 3, 5], 1)
    2
    """
    # The index of the smallest item so far.
    index_of_smallest = i

    for j in range(i+1, len(L)):
        if L[j] < L[index_of_smallest]:
            index_of_smallest = j

    return index_of_smallest


def selection_sort(L):
    """
    (list) -> NoneType

    Sort the items of L from smallest to largest.

    >>> L = [3, 7, 2, 5]
    >>> selection_sort(L)
    >>> L
    [2, 3, 5, 7]
    """
    for i in range(len(L)):
        # Find the index of the smallest item in L[i:] and swap that item with the item at index i.
        index_of_smallest = get_index_of_smallest(L, i)
        L[index_of_smallest], L[i] = L[i], L[index_of_smallest]



def insert(L, i):
    """
    (list, int) -> NoneType

    Precondition: L[:i] is sorted from smallest to largest.

    Move L[i] to where it belongs in L[:i+1].

    >>> L = [7, 3, 5, 2]
    >>> insert(L, 1)
    >>> L
    [3, 7, 5, 2]
    """
    # The value to be inserted into the sorted part of the list.
    value = L[i]
    # Find the index, j, where the value belongs.
    # Make room for the value by shifting.
    j = i
    while j != 0 and L[j-1] > value:
        # Shift L[j-1] one position to the right to L[j].
        L[j] = L[j-1]
        j = j - 1
    # Put the value where it belongs.
    L[j] = value


def insertion_sort(L):
    """
    (list) -> NoneType

    Sort the items of L from smallest to largest.

    >>> L = [7, 3, 5, 2]
    >>> insertion_sort(L)
    >>> L
    [2, 3, 5, 7]
    """
    for i in range(len(L)):
        insert(L, i)



L = [(random.randint(1, 10000)) for i in range(10000)]
print()
print("Bubble Sort: ")
cProfile.run('bubble_sort(L)')
print()
print("Selection Sort: ")
cProfile.run('selection_sort(L)')
print()
print("Insertion Sort: ")
cProfile.run('insertion_sort(L)')
print()
print("Python Standard Library Sort: ")
cProfile.run('sorted(L)')
print()
