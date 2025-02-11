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

int calculate_public_key(int private_key, int generator_x) {
    return (private_key * generator_x);
}

int calculate_shared_key(int received_key, int private_key) {
    return (received_key * private_key);
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

    if (count <= 2) {
        printf("Não há pontos suficientes para selecionar G2.\n");
        free(pontos);
        return 1;
    }

    Ponto G = pontos[3];  
    printf("\nGerador escolhido (G3): (%d, %d)\n", G.x, G.y);

    int alpha = 3;
    int beta = 7;

    int A = calculate_public_key(alpha, G.x);
    int B = calculate_public_key(beta, G.x);

    int shared_key_alice = calculate_shared_key(B, alpha);
    int shared_key_bob = calculate_shared_key(A, beta);

    printf("\nChave privada de Alice: %d\n", alpha);
    printf("Chave privada de Bob: %d\n", beta);
    printf("Chave pública de Alice: %d\n", A);
    printf("Chave pública de Bob: %d\n", B);
    printf("Chave compartilhada calculada por Alice: %d\n", shared_key_alice);
    printf("Chave compartilhada calculada por Bob: %d\n", shared_key_bob);

    if (shared_key_alice == shared_key_bob) {
        printf("\n✅ Troca de chaves bem-sucedida! Chave compartilhada: %d\n", shared_key_alice);
    } else {
        printf("\n❌ Erro na troca de chaves!\n");
    }

    free(pontos);
    return 0;
}
