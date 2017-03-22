# Analyzing algorithms and determining the amount of time algorithms take to run.

def repeat_chars(s):
    """
    (str) -> str
    """
    double = ''
    for character in s:
        double = double + character * 2  # The step being considered.
    return double


# As the length of s grows, how does the number of steps grow wrt len(s)?
# - constant?
# - logarithmically?
# - linearly?
# - quadratically?

# Run this code in the visualizer with different inputs, count the number of times the commented line of code (line 7) is
# executed, and compare that number to the length of s.
print(repeat_chars('abc'))
# The run time is linear, because in the print statement above, line 7 is executed once for each character
# in s. If s were length 7, then line 7 would be executed 7 times.

# Here is another example:
def first_thirty(s):
    """
    (str) -> str
    """
    thirty = ''
    for i in range(30):
        thirty = thirty + s[i] # The step being considered.
    return thirty


print(first_thirty('aaaaaaaaaaaaaaaaaaaaaaaaaaaaaa'))
# In the above example, the loop iterates 30 times and then returns a value (If s < 30, an IndexError is thrown).
# The number of steps is constant, because (assuming len(s) >= 30) no matter how long len(s) gets, only 30 steps
# are executed.


# Consider this code:
def f(L):
    """
    (list of numbers) -> number
    """
    total = 0
    for item in L:
        for i in range(10):
            total = total + item * i  # The step being considered.
    return total


print(f([1, 2, 3]))
# The number of steps grows linearly wrt len(L).
# This one is a bit tricky, because even though there is a nested loop, the number of times that the INNER
# loop iterates is constant and not affected by len(L).
# In other words, the inner loop executes 10 times for each item in L (no more, no less depending on length).
# However, as len(L) grows, there will be more iterations of the OUTER loop.
# For example, if len(L) is 3, there will be 30 * len(L) steps and if len(L) is 10, there will be
# 100 * len(L) steps.
# Therefore, the number of steps is growing linearly with respect to len(L).
