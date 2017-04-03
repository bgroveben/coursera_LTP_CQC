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

        A Rat object initialized with a symbol, row location, column location, and num_sprouts_eaten.

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

        Set the rat's row and col instance variables to the given row and column.

        >>> testrat = Rat('P',1,4)
        >>> testrat.row
        1
        >>> testrat.col
        4
        """
        self.row = row
        self.col = col

    def eat_sprout(self):
        """
        (Rat) -> NoneType

        Increment num_sprouts_eaten when the rat eats a sprout.

        >>> testrat1 = Rat('P',1,4)
        >>> testrat2 = Rat('J',2,2)
        >>> testrat1.num_sprouts_eaten
        0
        >>> testrat2.num_sprouts_eaten
        0
        >>> testrat1.eat_sprout()
        >>> testrat1.num_sprouts_eaten
        1
        >>> testrat2.eat_sprout()
        >>> testrat2.num_sprouts_eaten
        1
        >>> testrat1.eat_sprout()
        >>> testrat1.num_sprouts_eaten
        2
        >>> testrat2.eat_sprout()
        >>> testrat2.num_sprouts_eaten
        2
        """
        self.num_sprouts_eaten += 1

    def __str__(self):
        """
        (Rat) -> str

        Return a string representation of the rat, in this format:
        symbol at (row, col) ate num_sprouts_eaten sprouts.

        >>> testrat = Rat('J',4,3,num_sprouts_eaten=2)
        >>> testrat.__str__()
        'J at (4, 3) ate 2 sprouts.'
        """
        return '{0} at ({1}, {2}) ate {3} sprouts.'.format(self.symbol, self.row, self.col, self.num_sprouts_eaten)


class Maze:
    """ A 2D maze. """

    def __init__(self, maze, rat_1, rat_2, num_sprouts_left=2):
        """
        (Maze, list of list of str, Rat, Rat) -> NoneType

        Create Maze object with maze contents, rat_1, rat_2, and number of uneaten sprouts.

        >>> testmaze = Maze([['#', '#', '#', '#', '#', '#', '#'],\
                             ['#', '.', '.', '.', '.', '.', '#'],\
                             ['#', '.', '#', '#', '#', '.', '#'],\
                             ['#', '.', '.', '@', '#', '.', '#'],\
                             ['#', '@', '#', '.', '@', '.', '#'],\
                             ['#', '#', '#', '#', '#', '#', '#']],\
                             Rat('J', 1, 1),\
                             Rat('P', 1, 4))
        >>> testmaze.maze
        [['#', '#', '#', '#', '#', '#', '#'], ['#', '.', '.', '.', '.', '.', '#'], ['#', '.', '#', '#', '#', '.', '#'], ['#', '.', '.', '@', '#', '.', '#'], ['#', '@', '#', '.', '@', '.', '#'], ['#', '#', '#', '#', '#', '#', '#']]
        >>> print(testmaze.rat_1)
        J at (1, 1) ate 0 sprouts.
        >>> print(testmaze.rat_2)
        P at (1, 4) ate 0 sprouts.
        >>> testmaze.num_sprouts_left
        2
        """
        self.maze = maze
        self.rat_1 = rat_1
        self.rat_2 = rat_2
        self.num_sprouts_left = num_sprouts_left

    def is_wall():
        """
        (Maze, int, int) -> bool
        """
        pass

    def get_character():
        """
        (Maze, int, int) -> str
        """
        pass

    def move():
        """
        (Maze, Rat, int, int) -> bool
        """
        pass

    def __str__():
        """
        (Maze) -> str
        """
        pass


if __name__ == '__main__':
    # Do not import any modules. If you do, the tester may reject your submission.
    # Comment out the tests below before submitting.
    import doctest
    print(doctest.testmod())
