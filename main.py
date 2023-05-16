import random

def show_board(board):
    print('\n')
    position = 1
    for i in range(3):
        for j in range(3):
            if board[i][j] == ' ':
                print(position, end=' ')
            else:
                print(board[i][j], end=' ')
            position += 1
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


def play_check(board, player):
    while True:
        if player == 'X':
            show_board(board)
            play = input('Jogador ' + player + ', faça sua jogada (posição de 1 a 9): ')
            position = int(play) - 1
        else:
            position = random.randint(0, 8)
            position += 1

        if position in range(9) and board[position // 3][position % 3] == ' ':
            return position

        print('\nJogada inválida, tente novamente!')


def play_tic_tac_toe():
    board = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]
    player = 'X'

    while True:
        position = play_check(board, player)

        board[position // 3][position % 3] = player

        if winner_check(board, player):
            show_board(board)
            if player == 'X':
                print('\nParabéns, Jogador ' + player + ' ganhou!')
            else:
                print('\nDesculpe, você perdeu para a máquina!')
            return

        if all(board[i][j] != ' ' for i in range(3) for j in range(3)):
            show_board(board)
            print('\nEmpate!')
            return

        if player == 'X':
            player = 'O'
        else:
            player = 'X'


play_again = True
while play_again:
    play_tic_tac_toe()
    response = input('\nVocê gostaria de jogar de novo? (y/n) ')
    play_again = (response.lower() == 'y')
