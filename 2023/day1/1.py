import os

dirname = os.path.dirname("/home/anderson/Documentos/Programação/2023/day1/")
filename = os.path.join(dirname, "tst.txt")

linhas = []

with open(filename) as file:
    for i in file.readlines():
        linhas.append(i.strip())
#print(linhas)

# Primeira Parte
def soma(lista):
    junto, numero = [], []
    total = 0
    for item in lista:
        for w in item:
            if w.isdigit():
                numero.append(w)     
        bla = numero[0] + numero[-1]
        junto.append(int(bla))
        numero = []
    for i in junto:
        total += i
    print(total)

# Segunda Parte
def letras(lista):
    listinha = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'zero']
    dic = {'one': 1, 'two': 2, 'three':3, 'four':4, 'five':5, 'six':6, 'seven':7, 'eight':8, 'nine':9, 'zero':0}
    #for i in lista:
        #print(i in dic)
        #if i in dic:
            #print('no dic')
    z = 0
    for a in lista:
        if 'one' in a:
            nova = lista[z].replace('one','1')
            lista.pop(z)
            lista.insert(z,nova)
            print(nova)
        if 'two'in a:
            nova = lista[z].replace('two','2')
            lista.pop(z)
            print(lista)
            lista.insert(z,nova)
            print(lista)
            print(nova)
        if 'three'in a:
            nova = lista[z].replace('three','3')
            lista.pop(z)
            lista.insert(z,nova)
            print(nova)
        if 'four'in a:
            nova = lista[z].replace('four','4')
            lista.pop(z)
            lista.insert(z,nova)
            print(nova)
        if 'five'in a:
            nova = lista[z].replace('five','5')
            lista.pop(z)
            lista.insert(z,nova)
            print(nova)
        if 'six'in a:
            nova = lista[z].replace('six','6')
            lista.pop(z)
            lista.insert(z,nova)
            print(nova)
        if 'seven'in a:
            nova = lista[z].replace('seven','7')
            lista.pop(z)
            lista.insert(z,nova)
            print(nova)
        if 'eight'in a:
            nova = lista[z].replace('eight','8')
            lista.pop(z)
            lista.insert(z,nova)
            print(nova)
        if 'nine'in a:
            nova = lista[z].replace('nine','9')
            lista.pop(z)
            lista.insert(z,nova)
            print(lista)
            print(nova)
        if 'zero'in a:
            nova = lista[z].replace('zero','0')
            lista.pop(z)
            lista.insert(z,nova)
            print(nova)
        z += 1
        #break
    print(linhas)




#soma(linhas)
letras(linhas)