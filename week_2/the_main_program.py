### Writing a '__main__' program ###

# Look at the files palindrome_v1.py and palindrome_v2.py for examples.

# Python's __name__ variable

# Every module has a variable named __main__.
# Since this variable is special (it is built into Python), its name begins and ends with double underscores.
# If the function call print("I am", __name__) is included in a file, then when the module is executed, "I am __main__"
# will be printed out.
# However, if module_1 is imported into module_2, then executing module_2 will print out "I am module_1".
# In other words, __name__ will refer to "__main__" only if it is referenced inside the module being run.
# In all other cases, __name__ will refer to a string containing the module name.

### Using if __name__ == '__main__': ###

# We can use an if statement to check whether a module is tha main one being executed.
# If it is, only then will certain lines of code be executed.

if __name__ == '__main__':
    print("This line is being executed because this is the main module.")

# For the code above, if the variable __name__ doesn't refer to "__main__" (don't forget the quotes),
# then the code in the body of the if statement won't be executed.
