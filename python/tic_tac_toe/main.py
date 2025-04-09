'''
make a tic tac toe game as a programming exercise
'''
from typing import List


def get_board(row_count=3, col_count=3) -> List[List[None]]:
    'game board init to empty'
    return [[None for _ in range(col_count)] for _ in range(row_count)]


def init(shared_state: dict):
    'pre game setup'
    shared_state['board'] = get_board()
    shared_state['who_is_next'] = 'X'

    draw_board(shared_state)


def check_for_win(shared_state: dict):
    'check the win lines'
    winner = None
    win_lines = [
        [(0, 0), (0, 1), (0, 2)],
        [(1, 0), (1, 1), (1, 2)],
        [(2, 0), (2, 1), (2, 2)],
    ]

    for wl in win_lines:
        cnt = 0
        w = None
        #import pdb; pdb.set_trace()

        for i in range(len(wl) - 1):  # note the - 1
            r1, c1 = wl[i]
            r2, c2 = wl[i + 1]

            if shared_state['board'][r1][c1] and shared_state['board'][r1][c1] == shared_state['board'][r2][c2]:
                if not w:
                    w = shared_state['board'][r1][c1]
                cnt += 1

        if cnt >= len(wl) - 1:
            winner = w
            break

    return winner


def play(shared_state: dict):
    '''
    play the game and return true when done
    '''

    done = False

    print(f'\nit\'s {shared_state["who_is_next"]} turn!\n')
    r = int(input('row: '))
    c = int(input('col: '))

    if r >= 0 and r < len(shared_state['board']) and c >= 0 and c < len(shared_state['board'][0]) and not shared_state['board'][r][c]:

        if shared_state['who_is_next'] == 'X':
            shared_state['board'][r][c] = 'X'
            shared_state['who_is_next'] = 'O'
        else:
            shared_state['board'][r][c] = 'O'
            shared_state['who_is_next'] = 'X'
        winner = check_for_win(shared_state)
        if winner:
            print(f'winner is: {winner}.')
            done = True
    else:
        print(f'out of range: {r} {c} or taken.')
        done = True

    return done


def draw_board(shared_state: dict):
    'draw the board to the terminal'
    for r in range(len(shared_state['board'])):
        print('\n')
        for c in range(len(shared_state['board'][r])):
            print(f'{shared_state['board'][r][c]}, ', end='')


def shutdown():
    'clean up'
    print('well done!')


def run():
    'main loop'

    shared_state = {}
    init(shared_state)

    while not play(shared_state):
        draw_board(shared_state)

    shutdown()


if __name__ == '__main__':
    run()
