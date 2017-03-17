def get_divisors(num, possible_divisors):
    """
    (int, list of int) -> list of int

    Return a list of the values from possible_divisors that are divisors of num.

    >>> get_divisors(8, [1, 2, 3])
    [1, 2]
    >>> get_divisors(4, [-2, 0, 2])
    [-2, 2]
    """
    divisors = []
    for item in possible_divisors:
        if item != 0 and num % item == 0:
        # Comment supra and uncomment infra if you want to see an error.
        # if num % item ==0:
            divisors.append(item)
    return divisors

if __name__=='__main__':
    import doctest
    # doctest.testmod()
    # If you really want to see the test results printed in the console:
    print(doctest.testmod())
