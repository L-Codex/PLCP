/**
 * tabuada.c - Exibe a Tabuada de um Número
 * 
 * Descrição:
 *     Este programa solicita um número ao usuário e exibe
 *     sua tabuada de multiplicação de 1 a 10.
 *     Demonstra o uso de laço while em C.
 * 
 * Autor: Projeto PLCP - 2º Semestre (Programação Estruturada em C)
 */

#include <stdio.h>

// Define o limite da tabuada (1 a 10)
#define LIMITE 10

int main() {
    // Declaração das variáveis
    int numero;      // Número para gerar a tabuada
    int cont = 1;    // Contador do laço
    
    // Entrada: solicita o número ao usuário
    printf("Digite um número para ver a tabuada: ");
    scanf("%d", &numero);
    
    // Exibe o cabeçalho
    printf("Tabuada do %d:\n", numero);
    
    // Laço while para gerar a tabuada de 1 a LIMITE
    while (cont <= LIMITE) {
        // Exibe cada linha da tabuada
        printf("%d x %d = %d\n", numero, cont, numero * cont);
        cont++;  // Incrementa o contador
    }
    
    return 0;
}
