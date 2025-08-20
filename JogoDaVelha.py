from random import randrange
from time import sleep


def display_board(board):
# A função aceita um parâmetro contendo o status atual da placa
# e o imprime no console.

	for l in range (3):
		for c in range (3):
			print(f'[{board[l][c]}]', end='')
		print()


def enter_move(board):
# A função aceita o status atual do tabuleiro, pergunta ao usuário sobre sua jogada, 
# verifica a entrada é válida e atualiza o quadro de acordo com a decisão do usuário.

	ok = False #Suposição falsa - precisamos dela para entrar no loop.
	while not ok:
		move = input('Digite seu movimento: ')
		ok = len(move) == 1 and move >= '1' and move <= '9' #A entrada do usuário é válida?			
		if not ok:
			print('Jogada inválida. Jogue de novo.') #Não, não é - faça a entrada novamente.
			continue
		move = int(move) - 1  #Número de célula de 0 a 8.
		row = move // 3 	  #Linha da célula.
		col = move % 3 	 	  #Coluna da célula.
		sgn = board[row][col] #Verifica o quadrado selecionado.
		ok = sgn not in ['O', 'X']
		if not ok: #Está ocupado - para a entrada novamente.
			print('Campo já ocupado. Repita a sua jogada. ')
			continue
	board[row][col] = 'O' #Define '0' no quadrado selecionado.


def make_list_of_free_fields(board):
# A função navega pelo tabuleiro e constrói uma lista de todas as casas livres; 
# a lista consiste em tuplas, enquanto cada tupla é um par de números de linha e coluna.

	free = []
	for row in range(3): #Iterar pelas linhas.
		for col in range(3): #Iterar pelas colunas.
			if board[row][col] not in ['O', 'X']: #A celula está livre?
				free.append((row,col)) #Sim, é - anexe uma nova tupla à lista.
	return free


def victory_for(board, sgn):
# A função analisa o estado da placa a fim de verificar se 
# o jogador usando 'O's ou 'X's ganhou o jogo

	if sgn == 'X': 		#Estamos procurando por X?
		who = 'pc' 		#Sim - é do lado do computador.
	elif sgn == 'O': 	#Estamos procurando por O?
		who = 'player' 	#Sim - é o nosso lado.
	else:
		who = None 		#Não devemos cair aqui.
	cross1 = cross2 = True #Para diagonais.
	for rc in range(3):
		if board[rc][0] == sgn and board[rc][1] == sgn and board[rc][2] == sgn: #Verifica a linha rc (row, column).
			return who
		if board[0][rc] == sgn and board[1][rc] == sgn and board[2][rc] == sgn: #Verifica a coluna rc (row, column).
			return who
		if board[rc][rc] != sgn: #Verifica a 1ª diagonal.
			cross1 = False
		if board[rc][2-rc] != sgn: #Verifica a segunda diagonal.
			cross2 = False
	if cross1 or cross2:
		return who
	return None


def draw_move(board):
# A função desenha o movimento do computador e atualiza o tabuleiro.

	free = make_list_of_free_fields(board) #Faça uma lista de campos livres.
	cnt = len(free)
	if cnt > 0:
		this = randrange(cnt)
		row, col = free[this]
		jogada_pc = board[row][col]
		board[row][col] = 'X'
		print(f'Jogada da máquina: {jogada_pc}')


board = [['1', '2', '3'], ['4', '5', '6'], ['7', '8', '9']] #Define o tabuleiro com um X no meio.
free = make_list_of_free_fields(board)
human_turn = False #Que turno é agora?
while len(free):
	if human_turn:
		print('-='*12)
		enter_move(board)
		win = victory_for(board, 'O')
		display_board(board)
		print('-='*12)
		for i in range (3):
			print('.', end='', flush = True)
			sleep(0.8)
	else:
		draw_move(board)
		display_board(board)
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
