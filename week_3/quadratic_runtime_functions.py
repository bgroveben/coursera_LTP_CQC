# When functions run in quadratic time, every time you increase the number of elements (n),
# the number of computational steps will increase by the square of n (n*n, or n^2).

def print_pairs(n):
    """
    (int) -> NoneType

    Print all combinations of pairs of integers 1 to n, inclusive.
    """
    for i in range(1, n+1):
        for j in range(1, n+1):
            print(i, j)


print_pairs(2)
# Prints 4 pairs of integers.
print()
print_pairs(3)
# Prints 9 pairs of integers.
print()
print_pairs(4)
# Prints 16 pairs of integers.
print()
# For argument n, the print function is called n^2 times.
# When reading the code, notice that the print function call is inside a for loop, which loops n times.
# This (inner) for loop is also within a (outer) for loop that executes n times.
# Therefore, you get n * n iterations, meaning that the runtime grows quadratically wrt the size of the input.
