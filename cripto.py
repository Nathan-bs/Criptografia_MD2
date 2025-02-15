import sys

class Ponto:
    def __init__(self, x, y):
        self.x = x
        self.y = y

def generate_points(a, b, p):
    pontos = []
    count = 1

    print("\nPontos geradores na curva elíptica:")

    for x in range(p):
        for y in range(p):
            if (y * y) % p == (x * x * x + a * x + b) % p:
                pontos.append(Ponto(x, y))
                print(f"G{count} = ({x}, {y})")
                count += 1

    return pontos, count

def main():
    if len(sys.argv) != 4:
        print(f"Uso: {sys.argv[0]} <a> <b> <p>")
        return

    a = int(sys.argv[1])
    b = int(sys.argv[2])
    p = int(sys.argv[3])

    pontos, count = generate_points(a, b, p)

    if count <= 3:
        print("Não há pontos suficientes para selecionar dois geradores.")
        return

    alfa = 3
    beta = 9

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

    indice_beta_alfa = beta_alfa % count
    indice_alfa_beta = alfa_beta % count

    alfaB = pontos[indice_beta_alfa - 1]
    betaA = pontos[indice_alfa_beta - 1]

    print(f"\nChave privada de Alice: {alfa}")
    print(f"Chave privada de Bob: {beta}")

    print(f"\nGerador escolhido para Alice (G{indice_alfa}): ({A.x}, {A.y})")
    print(f"Gerador escolhido para Bob (G{indice_beta}): ({B.x}, {B.y})")

    print(f"\n{indice_alfa * indice_beta}")

    print(f"\nNovo gerador escolhido para Alice (G{indice_alfa_beta}): ({alfaB.x}, {alfaB.y})")
    print(f"Novo gerador escolhido para Bob (G{indice_beta_alfa}): ({betaA.x}, {betaA.y})")

    print(f"\nA chave de Alice é: {alfaB.x}")
    print(f"A chave de Bob é: {betaA.x}")

if __name__ == "__main__":
    main()