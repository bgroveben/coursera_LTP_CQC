# The following functions have linear running time, meaning that the number of steps executed is proportional to n.

def print_ints(n):
    """
    (int) -> NoneType

    Print the integers from 1 to n, inclusive.
    """
    for i in range(1, n + 1):
        print(i)


print_ints(10)
print()
# When the function is called, the value that n refers to is equal to the number of items printed, so that:
# - when n refers to 10, 10 integers are printed.
# - when n refers to 20, 20 integers are printed.
# - when n refers to 40, 40 integers are printed.


def print_odd_ints(n):
    """
    (int) -> NoneType

    Print the odd values from 1 to n, inclusive.
    """
    for i in range(1, n+1, 2):
        print(i)


print_odd_ints(10)
print()
# When print_odd_ints() is called, the value that n refers to is (almost exactly) twice the number of items printed:
# - when n refers to 10, 5 integers are printed.
# - when n refers to 20, 10 integers are printed.
# - when n refers to 40, 20 integers are printed.
# The number of steps is still proportional to n, so the runtime is linear.
# In other words, the runtime grows linearly with respect to the size of the input.
