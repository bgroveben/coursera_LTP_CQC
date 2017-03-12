### Week 1 Quiz ###


# 1.
def is_palindrome_v3(s):
    """
    (str) -> bool

    Return True if and only if s is a palindrome.

    1. Compare the first character to the last character, the second to the second last, and so on.
    2. Stop when the middle of the string is reached, so that the middle character isn't compared with anything.

    >>> is_palindrome_v3('noon')
    True
    >>> is_palindrome_v3('racecar')
    True
    >>> is_palindrome_v3('dented')
    False
    """
    j = len(s) - 1
    for i in range(len(s) // 2):
        if s[i] != s[j - i]:
            return False

    return True


    for i in range(len(s) // 2):
        if s[i] != s[len(s) - i - 1]:
            return False

    return True

print()
print(is_palindrome_v3('noon'))
print(is_palindrome_v3('racecar'))
print(is_palindrome_v3('dented'))
print()


# 2.
def is_anagram(s1, s2):
    """
    (str, str) -> bool

    Return True if and only if s1 is an anagram of s2.
    A string s1 is an anagram of string s2 if its letters can be rearranged to form s2.

    >>> is_anagram("silent", "listen")
    True
    >>> is_anagram("bear", "breach")
    False
    """
    # return sorted(s1) == sorted(s2)

    d1 = {i: s1.count(i) for i in s1}
    d2 = {i: s2.count(i) for i in s2}
    return d1 == d2

    L1 = [i for i in s1]
    L2 = [i for i in s2]
    for i in L1:
        if i in L2:
            L2.remove(i)
    return not L2

    # first = [(s1.count(letter), letter) for letter in sorted(set(s1))]
    # second = [(s2.count(letter), letter) for letter in sorted(set(s2))]
    # return first == second


print(is_anagram("silent", "listen"))
print(is_anagram("bear", "breach"))
print()


# 3. and 4.
def count_startswith(L, ch):
    """
    (list of str, str) -> int

    Precondition: the length of each item in L is >= 1, and len(ch) == 1.

    Return the number of strings in L that begin with ch.

    >>> count_startswith(['rumba', 'salsa', 'samba'], 's')
    2
    """
    # Use a list accumulator.
    ch_strings = []
    # For each item in L, if the item begins with ch, add it to the accumulator.
    for item in L:
        if item[0] == ch:
            ch_strings.append(item)
    # Return the length of the accumulator.
    return len(ch_strings)

    startswith = L[:]
    for item in L:
        if item.startswith(ch):
            startswith.remove(item)
    return len(L) - len(startswith)

    startswith =L[:]
    for item in L:
        if not item.startswith(ch):
            startswith.remove(item)
    return len(startswith)



count_startswith(['rumba', 'salsa', 'samba'], 's')
