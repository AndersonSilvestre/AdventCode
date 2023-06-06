import os
dirname = os.path.dirname("/home/anderson/Documentos/Programação/2022/day4/")
filename = os.path.join(dirname, 'day4.txt')
# Link usado como referência para entender o melhor método para separar o input.
# https://raw.githubusercontent.com/junefish/adventofcode/main/adventofcode2022/day4/day4problem1.py

passagem = []
with open(filename) as file:
    for secao in file.readlines():
        passagem.append(secao.strip().split(","))


def geraListaLimpeza(arquivo):
    limpeza = 0

    for item in passagem:
        # Cria 2 variaveis com os valores da lista
        elfo1, elfo2 = item[0], item[-1]
        # Separa cada valor com o seu começo e final. Criando assim 4 variaveis
        comeco1, final1 = elfo1.split('-')
        comeco2, final2 = elfo2.split('-')
        # Transforma todas as variaveis em Int p/ comparacoes
        comeco1 = int(comeco1)
        comeco2 = int(comeco2)
        final1 = int(final1)
        final2 = int(final2)

        if comeco1 <= comeco2 and final1 >= final2:
            limpeza += 1
        elif comeco2 <= comeco1 and final2 >= final1:
            limpeza += 1
        else:
            continue

    print(str(limpeza) + " Contem totalmente outro")


# Parte 2
def parte2(arquivo):
    sobrepoe = 0

    for item in passagem:
        # cria 2 variaveis com os valores da lista
        elfo1, elfo2 = item[0], item[-1]
        # Separa cada valor com o seu começo e final. Criando assim 4 variaveis
        comeco1, final1 = elfo1.split('-')
        comeco2, final2 = elfo2.split('-')
        # Transforma todas as variaveis em Int p/ comparacoes
        comeco1 = int(comeco1)
        comeco2 = int(comeco2)
        final1 = int(final1)
        final2 = int(final2)

        if comeco1 <= comeco2 <= final1:
            sobrepoe += 1
        elif comeco2 <= comeco1 <= final2:
            sobrepoe += 1
        else:
            continue
    print(str(sobrepoe) + " Se sobrepõe")


geraListaLimpeza(filename)
parte2(filename)
