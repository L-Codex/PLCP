/**
 * velocidade.c - Cálculo de Velocidade Média
 * 
 * Descrição:
 *     Este programa calcula a velocidade média de um objeto
 *     a partir da distância percorrida e do tempo gasto.
 * 
 * Fórmula:
 *     Velocidade = Distância / Tempo
 * 
 * Autor: Projeto PLCP - 2º Semestre (Programação Estruturada em C)
 */

#include <stdio.h>

int main() {
    // Declaração das variáveis
    float distancia = 438;   // Distância percorrida em km
    float tempo = 6;         // Tempo gasto em horas
    
    // Cálculo da velocidade média
    float velocidade = distancia / tempo;
    
    // Exibe o resultado com 2 casas decimais
    printf("Velocidade média: %.2f km/h\n", velocidade);
    
    return 0;
}
