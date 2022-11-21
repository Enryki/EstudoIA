from posixpath import lexists
from random import randint
import math
import random
from re import X

def bintodec(value): # recebe o binário e retorna o valor de f(i)
    x = value[:22]
    y = value[22:]
    x = (int(x, 2)*200/4194303)-100
    y = (int(y, 2)*200/4194303)-100
    # x = round(x, 5)
    # y = round(y, 5)
    lx.append(x)
    ly.append(y)
    p = 0.5 - ( ((math.sin(math.radians(math.sqrt(x**2 + y**2))))**2 - 0.5) / (1 + (0.001*(x**2 + y**2)) )**2 )
    #p = float("{:.5f}".format(p))
    return p

def selectpop(): # retorna a poplação para roleta
    rv = round(random.uniform(0, sp[99]), 5)
    for i in range(100):
        if(sp[i] >= rv):
            return i

def calcsp(): # coloca os valores em p e em sp
    for i in range(100): #calcula f(i) p/ cada indivíduo
        p.append(bintodec(populacao[i]))

        if i == 0:
            sp.append(p[i])
        else:
            sp.append(round(p[i] + sp[i-1], 5))

def bestchild(): # retorna o id do maior f(i)
    max_value = None
    max_idx = None
    for idx, num in enumerate(p):
        if (max_value is None or num > max_value):
            max_value = num
            max_id = idx
    return max_id

global ng # número total de gerações
global populacao # lista do cromossomas da população
global p # lista de (i) 
global sp # lista com o somatório de f(i)
global lx # lista dos valores de x
global ly # lista dos valores de y

ng = 4000 #número de gerações que serão executadas
populacao = []
p = [] # f(i)

for i in range(100): #geração de cromossomas aleatórios
    cromossoma = ''
    for j in range(44):
        cromossoma = cromossoma + str(randint(0, 1))
    populacao.append(cromossoma)

for i in range(ng):
    p = []
    sp = []
    lx = []
    ly = []
    calcsp()
    populacao_aux = []    
    for j in range(int(100/2)):

        r = random.uniform(0, 1)
        if r > 0.9:
            filho1 = populacao[j]
            filho2 = populacao[j+1]

        else:
            pai1 = selectpop()
            pai2 = selectpop()

            split = randint(1, 42)
        
            filho1 = populacao[pai1][:split]+populacao[pai2][split:]
            filho2 = populacao[pai2][:split]+populacao[pai1][split:]

        for j in range (44):
            r = random.uniform(0, 1)
            if r >= 0.001 and r <= 0.05:
                if filho1[j] == "0":
                    lista = list(filho1)
                    lista[j] = '1'
                    filho1 = "".join(lista)
                else:
                    lista = list(filho1)
                    lista[j] = '0'
                    filho1 = "".join(lista)
            
            r = random.uniform(0, 1)
            if r >= 0.001 and r <= 0.05:
                if filho2[j] == "0":
                    lista = list(filho2)
                    lista[j] = '1'
                    filho2 = "".join(lista)
                else:
                    lista = list(filho2)
                    lista[j] = '0'
                    filho2 = "".join(lista)

        populacao_aux.append(filho1)
        populacao_aux.append(filho2) 
    
    bc = bestchild()
    print("Geração: ", i, " | O melhor cromossoma é: ", populacao[bc], " | X = ", round(lx[bc], 3), " | Y = ", round(ly[bc], 3), " | P = ", p[bc])

    rc = randint(0, 99)
    populacao_aux[rc] = populacao[bc]

    populacao = populacao_aux