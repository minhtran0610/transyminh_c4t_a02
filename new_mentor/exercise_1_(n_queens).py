size = int(input("Enter board size: "))
chess_board = [["-" for i in range(size)] for i in range(size)]
queen_position = []
visited = [False for i in range(size+1)]

def print_board():
    for i in range(len(chess_board)):
        print(*chess_board[i], end=' ')
        print()

def track(queen, number_of_queens):
    in_diagonal = False
    """ Check if queens were in diagonal position """
    for i in range(len(queen_position)-1):
        if abs(queen_position[i+1] - queen_position[i]) == 1:
            in_diagonal = True

    if queen == number_of_queens + 1 and not in_diagonal:
        print(queen_position)
        for i in range(len(queen_position)):
            chess_board[i][queen_position[i]-1] = "H"
        print_board()
        print()
        for i in range(len(queen_position)):
            chess_board[i][queen_position[i]-1] = "-"
        return
    
    for i in range(1, number_of_queens+1):
        if not visited[i]:
            queen_position.append(i)
            visited[i] = True
            track(queen+1, number_of_queens)
            visited[i] = False
            queen_position.pop()

track(1,size)
