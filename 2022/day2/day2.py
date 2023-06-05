"""
Refs
https://panda.ime.usp.br/pensepy/static/pensepy/10-Arquivos/files.html
"""
import os

dirname = os.path.dirname("/home/anderson/Documentos/Programação/2022/day2/")
file = os.path.join(dirname, 'day2.txt')

# A and X = Rock(1)
# B and Y = Paper(2)
# C and Z = Scissors(3)
# Score = Lose(0), Draw(3), Victory(6)
elfo, meu = [], []
lose = 0
draw = 3
victory = 6
X = 1
Y = 2
Z = 3


def read_jokenpo(arquivo):
	
	arquivo = open(arquivo, 'r')
	item = 0	
	for linha in arquivo.readlines():
		elfo.append(linha[0])
		meu.append(linha[2])
	arquivo.close()


def jokenpo_letras(player1, player2):
	# Primeira parte / Part 1
	score = []

	for i in range(len(elfo)):
		# Se o elfo jogar Pedra(A) / If elf choose Rock(A)
		if player1[i] == "A" and player2[i] == "X":
			score.append(draw + X)

		elif player1[i] == "A" and player2[i] == "Y":
			score.append(victory + Y)

		elif player1[i] == "A" and player2[i] == "Z":
			score.append(lose + Z)

		# Se o elfo jogar Papel(B) / If elf choose Paper(B)
		elif player1[i] == "B" and player2[i] == "X":
			score.append(lose + X)

		elif player1[i] == "B" and player2[i] == "Y":
			score.append(draw + Y)

		elif player1[i] == "B" and player2[i] == "Z":
			score.append(victory + Z)

		# Se o elfo jogar Tesoura(C) / If elf choose Scissors(C)
		elif player1[i] == "C" and player2[i] == "X":
			score.append(victory + X)

		elif player1[i] == "C" and player2[i] == "Y":
			score.append(lose + Y)

		elif player1[i] == "C" and player2[i] == "Z":
			score.append(draw + Z)
	print(sum(score))


def jokenpo_final(player1, player2):
	# Segunda Parte / Part two
	score = []
	for i in range(len(elfo)):
		# Se o elfo jogar Pedra(A) / If elf choose Rock(A)
		if player1[i] == "A":
			if player2[i] == "X":
				score.append(Z + lose)
			elif player2[i] == "Y":
				score.append(X + draw)
			elif player2[i] == "Z":
				score.append(Y + victory)
		# Se o elfo jogar Papel(B) / If elf choose Paper(B)
		elif player1[i] == "B":
			if player2[i] == "X":
				score.append(X + lose)
			elif player2[i] == "Y":
				score.append(Y + draw)
			elif player2[i] == "Z":
				score.append(Z + victory)
		# Se o elfo jogar Tesoura(C) / If elf choose Scissors(C)
		elif player1[i] == "C":
			if player2[i] == "X":
				score.append(Y + lose)
			elif player2[i] == "Y":
				score.append(Z + draw)
			elif player2[i] == "Z":
				score.append(X + victory)
	print(sum(score))


read_jokenpo(file)
jokenpo_letras(elfo, meu)
jokenpo_final(elfo, meu)
