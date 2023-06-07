import copy
import os

dirname = os.path.dirname("/home/anderson/Documentos/Programação/2022/day5/")
filename = os.path.join(dirname, 'day5.txt')

lista = [['W', 'R', 'F'],
         ['T', 'H', 'M', 'C', 'D', 'V', 'W', 'P'],
         ['P', 'M', 'Z', 'N', 'L'],
         ['J', 'C', 'H', 'R'],
         ['C', 'P', 'G', 'H', 'Q', 'T', 'B'],
         ['G', 'C', 'W', 'L', 'F', 'Z'],
         ['W', 'V', 'L', 'Q', 'Z', 'J', 'G', 'C'],
         ['P', 'N', 'R', 'F', 'W', 'T', 'V', 'C'],
         ['J', 'W', 'H', 'G', 'R', 'S', 'V']]

with open(filename) as file:
    comandos = []
    for linhas in file.readlines():
        comandos.append(linhas.replace("move", "")
                        .replace("from", ",").replace("to", ",").replace("\n", "").replace(" ", "").split(","))


def movimenta(list):
    x = 0
    final = []
    list1 = copy.deepcopy(list)

    for comando in comandos:
        move = int(comando[0])
        de = int(comando[1]) - 1
        para = int(comando[2]) - 1
        while move > 0:
            movimenta = list1[de].pop()
            list1[para].append(movimenta)
            move -= 1
    # for para gerar a lista final
    for itens in list1:
        final.append(list1[x][-1])
        x = x + 1

    print("Aqui está a lista" + str(final).replace(",", "").replace("'", "").replace(" ", ""))


def cratemover9001(list):
    x = 0
    final = []
    list2 = copy.deepcopy(list)

    for comando in comandos:
        move = int(comando[0])
        movimenta = int(comando[0]) * -1
        de = int(comando[1]) - 1
        para = int(comando[2]) - 1
        while move > 0:
            movimentacao = list2[de].pop(movimenta)
            list2[para].append(movimentacao)
            move -= 1
            movimenta += 1
    # for para gerar a lista final
    for itens in list2:
        final.append(list2[x][-1])
        x = x + 1

    print("Aqui está a lista" + str(final).replace(",", "").replace("'", "").replace(" ", ""))


movimenta(lista)
cratemover9001(lista)
