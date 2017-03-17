### Creating YOur Own Types ###

# Importing a module

# The math module contains functions such as math.ceil, which returns the smallest integer that is greater than
# or equal to the function's argument.
# Importing math creates a variable called math.
# This creates a namespace, or chunk of memory, that holds the information for all of the functions and data
# variables in the math module.
import math
print()
print(math.ceil(4.3))
print()

# Type str

# Because str is built into Python, we already have a type named str.
# But, instead of a module, str refers to a class, and contains methods rather than functions.
# The notation for calling a str method is similar to the one used to call a function from the math module.
print(str.count('syzygy', 'y'))
print()
# The first argument to a method is always an instance of the class, so we can also use this notation to call the method:
print('syzygy'.count('y'))
print()

### Creating a Custom Class ###

# The str class has lots of useful methods; however, it doesn't have every possible method we might need.
# We can create a new class that customizes class str.
# Our class will have all of the str methods (open the terminal, start a python console/IDLE/IPython/etc and type:
# >>> help(str)
# to get a list of the methods), plus a new method that checks whether a string begins and ends with the same letter.

# We start our class definition with class WordplayStr(str).
# In this case, WordplayStr is the name of our new class, and the (str) indicates that our new class
# is based on the str class.
# WordplayStr is a subclass of str, which means that WordplayStr inherits all of the methods from str.
# Here is the completed class definition:

class WordplayStr(str):
    """
    A string that can report whether it has certain peculiar properties.
    """

    def same_start_and_end(self):
        """
        (WordplayStr) -> bool

        Precondition: len(self) != 0

        Return whether self begins and ends with the same letter.

        >>> s = WordplayStr('abracadabra')
        >>> s.same_start_and_end()
        True
        >>> s = WordplayStr('canoe')
        >>> s.same_start_and_end()
        False
        """
        return self[0] == self[-1]


if __name__=='__main__':
    import doctest
    doctest.testmod()  # If all tests pass, nothing will be printed out.

    test1 = WordplayStr('abracadabra')
    print(test1.same_start_and_end())
    print()
    test2 = 'shazam'
    print(WordplayStr.same_start_and_end(test2))
    print()
