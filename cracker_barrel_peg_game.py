class PegGame():
    '''Implements the peg game from Cracker Barrel
    Diagram of spot numbers:
                 0
               1   2
             3   4   5
           6   7   8   9
    '''
    # spots that a peg can jump to from a given spot
    can_hop_to = {0: [3, 5], \
        1: [6, 8], \
        2: [7, 9], \
        3: [0, 5], \
        4: [], \
        5: [0, 3], \
        6: [1, 8], \
        7: [2, 9], \
        8: [1, 6], \
        9: [2, 7]}
        
    jumps = {(0, 3): 1, (0, 5): 2, \
             (1, 6): 3, (1, 8): 4, \
             (2, 7): 4, (2, 9): 5, \
             (3, 0): 1, (3, 5): 4, \
             (5, 0): 2, (5, 3): 4, \
             (6, 1): 3, (6, 8): 7, \
             (7, 2): 4, (7, 9): 8, \
             (8, 1): 4, (8, 6): 7, \
             (9, 2): 5, (9, 7): 8}
    
    def __init__(self, empty_spot=0):
        self._spot_status = [1]*10
        self._spot_status[empty_spot] = 0
        
    def is_legal_move(self, spot, hop_to):
        return (1 == self._spot_status[spot]) and (0 == self._spot_status[hop_to]) and ((spot, hop_to) in self.jumps) and (1 == self._spot_status[self.jumps[(spot, hop_to)]])
        
    def legal_moves(self, from_spot=None):
        '''Return an array of tuples with from,to spots which are legal moves.
        If from_spot is given, only return legal moves from that spot.'''
        moves = []
        if(from_spot == None):
            for from_spot in range(len(self._spot_status)):
                for to_spot in range(len(self._spot_status)):
                    if(self.is_legal_move(from_spot, to_spot)):
                        moves.append((from_spot, to_spot))
        else:
            for to_spot in self.can_hop_to[from_spot]:
                if(self.is_legal_move(from_spot, to_spot)):
                    moves.append((from_spot, to_spot))
        return moves
    
    def is_empty(self, spot):
        return 0 == self._spot_status[spot]
        
    def move(self, from_spot, to_spot):
        if(not self.is_legal_move(from_spot, to_spot)):
            raise ValueError('Not a legal move')
        self._spot_status[from_spot] = 0
        self._spot_status[to_spot] = 1
        self._spot_status[self.jumps[(from_spot, to_spot)]] = 0
        
    def pegs_left(self):
        return sum(self._spot_status)
        
def solve_peg_game(move_history=None, empty_starting_spot=None):
    if(empty_starting_spot is None):
        for i in range(10):
            solve_peg_game(move_history=None, empty_starting_spot = i)
        return
    p = PegGame(empty_starting_spot)
    if(move_history is not None):
        # re-play all the moves up to this point
        for m in move_history:
            p.move(m[0], m[1])
    else:
        move_history = []
    if(len(p.legal_moves()) == 0):
        if(1 == p.pegs_left()):
            print('Solved: %s; empty starting spot: %d' % (move_history, empty_starting_spot))
    else:
        for next_move in p.legal_moves():
            new_move_history = move_history.copy()
            new_move_history.append(next_move)
            solve_peg_game(new_move_history, empty_starting_spot)
            
if(__name__ == '__main__'):
    print('''Solutions to follow. Moves are listed as (from_spot, to_spot) where
    the board is numbered like so:
                 0
               1   2
             3   4   5
           6   7   8   9''')
    solve_peg_game()