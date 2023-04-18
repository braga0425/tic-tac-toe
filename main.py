def show_board(board):
    print("\n  0 1 2")
    for i in range(3):
        print(i, end=" ")
        for j in range(3):
            print(board[i][j], end=" ")
        print()


def winner_check(board, player):
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] == player:
            return True
        if board[0][i] == board[1][i] == board[2][i] == player:
            return True
    if board[0][0] == board[1][1] == board[2][2] == player:
        return True
    if board[0][2] == board[1][1] == board[2][0] == player:
        return True
    return False


def play_check(player):
    while True:
        play = input("\nJogador " + player + ", faça sua play (linha + coluna, com espaço entre os números): ")
        lin, col = play.split()

        if lin.isdigit() and col.isdigit() and int(lin) in range(3) and int(col) in range(3):
            return int(lin), int(col)

        print("\nJogada inválida, tente novamente.\n")


def play_tic_tac_toe():
    board = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]
    player = "X"

    while True:
        show_board(board)
        lin, col = play_check(player)
        if board[lin][col] != " ":
            print("\nJogada inválida, tente novamente.\n")
            continue

        board[lin][col] = player

        if winner_check(board, player):
            show_board(board)
            print("\nParabéns, jogador " + player + " venceu!")
            return

        if " " not in board[0] and " " not in board[1] and " " not in board[2]:
            show_board(board)
            print("\nEmpate!")
            return

        if player == "X":
            player = "O"
        else:
            player = "X"


play_again = True
while play_again:
    play_tic_tac_toe()
    response = input("\nDeseja jogar novamente? (s/n) ")
    play_again = (response.lower() == "s")
