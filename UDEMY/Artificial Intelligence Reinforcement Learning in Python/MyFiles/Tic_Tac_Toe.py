# -*- coding: utf-8 -*-

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