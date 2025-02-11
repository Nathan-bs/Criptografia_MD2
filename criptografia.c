#include <stdio.h>
#include <stdlib.h>

void gerar_pontos(int p, int a, int b) {
    int x, y, n = 0;
    printf("\n\n");

    for (x = 0; x < p; x++) {
        for (y = 0; y < p; y++) {
            if ((y * y) % p == (x * x * x + a * x + b) % p) {
                n++;
                printf("G%d = ( %d, %d )\n", n, x, y);
            }
        }
    }
    printf("\n\n");
}

int main(int argc, char *argv[]){

    if (argc < 4) {  // Verifica se foram passados pelo menos 3 argumentos além do nome do programa
        printf("Uso: %s <a> <b> <p>\n", argv[0]);
        return 1; // Retorna erro
    }

    int a = atoi(argv[1]),
        b = atoi(argv[2]),
        p = atoi(argv[3]);

    gerar_pontos(p, a, b);
    return 0;
}