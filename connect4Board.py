



class Board:
    def __init__(self, height, width):
        '''constructs board, initializes construction
        '''
        self.height = height
        self.width = width
        self.slots = [[' '] * self.width for row in range(self.height)]

    def __repr__(self):
        '''returns string representation of board object
        '''
        s = ''         # begin with an empty string

        # add one row of slots at a time
        for row in range(self.height):
            s += '|'   # one vertical bar at the start of the row

            for col in range(self.width):
                s += self.slots[row][col] + '|'

            s += '\n'  # newline at the end of the row
    
        # Add code here for the hyphens at the bottom of the board
        s += ((self.width * 2) + 1) * '-'
        # and the numbers underneath it.
        s += '\n'
        for num in range(self.width):
            s += ' ' + str(num % 10)
        return s

    def add_checker(self, checker, col):
        '''adds a checker to the connect 4 board
        '''
        assert(checker == 'X' or checker == 'O')
        assert(0 <= col < self.width)

        row = 0
        while self.slots[row][col] == ' ':
            if row == (self.height - 1):
                break
            else:
                row += 1
        if self.slots[row][col] != ' ':
            row -= 1
        self.slots[row][col] = checker

    def reset(self):
        '''resets board to empty spaces
        '''
        self.slots = [[' '] * self.width for row in range(self.height)]

    def add_checkers(self, colnums):
        """ takes in a string of column numbers and places alternating
            checkers in those columns of the called Board object, 
            starting with 'X'.
        """
        checker = 'X'   # start by playing 'X'

        for col_str in colnums:
            col = int(col_str)
            if 0 <= col < self.width:
                self.add_checker(checker, col)

            # switch to the other checker
            if checker == 'X':
                checker = 'O'
            else:
                checker = 'X'

    def can_add_to(self, col):
        '''checks to see if a checker can be added to a column
        '''

        if 0 <= col < self.width:
            if self.slots[0][col] == ' ':
                return True
            else:
                return False
        else:
            return False

    def is_full(self):
        ''' Checks to see if the Board object is full
        '''
        flag = True
        for col in range(self.width):
            flag = self.can_add_to(col)
            if flag == True:
                return False
        return True

    def remove_checker(self, col):
        ''' removes the top checker from of col, if there is one
        '''
        for row in range(self.height):
            if self.slots[-1][col] == ' ':
                break
            elif self.slots[row][col] != ' ':
                self.slots[row][col] = ' '
                break

    def is_horizontal_win(self, checker):
        """ Checks for a horizontal win for the specified checker.
        """
        for row in range(self.height):
            for col in range(self.width - 3):
                # Check if the next four columns in this row
                # contain the specified checker.
                if self.slots[row][col] == checker and \
                   self.slots[row][col + 1] == checker and \
                   self.slots[row][col + 2] == checker and \
                   self.slots[row][col + 3] == checker:
                    return True

        # if we make it here, there were no horizontal wins
        return False

    def is_vertical_win(self, checker):
        """ Checks for a vertical win for the specified checker.
        """
        for row in range(self.height - 3):
            for col in range(self.width):
                # Check if the next four columns in this row
                # contain the specified checker.
                if self.slots[row][col] == checker and \
                   self.slots[row + 1][col] == checker and \
                   self.slots[row + 2][col] == checker and \
                   self.slots[row + 3][col] == checker:
                    return True

        # if we make it here, there were no vertical wins
        return False

    def is_down_diagonal_win(self, checker):
        """ Checks for a downward diagonal win for the specified checker.
        """
        for row in range(self.height - 3):
            for col in range(self.width - 3):
                # Check if the next four columns in this row
                # contain the specified checker.
                if self.slots[row][col] == checker and \
                   self.slots[row + 1][col + 1] == checker and \
                   self.slots[row + 2][col + 2] == checker and \
                   self.slots[row + 3][col + 3] == checker:
                    return True

        # if we make it here, there were no downward diagonal wins
        return False
    
    def is_up_diagonal_win(self, checker):
        """ Checks for a upward diagonal win for the specified checker.
        """
        for row in range(3, self.height):
            for col in range(self.width - 3):
                # Check if the next four columns in this row
                # contain the specified checker.
                if self.slots[row][col] == checker and \
                   self.slots[row - 1][col + 1] == checker and \
                   self.slots[row - 2][col + 2] == checker and \
                   self.slots[row - 3][col + 3] == checker:
                    return True

        # if we make it here, there were no upward diagonal wins
        return False
    

    def is_win_for(self, checker):
        '''check to see if checker has 4 consecutive spots on the board
        '''
        if self.is_horizontal_win(checker) == True:
            return True
        elif self.is_vertical_win(checker) == True:
            return True
        elif self.is_down_diagonal_win(checker) == True:
            return True
        elif self.is_up_diagonal_win(checker) == True:
            return True
        else:
            return False
        
