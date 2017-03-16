### Testing Automatically Using doctest ###

# As part of the function design recipe, we include one or two example calls on the function in the doctstring.
# For example, consider the function collect_vowels():

def collect_vowels(s):
    """
    (str) -> str

    Return the vowels (a, e, i, o, u) from s.

    >>> collect_vowels('Happy Anniversary!')
    'aAiea'
    >>> collect_vowels('xyz')
    ''
    """
    vowels = ''
    for char in s:
        if char in 'aeiouAEIOU':
            vowels = vowels + char
    return vowels

# Using doctest, you can run all of the tests from the docstring at once.
# Using IDLE:
# After running the module containing collect_vowels in the Python shell, import the doctest module,
# then call doctest.testmod():

# >>> import doctest
# >>> doctest.testmod()
# TestResults(failed=0, attempted=2)

# The number of tests that failed and the number of tests that were attempted are reported.
# In the example above, 2 tests were attempted and 0 failed.
# doctest.testmod() automatically compares the actual value returned by the function call with the expected value.

# You can also automatically run doctest when you load a module into Python by including the following code
# at the end of the module:

# import doctest
# doctest.testmod()

# In this case, every time you run the module, the doctest is also executed.
# If there are no errors, nothing will be reported to the console output (no news is good news).
# Try running this file in your terminal and see for yourself.
# Break the code and then run the file if you want to see how doctest handles errors.

import doctest
doctest.testmod()
