import numpy
board = []
counter = 0

def win_check(player):
    # win horizontally
    player_win = 0
    if board[0] == board[1] == board[2] == player or board[3] == board[4] == board[5] == player or board[6] == board[7] == board[8] == player:
        player_win += 1
    # win vertically
    elif board[0] == board[3] == board[6] == player or board[1] == board[4] == board[7] == player or board[2] == board[5] == board[8] == player:
        player_win += 1
    # win diagonally
    elif board[0] == board[4] == board[8] == player or board[2] == board[4] == board[6] == player:
        player_win += 1

    return player_win


def track(_level, _maxlevel):
    if _level == _maxlevel + 1:
        global counter
        # # counter += 1
        # print(board, counter)
        num_x = 0
        num_o = 0
        for i in board:
            if i == "x":
                num_x += 1
            elif i == "o":
                num_o +=1
        x_win = win_check("x")
        o_win = win_check("o")

        # legal check
        # draw
        legal = False
        if x_win == o_win == 0 and num_x == 5 and num_o == 4:
            legal = True
        # x win
        elif x_win == 1 and o_win == 0 and num_x - num_o == 1:
            legal = True
        # o win
        elif x_win == 0 and o_win == 1 and num_o == num_x:
            legal = True
        # x has double move:
        elif x_win == 2 and o_win == 0 and num_x == 5 and num_o == 4:
           legal = True

        # print board
        if legal:
            counter += 1
            print(numpy.reshape(board, (3, 3)), counter)

        return
             
    for j in ["-", "x", "o"]:
        # print(j, _level-1, visited)
        if j not in visited[_level-1]:
            board.append(j)
            visited[_level-1].append(j)
            track(_level+1, _maxlevel)
            visited[_level-1].pop()
            board.pop()

visited = []
for i in range(9):
    visited.append([])
track(1, 9)


