import sys

class Ponto:
    def __init__(self, x, y):
        self.x = x
        self.y = y

def gerar_pontos(a, b, p):
    pontos = []
    ordem = 1

    print("\nPontos geradores na curva elíptica:")

    for x in range(p):
        for y in range(p):
            if (y * y) % p == (x * x * x + a * x + b) % p:
                pontos.append(Ponto(x, y))
                print(f"{ordem}G = ({x}, {y})")
                ordem += 1
    print(f"{ordem}G = O")        

    return pontos, ordem

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

    alfa = 113
    beta = 109

    indice_alfa = alfa % p
    indice_beta = beta % p

    if indice_alfa == 0:
        indice_alfa = 1
    if indice_beta == 0:
        indice_beta = 1

    A = pontos[indice_alfa - 1]
    B = pontos[indice_beta - 1]

    alfa_beta = indice_beta * indice_alfa
    beta_alfa = indice_alfa * indice_beta

    indice_beta_alfa = beta_alfa % ordem
    indice_alfa_beta = alfa_beta % ordem

    alfaB = pontos[indice_beta_alfa - 1]
    betaA = pontos[indice_alfa_beta - 1]

    print(f"\nChave privada de Alice: {alfa}")
    print(f"Chave privada de Bob: {beta}")

    print(f"\nGerador escolhido para Alice ({indice_alfa}G): ({A.x}, {A.y}) / aG = A")
    print(f"Gerador escolhido para Bob ({indice_beta}G): ({B.x}, {B.y}) / bG = BG")

    print(f"\nNovo gerador escolhido para Alice ({indice_alfa_beta}G): ({alfaB.x}, {alfaB.y}) / aB = abG = R")
    print(f"Novo gerador escolhido para Bob ({indice_beta_alfa}G): ({betaA.x}, {betaA.y}) / bA = baG = S")

    print(f"\nA chave de Alice é: {alfaB.x}")
    print(f"A chave de Bob é: {betaA.x}")

    print(f"\nRx = Sx")

if __name__ == "__main__":
    main()
