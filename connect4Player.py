#
# ps9pr2.py  (Problem Set 9, Problem 2)
#
# A Connect-Four Player class 
#  

from connect4Board import Board

# write your class below

class Player:

    def __init__(self, checker):
        ''' initializes player class
        '''
        assert(checker == 'X' or checker == 'O')
        self.checker = checker
        self.num_moves = 0

    def __repr__(self):
        '''indicates what checker the Player object is using
        '''
        s = 'Player ' + self.checker
        return s

    def opponent_checker(self):
        ''' returns value of opponent's checker
        '''
        if self.checker == 'X':
            return 'O'
        else:
            return 'X'

    def next_move(self, b):
        '''keeps track of player turns as well as checks to see if next move is valid
        '''
        self.num_moves += 1

        while True:
            col = int(input('Enter a column: '))
            if b.can_add_to(col) == True:
                return col
            else:
                print('Try again!')

                            
