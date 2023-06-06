import os
import string

dirname = os.path.dirname("/home/anderson/Documentos/Programação/2022/day3/")
filename = os.path.join(dirname, 'day3.txt')
arquivo = open(filename, 'r')

primeiraP = []
segundaP = []
completa = []
minusculo = list(string.ascii_lowercase)
maiusculo = list(string.ascii_uppercase)
alfabetoLower = [ord(char) - 96 for char in list(string.ascii_lowercase)]
alfabetoUp = [ord(char) - 38 for char in list(string.ascii_uppercase)]
alfabeto = alfabetoLower + alfabetoUp


# Cria as listas / Create the lists
def gera_string(file):
	string2 = []

	for item in file.readlines():
		# Gera lista sem divisão de linhas
		completa.append(item.replace("\n", ""))
		# Divide a string em duas metades e salva nas listas
		primeiraP.append(item[:len(item)//2])
		string2.append(item[len(item)//2:])
		# for para tirar o \n da segunda metade da string
		for a in string2:
			segundaP.append(a.replace("\n", ""))
	arquivo.close()


# Primeira parte. Descobre qual letra se repete dentro da string e verifica o número que ela representa
# First part. Find out which letter repeats within the string and check the number it represents
def primeira_parte(file):
	i = 0
	conta_letras = 0
	while i < len(primeiraP):
		conta_minusculo = 0
		conta_maiusculo = 0
		for letra in primeiraP[i]:
			for char in segundaP[i]:
				if letra == char:
					if letra in list(string.ascii_lowercase):
						conta_minusculo = ord(letra) - 96
					elif letra in list(string.ascii_uppercase):
						conta_maiusculo = ord(letra) - 38
					break
				else:
					continue
		conta_letras += conta_maiusculo + conta_minusculo
		i += 1
	print(conta_letras, "Valor dos itens repetidos nas mochilas")


# Segunda parte. Verifica o valor dos grupos
# Second Part. Check the groups value
def parte2(file):
	i = 0
	grupo = 0
	tamanho = len(completa) / 3

	while i < tamanho:
		grupo_minusculo = 0
		grupo_maiusculo = 0
		for letra in completa[0]:
			if grupo_maiusculo > 0 or grupo_minusculo > 0:
				continue
			else:
				for letra2 in completa[1]:
					if letra == letra2:
						for letra3 in completa[2]:
							if letra == letra2 and letra2 == letra3:
								if letra in minusculo:
									grupo_minusculo = ord(letra) - 96
								elif letra in maiusculo:
									grupo_maiusculo = ord(letra) - 38
							else:
								continue
							break
						break
					else:
						continue
		i += 1
		grupo += grupo_maiusculo + grupo_minusculo
		del completa[0:3]
	print(grupo, "Valor dos grupos somados")


gera_string(arquivo)
primeira_parte(arquivo)
parte2(arquivo)
