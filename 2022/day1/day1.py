import os
dirname = os.path.dirname("/home/anderson/Documentos/Programação/2022/day1/")
filename = os.path.join(dirname, 'day1.txt')


def read_text(file):
    maior = []
    soma = 0

    data = open(file, 'r')

    for line in data.readlines():
        if line[0] != '\n':
            soma += int(line)
        else:
            maior.append(soma)
            soma = 0
            continue
    print(max(maior))
    # second answer
    maior.sort(reverse=True)
    print(sum(maior[0:3]))


read_text(filename)
