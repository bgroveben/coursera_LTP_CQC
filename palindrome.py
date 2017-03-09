# Determine whether a string is a palindrome or not.

# Palindrome: a string that is read the same from front-to-back and back-to-front.
# Example palindromes: noon, racecar.

# Algorithm: a sequence of steps that accomplish a task.

# Function Design Recipe:
# 1. Examples
# 2. Type Contract
# 3. Header
# 4. Description
# 5. Body
# 6. Test

def is_palindrome(s):
    """
    (str) -> bool

    Return True if and only if s is a palindrome.

    >>> is_palindrome('noon')
    True
    >>> is_palindrome('racecar')
    True
    >>> is_palindrome('dented')
    False
    """
    pass

print()


# Algorithm 1:
# Reverse the string.
# Compare the reversed string to the original string.
def is_palindrome_v1(s):
    """
    (str) -> bool

    Return True if and only if s is a palindrome.

    >>> is_palindrome_v1('noon')
    True
    >>> is_palindrome_v1('racecar')
    True
    >>> is_palindrome_v1('dented')
    False
    """
    return reverse(s) == s


def reverse(s):
    """
    (str) -> str

    Return a reversed version of s.

    >>> reverse('hello')
    'olleh'
    >>> reverse('a')
    'a'
    """
    rev = ''
    # For each character in s, add that character to the beginning of rev.
    for ch in s:
        rev = ch + rev

    return rev


print(is_palindrome_v1('noon'))
print(is_palindrome_v1('racecar'))
print(is_palindrome_v1('dented'))
print()


# Algorithm 2:
# Split the string into two halves.
# Reverse the second half.
# Compare the first half to the reversed second half.
def is_palindrome_v2(s):
    """
    (str) -> bool

    Return True if and only if s is a palindrome.

    >>> is_palindrome_v2('noon')
    True
    >>> is_palindrome_v2('racecar')
    True
    >>> is_palindrome_v2('dented')
    False
    """
    # The number of characters in s
    n = len(s)
    # Compare the first half of s to the reverse of the second half.
    # Omit the middle character of an odd-length string.
    return s[:n // 2] == reverse(s[n - n // 2:])


print(is_palindrome_v2('noon'))
print(is_palindrome_v2('racecar'))
print(is_palindrome_v2('dented'))
print()
# Algorithm 3:
# Compare the 1st character to the last character.
# Compare the 2nd character to the second-to-last character.
# ...
# Stop when the middle of the string is reached.
# For a string with an odd length, the middle character doesn't need to be compared to anything.
