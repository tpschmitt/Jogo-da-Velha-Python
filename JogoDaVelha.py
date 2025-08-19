from random import randrange


def display_board(board):
# A função aceita um parâmetro contendo o status atual da placa
# e o imprime no console.
	for l in range (3):
		for c in range (3):
			print(f'[{board[l][c]}]', end='')
		print()


def enter_move(board):
# A função aceita o status atual do tabuleiro, pergunta ao usuário sobre sua jogada, 
# verifica a entrada e atualiza o quadro de acordo com a decisão do usuário.
	ok = False
	while not ok:
		move = input('Digite seu movimento: ')
		ok = len(move) == 1 and move >= '1' and move <= '9'
		if not ok:
			print('Jogada inválida. Jogue de novo.')
			continue
		move = int(move) - 1
		row = move // 3
		col = move % 3
		sgn = board[row][col]
		ok = sgn not in ['O', 'X']
		if not ok:
			print('Campo já ocupado. Repita a sua jogada. ')
			continue
	board[row][col] = 'O'


def make_list_of_free_fields(board):
# A função navega pelo tabuleiro e constrói uma lista de todas as casas livres; 
# a lista consiste em tuplas, enquanto cada tupla é um par de números de linha e coluna.
	free = []
	for row in range(3):
		for col in range(3):
			if board[row][col] not in ['O', 'X']:
				free.append((row,col))
	return free


def victory_for(board, sgn):
# A função analisa o estado da placa a fim de verificar se 
# o jogador usando 'O's ou 'X's ganhou o jogo
	if sgn == 'X':
		who = 'pc'
	elif sgn == 'O':
		who = 'player'
	else:
		who = None
	cross1 = cross2 = True
	for rc in range(3):
		if board[rc][0] == sgn and board[rc][1] == sgn and board[rc][2] == sgn:
			return who
		if board[0][rc] == sgn and board[1][rc] == sgn and board[2][rc] == sgn:
			return who
		if board[rc][rc] != sgn:
			cross1 = False
		if board[rc][2-rc] != sgn:
			cross2 = False
	if cross1 or cross2:
		return who
	return None


def draw_move(board):
# A função desenha o movimento do computador e atualiza o tabuleiro.
	free = make_list_of_free_fields(board)
	cnt = len(free)
	if cnt > 0:
		this = randrange(cnt)
		row, col = free[this]
		board[row][col] = 'X'

board = [['1', '2', '3'], ['4', 'X', '6'], ['7', '8', '9']]
free = make_list_of_free_fields(board)
human_turn = True
while len(free):
	display_board(board)
	if human_turn:
		enter_move(board)
		win = victory_for(board, 'O')
	else:
		draw_move(board)
		win = victory_for(board, 'X')
	if win != None:
		break
	human_turn = not human_turn
	free = make_list_of_free_fields(board)


if win == 'player':
	print('Você venceu!!!')
elif win == 'pc':
	print('Você perdeu.')
else:
	print('Empatou.')
