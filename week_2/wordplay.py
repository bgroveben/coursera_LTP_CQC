# Create a custom class that is a subclass of str.

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
    print(doctest.testmod())
