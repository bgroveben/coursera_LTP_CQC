# In the add_greeting() function, the default parameter is mutable.
# We have the parameter L that has a default value of an empty list.
# The function appends the string 'hello' to the list and prints it.

def add_greeting(L=[]):
    """ (list) -> NoneType

    Append 'hello' to L and print L.

    >>> L = ['hi', 'bonjour']
    >>> add_greeting(L)
    ['hi', 'bonjour', 'hello']
    """
    L.append('hello')
    print(L)


if __name__ == '__main__':
    import doctest
    doctest.testmod()

# Now let's see what happens when the function is called multiple times.
    print()
    add_greeting()
    add_greeting()
    add_greeting()
    print()
# The memory address that L refers to is the same for each function call, so the string 'hello' is appended
# to that same list each time the function is called.
# When the function is called, any changes that the function call makes to the mutable object persist from
# one function call to the next.
