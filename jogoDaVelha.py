import os
import random 

jogarNovamente = 's'
jogadas = 0
quemJoga = 2
maxJogadas = 9
vit = 'n'
velha=[
    [" "," "," "],
    [" "," "," "],
    [" "," "," "]
]

def tela():
    global velha
    os.system("cls")
    print("    0   1   2")
    print("0:  " + velha[0][0] + " | " + velha[0][1] + " | " + velha[0][2])
    print("   -----------")
    print("1:  " + velha[1][0] + " | " + velha[1][1] + " | " + velha[1][2])
    print("   -----------")
    print("2:  " + velha[2][0] + " | " + velha[2][1] + " | " + velha[2][2])

def jogadorJoga():
    global jogadas 
    global quemJoga
    global vit
    global maxJogadas

    if quemJoga == 2 and jogadas<maxJogadas:
        linha = int(input("Digite a linha que quer jogar: "))
        coluna = int(input("Digite a coluna que quer jogar: "))
        try:
            while velha[linha][coluna]!=" ":
                linha = int(input("Digite a linha que quer jogar: "))
                coluna = int(input("Digite a coluna que quer jogar: "))
            velha[linha][coluna] = "X"
            quemJoga = 1
            jogadas+=1
        except:
            print("Linha ou coluna invalida")
          

def computador():
    global jogadas 
    global quemJoga
    global vit
    global maxJogadas
    if quemJoga == 1 and jogadas<maxJogadas:
        linha = random.randrange(0,3)
        coluna = random.randrange(0,3)
        while velha[linha][coluna]!=" ":
            linha = random.randrange(0,3)
            coluna = random.randrange(0,3)
        velha[linha][coluna] = "O"
        jogadas+=1
        quemJoga = 2
               

def ganhou():
    global velha
    vitoria = "n"
    simbolos = ["X","O"]
    #verificacao de linha
    for s in simbolos:
        vitoria = "n"
        l=c=0
        while l<3:
            soma = 0
            c = 0 
            while c<3:
                if (velha[l][c]==s):
                    soma+=1
                c+=1
            if(soma == 3):
                vitoria = s
                break
            l+=1
        if(vitoria!="n"):
            break
    #verificacao de coluna 
        l=c=0
        while c<3:
            soma = 0
            l = 0 
            while l<3:
                if (velha[l][c]==s):
                    soma+=1
                l+=1
            if(soma == 3):
                vitoria = s
                break
            c+=1
        if(vitoria!="n"):
            break
    #verificacao diagonal 1
        soma = 0
        idiag = 0 
        while idiag<3:
            if (velha[idiag][idiag]==s):
                soma+=1
            idiag+=1
        if(soma==3):
            vitoria=s
            break
    #verificacao diagonal 2
        soma = 0
        idiagl = 0 
        idiagc = 2 
        while idiagc>=3:
            if (velha[idiagl][idiagc]==s):
                soma+=1
            idiagl+=1
            idiagc-=1
        if(soma==3):
            vitoria=s
            break
    return vitoria

while True:
    tela()
    jogadorJoga()
    computador()
    ganhou()
    tela()
    vit = ganhou()
    if(vit!="n")or(jogadas>=maxJogadas):
        break

