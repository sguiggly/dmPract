board = []
 
for row in range(6):
  board.append([])
  for column in range(7):
    board[row].append('.')
 
def print_board(board):
  for row in board:
    print( " ".join(row))

def get_player(turn):
    if turn:
        player=1
    else:
        player=2
    return player

def update_board(board, selection, player):
    row=5
    while row>=0:
        if board[row][selection]=='.':
            if player==1:
                board[row][selection]='x'
            else:
                board[row][selection]='o'
            break
        else:
            row-=1
    return board

def is_valid(board, selection):
    try:
       selection = int(selection)
    except ValueError:
       return False

    if selection in range(6): 
        if board[0][selection]=='.':
            return True
    else:
        return False

def check_win(board,player):
    boardHeight = len(board[0])
    boardWidth = len(board)
    if player==1:
        tile='x'
    else:
        tile='o'
    # check horizontal spaces
    for y in range(boardHeight):
        for x in range(boardWidth - 3):
            if board[x][y] == tile and board[x+1][y] == tile and board[x+2][y] == tile and board[x+3][y] == tile:
                return True

    # check vertical spaces
    for x in range(boardWidth):
        for y in range(boardHeight - 3):
            if board[x][y] == tile and board[x][y+1] == tile and board[x][y+2] == tile and board[x][y+3] == tile:
                return True

    # check / diagonal spaces
    for x in range(boardWidth - 3):
        for y in range(3, boardHeight):
            if board[x][y] == tile and board[x+1][y-1] == tile and board[x+2][y-2] == tile and board[x+3][y-3] == tile:
                return True

    # check \ diagonal spaces
    for x in range(boardWidth - 3):
        for y in range(boardHeight - 3):
            if board[x][y] == tile and board[x+1][y+1] == tile and board[x+2][y+2] == tile and board[x+3][y+3] == tile:
                return True

    return False

 
def game(board):
    print_board(board)
    done = False
    turn=True
    while not done:
        player=get_player(turn)
        selection=input('Player'+str(player)+' needs pick a column')
        while not is_valid(board,selection):
            selection=input('not a valid move, pick a new column')
        update_board(board,int(selection),player)
        if check_win(board,player):
            print('Player'+str(player)+' wins!')
            done=True
        else:
            turn=not turn
        print_board(board)

game(board)
