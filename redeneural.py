import random

tabeladetreino = []

# n1 n2 saída -> saída 1 = cientista | saída 0 = compositor
tabeladetreino.append(["BACH", 0, 0, 0])
tabeladetreino.append(["BEETHOVEN", 0, 1, 0])
tabeladetreino.append(["EINSTEIN", 1, 0, 1])
tabeladetreino.append(["KEPLER", 1, 1, 1])

global w1
global w2
global wb

w1 = 0
w2 = 0
wb = 0
cont = 0

#(Bias*Wb)+(N1*W1)+(N2*W2)
def somatorio(line):
    return (1*wb)+(tabeladetreino[line][1]*w1)+(tabeladetreino[line][2]*w2)

while(cont!=4):
    cont = 0
    
    ordem = random.sample([0,1,2,3], k=4)

    for i in range(4):
        s = somatorio(ordem[i])

        if s == tabeladetreino[ordem[i]][3] or ((s > 0) and (tabeladetreino[ordem[i]][3] == 1)) :
            cont = cont + 1
        else:
            print("Erro encontrado!")
            wb = wb + ((tabeladetreino[ordem[i]][3] - s) * 1 * 1)
            w1 = w1 + ((tabeladetreino[ordem[i]][3] - s) * 1 * tabeladetreino[ordem[i]][1])
            w2 = w2 + ((tabeladetreino[ordem[i]][3] - s) * 1 * tabeladetreino[ordem[i]][2])
            print(wb, w1, w2)
        
    
print(wb, w1, w2)