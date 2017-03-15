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
    # Create a dictionary 𝚍𝟷 in which each key is a letter from 𝚜𝟷 and each value is the number of occurrences
    # of that letter in 𝚜𝟷.
    # Create a dictionary 𝚍𝟸 in which each key is a letter from 𝚜𝟸 and each value is the number of occurrences
    # of that letter in 𝚜𝟸.
    # If 𝚍𝟷 == 𝚍𝟸, then 𝚜𝟷 is an anagram of 𝚜𝟸.

    # Create a list 𝙻𝟷 of the characters in 𝚜𝟷.
    # Create a list 𝙻𝟸 of the characters in 𝚜𝟸.
    # Sort both lists.
    # If 𝙻𝟷 == 𝙻𝟸, 𝚜𝟷 is an anagram of 𝚜𝟸.

    return sorted(s1) == sorted(s2)

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

# 4. Select the code fragment(s) that correctly implement the function according to the header above.
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


print(count_startswith(['rumba', 'salsa', 'samba'], 's'))
print()


# 5.
# Consider this code, in which s refers to a string:
def numberfive(s):
    digits = ""
    for ch in s:
        if ch.isdigit():
            digits = digits + ch
    return digits
# Select the code fragment(s) that will produce the same value for digits.
def numberfive(s):
    digits = ''
    for i in range(len(s)):
        if s[i].isdigit():
            digits = digits + s[i]
    return digits

def numberfive(s):
    indices = []
    digits = ''
    for i in range(len(s)):
        if s[i].isdigit():
            indices.append(i)
    for index in indices:
        digits = digits + s[index]
    return digits

def numberfive(s):
    digits = ''
    for ch in s:
        if ch in '0123456789':
            digits = digits + ch
    return digits

print(numberfive('abc123'))
print()


# 6. and 7.
# Consider this function header and docstring:
def is_one_to_one(d):
    """
    (dict) -> bool

    Return True if and only if no two of d's keys map to the same value.
    (Translation: Return True if and only if each key in d has a unique value.)

     >>> is_one_to_one({'a': 1, 'b': 2, 'c': 3})
     True
     >>> is_one_to_one({'a': 1, 'b': 2, 'c': 1})
     False
     >>> is_one_to_one({})
     True
    """
# 6. Select the algorithm(s) that can be used to implement is_one_to_one.

    # 6-1. Use a list accumulator to keep track of the values we've seen so far.
    seen = []  # The values that have been seen so far.
    # 6-2. For each key in d,
    for k in d:
        # if the value associated with that key has already been seen, return False;
        if d[k] in seen:
            return False
        # otherwise, append it to the list of values that we've seen so far.
        else:
            seen.append(d[k])
    # 6-3. Once all of the keys have been processed, return True because we didn't see a duplicate value.
    return True

    # 6-1 Put all of the values from d into a list.
    v = []
    for i in d.values():
        v.append(i)
    # 6-2 For each value in the list, count how many times it appears in the list.
    counts = {i: v.count(i) for i in v}
    # If a value appears more than once in the list, return False.
    for count in counts.values():
        if count > 1:
            return False
    # 6-3 Once all of the values in the list have been processed, return True because we didn't see a duplicate value.
    return True

    # 6-1 Put all of the values from d into a list.
    v = []
    for i in d.values():
        v.append(i)
    # 6-2 Make a copy of that list.
    dup_v = v.copy()
    # 6-3 Remove all of the duplicate items from the second list.
    rmv = set(dup_v)
    # 6-4 Compare the lengths of the two lists.
    # If they are equal, return True because that means that there were no duplicate items; otherwise, return False
    return rmv == v

# 7. Select the algorithm that best describes the approach taken in the function defined above.


print(is_one_to_one({'a': 1, 'b': 2, 'c': 3}))
print(is_one_to_one({'a': 1, 'b': 2, 'c': 1}))
print(is_one_to_one({}))


# 8. Which of the following data structures could be used to represent one person's responses to the questions?
#### List of str, where each character is either 'Y' or 'N'
#### dict of {str: list of int}, where each key is a response (either 'Y' or 'N') and each value is a list of questions numbers for which the person provided that response.

# 9. Which of the following data structures could be used to represent all of the cyclists and their times?
#### A list of [str, float] lists, where each inner list represents [cyclist, time]. The outer list is ordered from fastest time to slowest time.
#### A dict of {str: float} where each key is a cyclist and each value is a time.
#### Parallel lists, where one is a 𝚕𝚒𝚜𝚝 𝚘𝚏 𝚜𝚝𝚛 and the other is a 𝚕𝚒𝚜𝚝 𝚘𝚏 𝚏𝚕𝚘𝚊𝚝: the list of cyclists, and the list of their times. The lists are sorted by the order in which the cyclists cross the finish line (which is not the same as how long they took).

# 10. Which data structure will make it easiest to look up the three fastest cyclists?
#### A list of [str, float] lists, where each inner list represents [cyclist, time]. The outer list is ordered from fastest time to slowest time.

#!#!# 11 IS STILL WRONG #!#!
# 11. Select the algorithm(s) that can determine the city that had the maximum total precipitation in February.
# 11-1 Build the weather dictionary.
# 11-2 Look up key '𝙵𝚎𝚋' in the weather dictionary to get the "city to precipitation" dictionary for February.
# 11-3 Create a list containing the sum of the precipitation amounts from each of the city precipitation lists for February. Also create a parallel list containing the city names.
# 11-4 Sort the list containing the sum of the precipitation amounts so that the largest value is last. The answer is the city in the parallel list at the last position.

# 11-1 Build the weather dictionary.
# 11-2 Look up key '𝙵𝚎𝚋' in the weather dictionary to get the "city to precipitation" dictionary for February.
# 11-3 Iterate through the cities in that dictionary, calculating the sum of the precipitation amounts for that city. Keep track of the city that has the most precipitation so far.
# 11-4 Once the iteration is complete, whichever city had the most precipitation is the answer.

# 11-1 Build the weather dictionary.
# 11-2 Look up key '𝙵𝚎𝚋' in the weather dictionary to get the "city to precipitation" dictionary for February.
# 11-3 Invert that dictionary so that the keys are the lists of precipitation amounts and the values are the cities.
# 11-4 For each key in this inverted dictionary, sum the precipitation amounts in that list, and keep track of the list that had the largest sum.
# 11-5 Once the iteration is complete, whichever list had the most precipitation is the key. To get the answer, look its value up in the inverted dictionary to get the corresponding city name.

# 12. Select the algorithm(s) that can be used to make a list of the days in which no city had any precipitation.
# 12-1 Build the weather dictionary.
# 12-2 Create an empty "zero-precipitation" list to accumulate the answer.
# 12-3 Iterate over the months to get each "city to precipitation" dictionary. For each of these dictionaries:
#    a) Build a dictionary where each key is a city from the current "city to precipitation" dictionary, and each value is a list of the day numbers on which the city had no precipitation.
#    b) Iterate over the values in that dictionary to build a list containing the day numbers that appear in all the lists of day numbers.
#    c) Iterate over the list of day numbers, appending tuples containing the current month name and the day number to the "zero-precipitation" list.

# 12-1 Build the weather dictionary.
# 12-2 Create a "zero-precipitation" list containing all days of the year from ('𝙹𝚊𝚗', 𝟷) through ('𝙳𝚎𝚌', 𝟹𝟷).
# 12-3 Iterate over the months to get each "city to precipitation" dictionary. For each of these dictionaries:
#    a) For each city in the current "city to precipitation" dictionary, iterate over the precipitation amounts. Because we know the current month and day number, we will remove from the "zero-precipitation" list any day that has a non-zero precipitation amount.
# 12-4. One this process is complete, the "zero-precipitation" list contains only the (month, day number) for days in which no city had precipitation.
