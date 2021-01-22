#
# ps9pr3.py  (Problem Set 9, Problem 3)
#
# Playing the game 
#   

from connect4Board import Board
from connect4Player import Player

import random
   
def connect_four(p1, p2):
    """ Plays a game of Connect Four between the two specified players,
        and returns the Board object as it looks at the end of the game.
        inputs: p1 and p2 are objects representing Connect Four
          players (objects of the Player class or a subclass of Player).
          One player should use 'X' checkers and the other should
          use 'O' checkers.
    """
    # Make sure one player is 'X' and one player is 'O'.
    if p1.checker not in 'XO' or p2.checker not in 'XO' \
       or p1.checker == p2.checker:
        print('need one X player and one O player.')
        return None

    print('Welcome to Connect Four!')
    print()
    b = Board(6, 7)
    print(b)
    flag = True 
    
    while True:
        if process_move(p1, b) == True:
            return b
        if process_move(p2, b) == True:
            return b

        
    print("Thanks for playing!")
def process_move(p, b):
    '''processes a single player move
    '''
    
    nmove = p.next_move(b)
    nmove = int(nmove)
    b.add_checker(p.checker, nmove)
    print('\n')
    print(b)

    if b.is_win_for(p.checker) == True:
        
        print(str(p) + ' wins in ' + str(p.num_moves))
        False
        
    elif b.is_full() == True:
        print("It's a tie!")
        False
        
    else:
        #add case for when game is not over, we should't
        #keep printing the board when the game is over
        print(str(p) + "'s turn")

class RandomPlayer(Player):
    import random

    def next_move(self, b):
        '''overrides next_move method to choose a random column for unintelligent player
        '''
        checker = self.checker
        super().__init__(checker)
        choicelist = [x for x in range(b.width) if b.can_add_to(x) == True]
        col = random.choice(choicelist)
        return col        

    
class AIPlayer(Player):
    def __init__(self, checker, tiebreak, lookahead):
        '''constructor for AIplayer
        '''
        assert(checker == 'X' or checker == 'O')
        assert(tiebreak == 'LEFT' or tiebreak == 'RIGHT' or tiebreak == 'RANDOM')
        assert(lookahead >= 0)
        super().__init__(checker)
        self.tiebreak = tiebreak
        self.lookahead = lookahead

    def __repr__(self):
        '''indicates what checker the Player object is using
        '''
        super().__repr__()
        s = 'Player ' + self.checker + ' (' + self.tiebreak + ', ' + str(self.lookahead) + ')'
        return s

    def max_score_column(self, scores):
        '''returns index of highest score of possible columns
            if there is a tie, it will utilize tiebreak preference
        '''
        highestscore = max(scores)
        indexlist = [index for index in range(len(scores)) if highestscore == scores[index]]
        if self.tiebreak == 'LEFT':
            return indexlist[0]
        elif self.tiebreak == 'RIGHT':
            return indexlist[-1]
        elif self.tiebreak == 'RANDOM':
            choice = random.choice(indexlist)
            return choice

    def scores_for(self, b):
        ''''''
        scores = [0 for x in range(b.width)]
        for column in range(b.width):
            if b.can_add_to(column) == False:
                scores[column] = -1
            elif b.is_win_for(self.checker) == True:
                scores[column] = 100
            elif b.is_win_for(self.opponent_checker()) == True:
                scores[column] = 0
            elif self.lookahead == 0:
                scores[column] = 50
            else:
                b.add_checker(self.checker, column)
                opponent = AIPlayer(self.opponent_checker(), self.tiebreak, self.lookahead - 1)
                opponentscore = opponent.scores_for(b)
                if max(opponentscore) == 0:
                    scores[column] = 100
                elif max(opponentscore) == 100:
                    scores[column] = 0
                elif max(opponentscore) == 50:
                    scores[column] = 50
                b.remove_checker(column)
        return scores
    
    def next_move(self, b):
        '''overrides next_move method to choose a random column for unitelligent player
        '''
        checker = self.checker
        super().__init__(checker)
        self.num_moves += 1
        scorelist = self.scores_for(b)
        suggestion = self.max_score_column(scorelist)
        return suggestion