def display_board(board):
    print(board[1]+"|"+board[2]+"|"+board[3])
    print(board[4]+"|"+board[5]+"|"+board[6])
    print(board[7]+"|"+board[8]+"|"+board[9])

def player_input():
    choose = ''
    while choose !='X' and choose !='O':
        choose = input("Player 1, choose 'X' or 'O': ")
        print("\n"*10)
    player1 = choose
    if player1 == 'X':
        player2 = 'O'
    else:
        player2 = 'X'
    return(player1, player2)

print(player_input())


