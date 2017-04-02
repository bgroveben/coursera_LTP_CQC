# Do not import any modules. If you do, the tester may reject your submission.

# Constants for the contents of the maze.

# The visual representation of a wall.
WALL = '#'

# The visual representation of a hallway.
HALL = '.'

# The visual representation of a brussels sprout.
SPROUT = '@'

# Constants for the directions. Use these to make Rats move.

# The left direction.
LEFT = -1

# The right direction.
RIGHT = 1

# No change in direction.
NO_CHANGE = 0

# The up direction.
UP = -1

# The down direction.
DOWN = 1

# The letters for rat_1 and rat_2 in the maze.
RAT_1_CHAR = 'J'
RAT_2_CHAR = 'P'


class Rat:
    """ A rat caught in a maze. """

    def __init__(self, symbol, row, col, num_sprouts_eaten=0):
        """
        (Rat, str, int, int) -> NoneType

        A Rat object initialized with a symbol, location (row, col), and num_sprouts_eaten.

        >>> testrat = Rat('P',1,4)
        >>> testrat.symbol
        'P'
        >>> testrat.row
        1
        >>> testrat.col
        4
        >>> testrat.num_sprouts_eaten
        0
        """
        self.symbol = symbol
        self.row = row
        self.col = col
        self.num_sprouts_eaten = num_sprouts_eaten

    def set_location(self, row, col):
        """
        (Rat, int, int) -> NoneType

        Keep track of the rat's location by row and column.
        Set the rat's row and col instance variables to the given row and column.
        """
        pass

    def eat_sprout(self):
        """
        (Rat) -> NoneType

        Increment num_sprouts_eaten when the rat eats a sprout.

        >>> testrat = Rat('P',1,4)
        >>> testrat.num_sprouts_eaten
        0
        >>> testrat.eat_sprout()
        >>> testrat.num_sprouts_eaten
        1
        """
        self.num_sprouts_eaten += 1

        def __str__(self):
            """
            (Rat) -> str

            Return a string representation of the rat, in this format:
            symbol at (row, col) ate num_sprouts_eaten sprouts.
            """
            pass

class Maze:
    """ A 2D maze. """

    # Write your Maze methods here.


if __name__ == '__main__':
    # Do not import any modules. If you do, the tester may reject your submission.
    # Comment out the tests below before submitting.
    import doctest
    print(doctest.testmod())
