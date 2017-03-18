# Functions for writing test cases.

def count_lowercase_vowels(s):
    """
    (str) -> int

    Return the number of lowercased vowels (a, e, i, o, u) in s.

    Notes for this exercise are in choosing_test_cases.txt.

    unittest cases will be in TestChoosingTestCases.py (no separate directory for tests -- yet).

    >>> write doctest cases here
    """
    num_vowels = 0
    for char in s:
        if char in 'aeiuo':
            num_vowels = num_vowels + 1
    return num_vowels



def is_palindrome(s):
    """
    (str) -> bool

    Return True if and only if s is a palindrome.

    Notes for this exercise are in choosing_test_cases.txt.

    unittest cases will be in TestChoosingTestCases.py (no separate directory for tests -- yet).

    >>> write doctest cases here

    """
    return s[::-1] == s
