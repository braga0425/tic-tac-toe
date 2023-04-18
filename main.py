def show_board(board):
    print("\n  0  1  2")
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

def play_tic_tac_toe():
    board = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]
    player = "X"

    while True:
        show_board(board)
        jogada = input("\nJogador " + player + ", faça sua jogada (linha + coluna, com espaço entre os números): ")
        linha, coluna = jogada.split()
        linha = int(linha)
        coluna = int(coluna)

        if board[linha][coluna] != " ":
            print("\nJogada inválida, tente novamente.\n")
            continue

        board[linha][coluna] = player

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

play_tic_tac_toe()
