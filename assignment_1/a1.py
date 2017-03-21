def num_buses(n):
    """ (int) -> int

    Precondition: n >= 0

    Return the minimum number of buses required to transport n people.
    Each bus can hold 50 people.

    >>> num_buses(0)
    0
    >>> num_buses(1)
    1
    >>> num_buses(50)
    1
    >>> num_buses(75)
    2
    >>> num_buses(100)
    2
    >>> num_buses(101)
    3
    >>> num_buses(235)
    5
    """
    total = 0
    remaining = n

    while remaining > 0:
        total += 1
        remaining -= 50

    return total



def stock_price_summary(price_changes):
    """ (list of number) -> (number, number) tuple

    price_changes contains a list of stock price changes. Return a 2-item
    tuple where the first item is the sum of the gains in price_changes and
    the second is the sum of the losses in price_changes.

    >>> stock_price_summary([])
    (0, 0)
    >>> stock_price_summary([0])
    (0, 0)
    >>> stock_price_summary([0.05])
    (0.05, 0)
    >>> stock_price_summary([-0.05])
    (0, -0.05)
    >>> stock_price_summary([0, 0, 0, 0, 0, 0, 0])
    (0, 0)
    >>> stock_price_summary([0.01, 0.03, -0.02, -0.14, 0, 0, 0.10, -0.01])
    (0.14, -0.17)
    >>> stock_price_summary([0.01, 0.03, 0.02, 0.14, 0.10, 0.01])
    (0.31, 0)
    >>> stock_price_summary([-0.01, -0.03, -0.02, -0.14, -0.10, -0.01])
    (0, -0.31)
    """
    gain, loss = 0, 0

    for price in price_changes:
        if price < 0:
            loss += price
        else:
            gain += price

    return (round(gain, 2), round(loss, 2))



def swap_k(L, k):
    """ (list, int) -> NoneType

    Precondition: 0 <= k <= len(L) // 2

    Swap the first k items of L with the last k items of L.

    >>> nums1 = [1, 2, 3, 4, 5]
    >>> swap_k(nums1, 0)
    >>> nums1
    [1, 2, 3, 4, 5]

    >>> nums1 = [1, 2, 3, 4, 5]
    >>> swap_k(nums1, 1)
    >>> nums1
    [5, 2, 3, 4, 1]

    >>> nums2 = [1, 2, 3, 4, 5, 6, 7]
    >>> swap_k(nums2, 3)
    >>> nums2
    [5, 6, 7, 4, 1, 2, 3]

    >>> nums3 = [1, 2, 3, 4, 5, 6, 7]
    >>> swap_k(nums3, 2)
    >>> nums3
    [6, 7, 3, 4, 5, 1, 2]

    >>> nums4 = [1, 2, 3, 4, 5, 6]
    >>> swap_k(nums4, 1)
    >>> nums4
    [6, 2, 3, 4, 5, 1]

    >>> nums5 = [1, 2, 3, 4, 5, 6, 7, 8]
    >>> swap_k(nums5, 3)
    >>> nums5
    [6, 7, 8, 4, 5, 1, 2, 3]

    >>> nums6 = [1, 2, 3, 4, 5, 6]
    >>> swap_k(nums6, 2)
    >>> nums6
    [5, 6, 3, 4, 1, 2]
    """
    if not k:
        L
    else:
        first = L[:k]
        L[:k] = L[-k:]
        del L[-k:]
        L.extend(first)



if __name__ == '__main__':
    import doctest
    print(doctest.testmod())
