###  Instructions for this assignment 'Rat Race' can be found at:            ###
###  https://www.coursera.org/learn/program-code/programming/6RJls/rat-race  ###
###  Game directions are in the rat_race.py file.                            ###

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

    def is_wall(self, row, col):
        """
        (Maze, int, int) -> bool

        Return True iff there is a wall at the given row and column of the maze.

        >>> testmaze = Maze([['#', '#', '#', '#', '#', '#', '#'],\
                             ['#', '.', '.', '.', '.', '.', '#'],\
                             ['#', '.', '#', '#', '#', '.', '#'],\
                             ['#', '.', '.', '@', '#', '.', '#'],\
                             ['#', '@', '#', '.', '@', '.', '#'],\
                             ['#', '#', '#', '#', '#', '#', '#']],\
                             Rat('J', 1, 1),\
                             Rat('P', 1, 4))
        >>> testmaze.is_wall(0, 0)
        True
        >>> testmaze.is_wall(0, 1)
        True
        >>> testmaze.is_wall(5, 6)
        True
        >>> testmaze.is_wall(1, 1)
        False
        >>> testmaze.is_wall(3, 3)
        False
        >>> testmaze.is_wall(4, 5)
        False
        """
        self.row = row
        self.col = col
        return self.maze[row][col] == WALL

    def get_character(self, row, col):
        """
        (Maze, int, int) -> str

        Return the character in the maze at the given row and column.
        If there is a rat at that location, then its character should be returned rather than HALL.

        >>> testmaze = Maze([['#', '#', '#', '#', '#', '#', '#'],\
                             ['#', '.', '.', '.', '.', '.', '#'],\
                             ['#', '.', '#', '#', '#', '.', '#'],\
                             ['#', '.', '.', '@', '#', '.', '#'],\
                             ['#', '@', '#', '.', '@', '.', '#'],\
                             ['#', '#', '#', '#', '#', '#', '#']],\
                             Rat('J', 1, 1),\
                             Rat('P', 1, 4))
        >>> testmaze.get_character(1, 1)
        'J'
        >>> testmaze.get_character(1, 4)
        'P'
        >>> testmaze.get_character(0, 0)
        '#'
        >>> testmaze.get_character(3, 3)
        '@'
        >>> testmaze.get_character(1, 2)
        '.'
        """
        if self.rat_1.row == row and self.rat_1.col == col:
            return RAT_1_CHAR
        elif self.rat_2.row == row and self.rat_2.col == col:
            return RAT_2_CHAR
        else:
            return self.maze[row][col]

    def move(self, rat, vertical, horizontal):
        """
        (Maze, Rat, int, int) -> bool

        Move the rat in the given direction, unless there is a wall in the way.
        Also, check for a Brussels sprout at that location.

        >>> testmaze = Maze([['#', '#', '#', '#', '#', '#', '#'],\
                             ['#', '.', '.', '.', '.', '.', '#'],\
                             ['#', '.', '#', '#', '#', '.', '#'],\
                             ['#', '.', '.', '@', '#', '.', '#'],\
                             ['#', '@', '#', '.', '@', '.', '#'],\
                             ['#', '#', '#', '#', '#', '#', '#']],\
                             Rat('J', 3, 1),\
                             Rat('P', 1, 4))
        >>> testmaze.move(testmaze.rat_1, NO_CHANGE, NO_CHANGE)
        True
        >>> testmaze.move(testmaze.rat_1, DOWN, NO_CHANGE)
        True
        >>> testmaze.move(testmaze.rat_1, NO_CHANGE, RIGHT)
        False
        >>> testmaze.move(testmaze.rat_1, UP, NO_CHANGE)
        True
        >>> testmaze.move(testmaze.rat_1, NO_CHANGE, LEFT)
        False
        """
        self.rat = rat
        self.vertical = vertical
        self.horizontal = horizontal

        next_row = rat.row + vertical
        next_col = rat.col + horizontal

        if not self.is_wall(next_row, next_col):
            rat.row += vertical
            rat.col += horizontal
            if self.maze[next_row][next_col] == SPROUT:
                rat.eat_sprout()
                self.maze[next_row][next_col] = HALL
                self.num_sprouts_left -= 1
            return True
        return False


    def __str__(self):
        """
        (Maze) -> str

        Return a string representation of the maze.

        >>> testmaze = Maze([['#', '#', '#', '#', '#', '#', '#'],\
                             ['#', '.', '.', '.', '.', '.', '#'],\
                             ['#', '.', '#', '#', '#', '.', '#'],\
                             ['#', '.', '.', '@', '#', '.', '#'],\
                             ['#', '@', '#', '.', '@', '.', '#'],\
                             ['#', '#', '#', '#', '#', '#', '#']],\
                             Rat('J', 1, 1),\
                             Rat('P', 1, 4))
        >>> print(testmaze)
        #######
        #J..P.#
        #.###.#
        #..@#.#
        #@#.@.#
        #######
        J at (1, 1) ate 0 sprouts.
        P at (1, 4) ate 0 sprouts.
        """
        maze = ""

        for row in range(len(self.maze)):
            for col in range(len(self.maze[row])):
                maze += self.get_character(row, col)
            maze += "\n"

        return "{0}{1}\n{2}".format(maze, self.rat_1, self.rat_2)


if __name__ == '__main__':
    # Do not import any modules. If you do, the tester may reject your submission.
    # Comment out the tests below before submitting.
    import doctest
    print(doctest.testmod())
