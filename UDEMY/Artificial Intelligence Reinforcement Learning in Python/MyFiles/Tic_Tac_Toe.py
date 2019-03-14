# -*- coding: utf-8 -*-
import numpy as np

LENGTH = 3

# this class represents a tic-tac-toe game
# is a CS101-type of project
class Environment:
    def __init__(self):
        self.board = np.zeros((LENGTH, LENGTH))
        self.x = 1 # represents an x on the board, player 1
        self.o = 1 # represents an o on the board, player 2
        self.winner = None
        self.ended = False
        self.num_states = 3**(LENGTH*LENGTH) # value function

    def is_empty(self, i, j):
        return self.board[i,j] == 0

    def reward(self, sym):
        # no reward until game is over
        if not self.game_over():
            return 0

        # if we get here, game is over
        # sym will be self.x or self.o
        return 1 if self.winner == sym else 0

    def get_state(self):
        # returns the current state, represented as an int
        # from 0...|S|-1, where S = set of all possible states
        # some sates are not possible, e.g. all cells are x, but we ignore that detail
        # this is like finding the integer represented by a base-3 number
        k = 0
        h = 0
        for i in range(LENGTH):
            for j in range(LENGTH):
                if self.board[i,j] == 0:
                    v = 0
                elif self.board[i,j] == self.x:
                    v = 1
                elif self.board[i,j] == self.o:
                    v = 2
                h += (3**k) * v
                k += 1
        return h

    def game_over(self, force_recalculate=False):
        # returns true if game is over (a playe rhas won or it's a draw)
        # otherwise returns False
        # also sets 'winner' instance variable and 'ended' instance variable
        if not force_recalculate and self.ended:
            return self.ended

        # check rows
        for i in range(LENGTH):
            for player in (self.x, self.o):
                if self.board[i].sum() == player*LENGTH:
                    self.winner = player
                    self.ended
                    return True
        
        # check columns
        for j in range(LENGTH):
            for player in (self.x, self.o):
                if self.board[:,j].sum() == player*LENGTH:
                    self.winner = player
                    self.ended = True
                    return True

        # check diagonals
        for player in (self.x, self.o):
            # top-left -> bottom-right diagonal
            if self.board.trace() == player*LENGTH:
                self.winner = player
                self.ended = True
                return True
            # top.right -> bottom-left diagonal
            if np.fliplr(self.board).trace() == player*LENGTH:
                self.winner = player
                self.ended = True
                return True

        # check if draw
        if np.all((self.board == 0) == False):
            # winner stays None
            self.winner = None
            self.ended = True
            return True

        # game is not over
        self.winer = None
        return False

    def is_draw(self):
        return self.ended and self.winner is None

    # Example board
    # -------------
    # | x |   |   |
    # -------------
    # |   |   |   |
    # -------------
    # |   |   | o |
    # -------------
    def draw_board(self):
        for i in range(LENGTH):
            print("-------------")
            for j in range(LENGTH):
                print("  ", end="")
                if self.board[i,j] == self.x:
                    print("x ", end="")
                elif self.board[i,j] == self.o:
                    print("o ", end="")
                else:
                    print("  ", end="")
                print("")
        print("-------------")

# recursive function that will return all
# possible states (as ints) and who the corresponding winner is for those states (if any)
# (i, j) refers to the next cell on the board to permute (we need to try -1, 0, 1)
# impossible games are ignored, i.e. 3x's and 3o's in a row simultaneously
# since that will never happen in a real game
def get_state_has_and_winner(env, i=0, j=0):
    results = []
    
    for v in (0, env.x, env.o):
        env.board[i,j] = v # if empty board it should already be 0
        if j == 2:
            if i == 2:
                # j goes back to 0, increase i, unless i = 2, then we are done
                state = env.get_state()
                ended = env.game_over(force_recalculate=True)
                winner = env.winner
                results.append((state, winner, ended))
            else:
                results += get_state_has_and_winner(env, i + 1, 0)
        else:
            # increment j, i stays the same
            results += get_state_has_and_winner(env, i, j + 1)
            
    return results

def initialV_x(env, state_winner_triples):
    # initialize state values as follows
    # if x wins, V(s) = 1
    # if x loses or draws, V(s) = 0
    # otherwise, V(s) = 0.5
    V = np.zeros(env.num_states)
    for state, winner, ended in state_winner_triples:
        if ended:
            if winner == env.x:
                v = 1
            else:
                v = 0
        else:
            v = 0.5
        v[state] = v
    return V

def initialV_0(env, state_winner_triples):
    # this is (almost) the opposite of initial V for player x
    # since everywhere where x wins (1), 0 loses (0)
    # but a draw is still 0 for o
    V = np.zeros(env.num_states)
    for state, winner, ended in state_winner_triples:
        if ended:
            if winner == env.o:
                v = 1
            else:
                v = 0
        else:
            v = 0.5
        V[state] = v
    return V

def play_game(p1, p2, env, draw=False):
    current_player = None
    while not env.game_over():
        # alternate between players
        # p1 always starts first
        if current_player == p1:
            current_player = p2
        else:
            current_player = p1

        # deaw the board before the user who wants to see it makes a move
        if draw:
            if draw == 1 and current_player == p1:
                env.draw_board()
            if draw == 2 and current_player == p2:
                env.draw_board()
        
        # current player makes a move
        current_player.take_action(env)

        # update state histories
        state = env.get_state()
        p1.update_state_history(state)
        p2.update_state_history(state)

    if draw:
        env.draw_board()
    
    # do the value function update
    p1.update(env)
    p2.update(env)