# Functions that run in logarithmic time don't increase the number of computations as quickly as the
# proportional increase in the size of n, which gives them runtimes close to constant time.

def print_double_step(n):
    """
    (int) -> NoneType

    Print integers from 1 to n inclusive, with an initial step size of 1 and each subsequent
    step size being twice as large as it was previously.

    In this example, the size of the first step is 1, the next step is 2, then 4, then 8, 16, 32,  ...
    """
    i = 1
    while i < n+1:
        print(i)
        i = i * 2

print_double_step(2)
print()
print_double_step(4)
print()
print_double_step(6)
print()
print_double_step(8)
print()
# When n refers to values 8 to 15, 4 integers will be printed.
# When n refers to 16, 5 integers are printed.
# When n refers to 32, 6 integers are printed.
# When n refers to 64, 8 integers are printed.
# Starting with n referring to 1, each time that n is doubled, one extra line is printed.
# This function is logarithmic and as the input size increases, the running time grows more slowly than
# for linear and quadratic functions.
