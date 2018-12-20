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

def update_board(board, selection):
    

 
def game(board):
    done = False
    turn=True
    while not done:
        player=get_player(turn)
        if player==1:
            selection=input('Player1 needs pick a column')
