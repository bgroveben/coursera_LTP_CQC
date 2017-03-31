# Like everything else in Python, functions are objects.
# Since functions are objects, they can be supplied as arguments to other functions.

def function_runner(f):
    """
    (function) -> NoneType

    Call f().
    """
    f()

def function_the_first():
    print("function_the_first was called, sucka.")

def function_the_second():
    print("function_the_second was called, sucka.")


if __name__ == '__main__':
    print()
    function_runner(function_the_first)
    print()
    function_runner(function_the_second)
    print()
