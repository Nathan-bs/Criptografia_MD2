#include <stdio.h>
#include <stdlib.h>

typedef struct {
    int x;
    int y;
} Ponto;

void generate_points(int a, int b, int p, Ponto **pontos, int *count) {
    int x, y;
    *count = 1;  
    *pontos = (Ponto *)malloc((p * p + 1) * sizeof(Ponto));  

    if (*pontos == NULL) {
        printf("Erro ao alocar memória!\n");
        return;
    }

    printf("\nPontos geradores na curva elíptica:\n");

    for (x = 0; x < p; x++) {
        for (y = 0; y < p; y++) {
            if ((y * y) % p == (x * x * x + a * x + b) % p) {
                (*pontos)[*count].x = x;
                (*pontos)[*count].y = y;
                printf("G%d = (%d, %d)\n", *count, x, y);
                (*count)++;
            }
        }
    }
}

int main(int argc, char *argv[]) {
    if (argc != 4) {
        printf("Uso: %s <a> <b> <p>\n", argv[0]);
        return 1;
    }

    int a = atoi(argv[1]);
    int b = atoi(argv[2]);
    int p = atoi(argv[3]);
    Ponto *pontos = NULL;
    int count = 0;

    generate_points(a, b, p, &pontos, &count);

    if (count <= 3) { 
        printf("Não há pontos suficientes para selecionar dois geradores.\n");
        free(pontos);
        return 1;
    }

    long int alfa = 3;
    long int beta = 9;

    int indice_alfa = (alfa % p);
    int indice_beta = (beta % p);

    if (indice_alfa == 0) indice_alfa = 1;
    if (indice_beta == 0) indice_beta = 1;
    
    Ponto A = pontos[indice_alfa];
    Ponto B = pontos[indice_beta];

    long int alfa_beta = indice_beta * indice_alfa;
    long int beta_alfa = indice_alfa * indice_beta;

    int indice_beta_alfa = (beta_alfa % count);
    int indice_alfa_beta = (alfa_beta % count);
    
    Ponto alfaB = pontos[indice_beta_alfa];
    Ponto betaA = pontos[indice_alfa_beta];
    
    printf("\nChave privada de Alice: %ld\n", alfa);
    printf("Chave privada de Bob: %ld\n", beta);
    
    printf("\nGerador escolhido para Alice (G%d): (%d, %d)\n", indice_alfa, A.x, A.y);
    printf("Gerador escolhido para Bob (G%d): (%d, %d)\n", indice_beta, B.x, B.y);

    printf("\nNovo gerador escolhido para Alice (G%d): (%d, %d)\n", indice_alfa_beta, alfaB.x, alfaB.y);
    printf("Novo gerador escolhido para Bob (G%d): (%d, %d)\n", indice_beta_alfa, betaA.x, betaA.y);

    printf("\nA chave de Alice é: %d\n",alfaB.x);
    printf("A chave de Bob é: %d\n",betaA.x);

    free(pontos);
    return 0;
}