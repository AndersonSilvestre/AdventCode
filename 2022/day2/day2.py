"""
Referencias
https://panda.ime.usp.br/pensepy/static/pensepy/10-Arquivos/files.html

"""
import os

dirname = os.path.dirname("/home/user/Área de Trabalho/adventCode2022/input/")
filename = os.path.join(dirname, 'day2.txt')

# A and X = Rock(1)
# B and Y = Paper(2)
# C and Z = Scissors(3)
# Score = Lose(0), Draw(3), Victory(6)
elfo = []
meu = []
lose = 0
draw = 3
victory = 6
X = 1
Y = 2
Z = 3


def readJokenpo(arquivo):
	
	arquivo = open(filename, 'r')
	item = 0	
	for linha in arquivo.readlines():
		elfo.append(linha[0])
		meu.append(linha[2])
	arquivo.close()
'''
	while item < len(elfo):
		if elfo[item] == "A":
			elfo[item] = 1
			#print("igual A")
			#print(item, "A")
		if elfo[item] == "B":
			elfo[item] = 2
			#print(item, "B")
		if elfo[item] == "C":
			elfo[item] = 3
			#print(item, "C")
		item += 1
	item = 0

	while item < len(meu):
		if meu[item] == "X":
			meu[item] = 1
			#print(item, "X")
		if meu[item] == "Y":
			meu[item] = 2
			#print(item, "Y")
		if meu[item] == "Z":
			meu[item] = 3
			#print(item, "Z")
		item += 1
'''

def jokenpoLetras(player1, player2):
	score = []

	for i in range(len(elfo)):
		#Se o elfo jogar Pedra(A)
		if player1[i] == "A" and player2[i] == "X":
			score.append(draw + X)
			#i += 1
			#print(i)
			#print(player1[i], player2[i])
			#print(draw, "+", player2[i], score)
			
		elif player1[i] == "A" and player2[i] == "Y":
			score.append(victory + Y)
			#i += 1
			#print(i)
			#print(player1[i], player2[i])
			#print(victory, "+", player2[i], score)
			
		elif player1[i] == "A" and player2[i] == "Z":
			score.append(lose + Z)
			#print(i)
			#print(player1[i], player2[i])
			#print(lose, "+", player2[i], score)
			

		#Se o elfo jogar Papel(B)
		elif player1[i] == "B" and player2[i] == "X":
			score.append(lose + X)
			#i += 1
			#print(i)
			#print(player1[i], player2[i])
			#print(lose, "+", player2[i], score)
			
		elif player1[i] == "B" and player2[i] == "Y":
			score.append(draw + Y)
			#i += 1
			#print(i)
			#print(player1[i], player2[i])
			#print(draw, "+", player2[i], score)
			
		elif player1[i] == "B" and player2[i] == "Z":
			score.append(victory + Z)
			#print(i)
			#print(player1[i], player2[i])
			#print(victory, "+", player2[i], score)
			

		#Se o elfo jogar Tesoura(C)
		elif player1[i] == "C" and player2[i] == "X":
			score.append(victory + X)
			#i += 1
			#print(i)
			#print(player1[i], player2[i])
			#print(victory, "+", player2[i], score)
			
		elif player1[i] == "C" and player2[i] == "Y":
			score.append(lose + Y)
			#i += 1
			#print(i)
			#print(player1[i], player2[i])
			#print(lose, "+", player2[i], score)
			
		elif player1[i] == "C" and player2[i] == "Z":
			score.append(draw + Z)
			#print(i)
			#print(player1[i], player2[i])
			#print(draw, "+", player2[i], score)

	print(sum(score))

def jokenpoFinal(player1, player2):
	score = []
	for i in range(len(elfo)):
		#Se o elfo jogar Pedra(A)
		if player1[i] == "A":
			if player2[i] == "X":
				score.append(Z + lose)
			elif player2[i] == "Y":
				score.append(X + draw)
			elif player2[i] == "Z":
				score.append(Y + victory)
		#Se o elfo jogar Papel(B)
		elif player1[i] == "B":
			if player2[i] == "X":
				score.append(X + lose)
			elif player2[i] == "Y":
				score.append(Y + draw)
			elif player2[i] == "Z":
				score.append(Z + victory)
		#Se o elfo jogar Tesoura(C)
		elif player1[i] == "C":
			if player2[i] == "X":
				score.append(Y + lose)
			elif player2[i] == "Y":
				score.append(Z + draw)
			elif player2[i] == "Z":
				score.append(X + victory)
	print(sum(score))
readJokenpo(filename)
jokenpoLetras(elfo, meu)
jokenpoFinal(elfo, meu)