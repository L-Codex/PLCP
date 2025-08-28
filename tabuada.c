#include <stdio.h>
#define LIMITE 10

int main() {
    int numero;
    int cont = 1;

    printf("Digite um número para ver a tabuada: ");
    scanf("%d", &numero);

    printf("Tabuada do %d:\n", numero);

    while (cont <= LIMITE) {
        printf("%d x %d = %d\n", numero, cont, numero * cont);
        cont++;
    }

    return 0;
}
