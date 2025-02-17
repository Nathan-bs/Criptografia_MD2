from math import gcd
import sys
import random

class Ponto:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, outro):
        return self.x == outro.x and self.y == outro.y

    def __repr__(self):
        return f"Ponto({self.x}, {self.y})"
    
def inverso_modular(valor, mod):
    if gcd(valor, mod) != 1:
        return None
    return pow(valor, -1, mod)

def gerar_pontos(a, b, p):
    pontos = []
    ordem = 1

    print("\nPontos geradores na curva elíptica:")

    for x in range(p):
        for y in range(p):
            if (y * y) % p == (x * x * x + a * x + b) % p:
                pontos.append(Ponto(x, y))
                print(f"{ordem}g = ({x}, {y})")
                ordem += 1      

    return pontos, ordem

def soma_pontos(P, Q, a, p):
    if P is None:
        return Q
    if Q is None:
        return P
    if P.x == Q.x and (P.y != Q.y or P.y == 0):
        return None

    if P != Q:
        inverso = inverso_modular(Q.x - P.x, p)
        if inverso is None:
            return None
        s = ((Q.y - P.y) * inverso) % p
        xR = (s**2 - P.x - Q.x) % p
    else:
        inverso = inverso_modular(2 * P.y, p)
        if inverso is None:
            return None
        s = ((3 * P.x**2 + a) * inverso) % p
        xR = (s**2 - 2*P.x) % p
    
    yR = (s * (P.x - xR) - P.y) % p
    
    return Ponto(xR, yR)

def ordem_ponto(P, a, p):
    Q = P
    ordem = 1
    while Q is not None:
        Q = soma_pontos(Q, P, a, p)
        ordem += 1
    return ordem

def main():
    if len(sys.argv) != 4:
        print(f"Uso: {sys.argv[0]} <a> <b> <p>")
        return

    a = int(sys.argv[1])
    b = int(sys.argv[2])
    p = int(sys.argv[3])

    pontos, ordem = gerar_pontos(a, b, p)

    if ordem <= 3:
        print("Não há pontos suficientes para selecionar dois geradores.")
        return
    multiplos_G = []
    if len(pontos) > 50:
        pontos_aleatorios = random.sample(pontos, 50)
    else:
        pontos_aleatorios = pontos

        
    print("\nOrdens dos 50 pontos selecionados:")
    for i, ponto in enumerate(pontos_aleatorios):
        ordem = ordem_ponto(ponto, a, p)
        print(f"Ordem do ponto {i+1}G = ({ponto.x}, {ponto.y}): {ordem}")

    maior_ordem = 0
    melhor_ponto = None
    
    for ponto in pontos_aleatorios:
        ordem = ordem_ponto(ponto, a, p)
        if ordem > maior_ordem:
            maior_ordem = ordem
            melhor_ponto = ponto
    
    print(f"\nPonto de maior ordem encontrado: {melhor_ponto}, ordem = {maior_ordem}")
    
    print("\nMúltiplos do Gerador")
    G = melhor_ponto
    Q = G
    multiplos_G = []
    for i in range(1, maior_ordem + 2):
        if Q is None:
            print(f"{i}G = O")
            break
        print(f"{i}G = ({Q.x}, {Q.y})")
        multiplos_G.append(Q)
        Q = soma_pontos(Q, G, a, p)

    alfa = 3
    beta = 9

    indice_alfa = alfa % p
    indice_beta = beta % p

    if indice_alfa == 0:
        indice_alfa = p
    if indice_beta == 0:
        indice_beta = p

    A = multiplos_G[indice_alfa - 1]
    B = multiplos_G[indice_beta - 1]

    alfa_beta = indice_beta * indice_alfa
    beta_alfa = indice_alfa * indice_beta

    indice_beta_alfa = beta_alfa % (len(multiplos_G) + 1)
    indice_alfa_beta = alfa_beta % (len(multiplos_G) + 1)

    alfaB = multiplos_G[indice_beta_alfa - 1]
    betaA = multiplos_G[indice_alfa_beta - 1]

    print(f"\nChave privada de Alice: {alfa}")
    print(f"Chave privada de Bob: {beta}")

    print(f"\nGerador escolhido para Alice ({indice_alfa}G): ({A.x}, {A.y})")
    print(f"Gerador escolhido para Bob ({indice_beta}G): ({B.x}, {B.y})")

    print(f"\nNovo gerador escolhido para Alice ({indice_alfa_beta}G): ({alfaB.x}, {alfaB.y})")
    print(f"Novo gerador escolhido para Bob ({indice_beta_alfa}G): ({betaA.x}, {betaA.y})")

    print(f"\nA chave de Alice é: {alfaB.x}")
    print(f"A chave de Bob é: {betaA.x}")

if __name__ == "__main__":
    main()