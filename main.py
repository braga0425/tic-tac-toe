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


def play_check(board, player, game_mode):
    while True:
        if game_mode == '1' or player == 'X':
            show_board(board)
            play = input('Jogador ' + player + ', faça sua jogada (posição de 1 a 9): ')
            position = int(play) - 1
        else:
            position = random.randint(0, 8)

        if position in range(9) and board[position // 3][position % 3] == ' ':
            return position

        print('\nJogada inválida, tente novamente!')


def play_tic_tac_toe():
    board = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]
    players = ['X', 'O']
    random.shuffle(players)
    current_player = players[0]
    game_mode = input('Escolha o modo de jogo:\n1. Jogar contra outra pessoa\n2. Jogar contra a máquina\nDigite o número correspondente: ')

    while True:
        position = play_check(board, current_player, game_mode)

        board[position // 3][position % 3] = current_player

        if winner_check(board, current_player):
            show_board(board)
            if current_player == 'X':
                print('\nParabéns, Jogador ' + current_player + ' ganhou!')
            else:
                if game_mode == '2':
                    print('\nDesculpe, você perdeu para a máquina!')
                else:
                    print('\nParabéns, Jogador ' + current_player + ' ganhou!')
            return

        if all(board[i][j] != ' ' for i in range(3) for j in range(3)):
            show_board(board)
            print('\nEmpate!')
            return

        current_player = players[1] if current_player == players[0] else players[0]


play_again = True
while play_again:
    play_tic_tac_toe()
    response = input('\nVocê gostaria de jogar de novo? (s/n) ')
    play_again = (response.lower() == 's')
