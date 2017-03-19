# Functions for writing test cases.

def count_lowercase_vowels(s):
    """
    (str) -> int

    Return the number of lowercased vowels (a, e, i, o, u) in s.

    Notes for this exercise are in choosing_test_cases.txt.

    unittest cases will be in TestChoosingTestCases.py (no separate directory for tests -- yet).

    >>> count_lowercase_vowels('')
    0
    >>> count_lowercase_vowels('a')
    1
    >>> count_lowercase_vowels('b')
    0
    >>> count_lowercase_vowels('pfffft')
    0
    >>> count_lowercase_vowels('bandit')
    2
    >>> count_lowercase_vowels('aeioua')
    6
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

    >>> is_palindrome('')
    True
    >>> is_palindrome('a')
    True
    >>> is_palindrome('aa')
    True
    >>> is_palindrome('ab')
    False
    >>> is_palindrome('aba')
    True
    >>> is_palindrome('abc')
    False
    >>> is_palindrome('redder')
    True
    >>> is_palindrome('reader')
    False
    >>> is_palindrome('racecar')
    True
    >>> is_palindrome('bananas')
    False
    """
    return s[::-1] == s

if __name__ == '__main__':
    import doctest
    print(doctest.testmod())
