# Add equality method to our CashRegister class.

class CashRegister:
    """
    A cash register.
    """

    def __init__(self, loonies, toonies, fives, tens, twenties):
        """
        (CashRegister, int, int, int, int, int) -> NoneType

        A CashRegister with loonies, toonies, fives, tens, and twenties.
        """
        self.loonies = loonies
        self.toonies = toonies
        self.fives = fives
        self.tens = tens
        self.twenties = twenties


    # If we use the equality operator (==) without defining an __eq__() method for our class, then the __eq__() method
    # that is inherited from Python's object class (the base class that all other classes inherit from) is used.
    # Python's object.__eq__() method compares memory addresses, so that 2 different CashRegister instances with
    # equivalent amounts (like reg1 and reg2 in the doctest below) will evaluate to False instead of True.
    # Comment out the __eq__() method below and compare the file output.
    def __eq__(self, other):
        """
        (CashRegister, CashRegister) -> bool

        Return True iff this CashRegister has the same amount of money as other.

        >>> reg1 = CashRegister(2, 0, 0, 0, 0)
        >>> reg2 = CashRegister(0, 1, 0, 0, 0)
        >>> reg1 == reg2
        True
        """
        return self.get_total() == other.get_total()


    def get_total(self):
        """
        (CashRegister) -> int

        Return the total amount of cash in the register.
        """

        return self.loonies + self.toonies * 2 + self.fives * 5 + self.tens * 10 + self.twenties * 20


    def add(self, count, denomination):
        """
        (CashRegister, int, str) -> NoneType

        Add count items of denomination to the register.
        denomination is one of 'loonies', 'toonies', 'fives', 'tens' and 'twenties'.
        """
        if denomination == 'loonies':
            self.loonies += count
        elif denomination == 'toonies':
            self.toonies += count
        elif denomination == 'fives':
            self.fives += count
        elif denomination == 'tens':
            self.tens += count
        elif denomination == 'twenties':
            self.twenties += count


    def remove(self, count, denomination):
        """
        (CashRegister, int, str) -> NoneType

        Remove count items of denomination from the register.
        denomination is one of 'loonies', 'toonies', 'fives', 'tens', and 'twenties'
        """
        if denomination == 'loonies':
            self.loonies -= count
        elif denomination == 'toonies':
            self.toonies -= count
        elif denomination == 'fives':
            self.fives -= count
        elif denomination == 'tens':
            self.tens -= count
        elif denomination == 'twenties':
            self.twenties -= count



if __name__ == '__main__':
    cr1 = CashRegister(2, 0, 0, 0, 0)
    cr2 = CashRegister(0, 1, 0, 0, 0)
    cr3 = CashRegister(1, 1, 0, 0, 0)
    print()
    print("cr1: ")
    print(cr1)
    print()
    print("cr2: ")
    print(cr2)
    print()
    print("cr3: ")
    print(cr3)
    print()
    print("cr1 == cr2: ")
    print(cr1 == cr2)
    print()
    print("cr2 == cr3: ")
    print(cr3 == cr2)
    print()
