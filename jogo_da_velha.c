/**
 * jogo_da_velha.c - Jogo da Velha com IA
 * 
 * Descrição:
 *     Implementação completa do Jogo da Velha (Tic-Tac-Toe) em C.
 *     O jogador pode escolher jogar contra outro jogador ou contra
 *     a IA do computador que utiliza o algoritmo Minimax com poda
 *     alpha-beta para tomar decisões ótimas.
 * 
 * Recursos:
 *     - Interface colorida usando códigos ANSI
 *     - IA inteligente com algoritmo Minimax otimizado
 *     - Modo para 2 jogadores ou contra o computador
 * 
 * Complexidade da IA:
 *     O(b^(d/2)) com poda alpha-beta (melhor caso)
 * 
 * Autor: Projeto PLCP - 2º Semestre (Programação Estruturada em C)
 */

#include <limits.h>
#include <locale.h>
#include <stdbool.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

// Comando para limpar a tela (Windows)
#define CLEAR "cls"

// Definição de cores ANSI para terminal
#define RED    "\033[31m"    // Vermelho para jogador X
#define GREEN  "\033[32m"    // Verde para jogador O
#define YELLOW "\033[33m"    // Amarelo para avisos
#define BLUE   "\033[34m"    // Azul
#define CYAN   "\033[36m"    // Ciano para títulos
#define RESET  "\033[0m"     // Reset para cor padrão

/**
 * Inicializa o tabuleiro com números de 1 a 9.
 * 
 * Parâmetros:
 *     tabuleiro: matriz 3x3 representando o tabuleiro
 */
void inicializar(char tabuleiro[3][3]) {
  char c = '1';
  for (int i = 0; i < 3; ++i) {
    for (int j = 0; j < 3; ++j) { tabuleiro[i][j] = c++; }
  }
}

/**
 * Exibe o tabuleiro na tela com cores e formatação.
 * 
 * Parâmetros:
 *     tabuleiro: matriz 3x3 representando o tabuleiro
 */
void exibir(char tabuleiro[3][3]) {
  system(CLEAR);
  printf(CYAN "\n╔══════════════════════════════╗\n" RESET);
  printf(CYAN "║        JOGO DA VELHA         ║\n" RESET);
  printf(CYAN "╚══════════════════════════════╝\n\n" RESET);

  printf("       1   2   3\n");
  printf("     ┌───┬───┬───┐\n");
  for (int lin = 0; lin < 3; ++lin) {
    printf("   %d │", lin + 1);
    for (int col = 0; col < 3; ++col) {
      char c = tabuleiro[lin][col];
      // Aplica cor conforme o jogador
      if (c == 'X')
        printf(RED " %c " RESET, c);
      else if (c == 'O')
        printf(GREEN " %c " RESET, c);
      else
        printf(" %c ", c);
      if (col < 2) printf("│");
    }
    printf("│\n");
    if (lin < 2) printf("     ├───┼───┼───┤\n");
  }
  printf("     └───┴───┴───┘\n\n");
}

/**
 * Processa a jogada do usuário.
 * Faz leitura segura usando fgets + sscanf para evitar problemas com scanf.
 * 
 * Parâmetros:
 *     tabuleiro: matriz 3x3 representando o tabuleiro
 *     jogador: caractere do jogador atual ('X' ou 'O')
 * 
 * Retorno:
 *     true se a jogada foi válida, false caso contrário
 */
bool movimentar(char tabuleiro[3][3], char jogador) {
  char linha[100];
  int escolha;

  printf(
    "Jogador %s%c%s, escolha uma posição (1-9): ", jogador == 'X' ? RED : GREEN, jogador, RESET
  );

  // Leitura segura da entrada
  if (!fgets(linha, sizeof(linha), stdin)) {
    printf(YELLOW "Erro na leitura. Tente novamente.\n" RESET);
    return false;
  }
  if (sscanf(linha, "%d", &escolha) != 1) {
    printf(YELLOW "Entrada inválida! Digite um número de 1 a 9.\n" RESET);
    return false;
  }
  if (escolha < 1 || escolha > 9) {
    printf(YELLOW "Posição inválida! Escolha entre 1 e 9.\n" RESET);
    return false;
  }

  // Converte a escolha (1-9) para coordenadas (linha, coluna)
  int lin = (escolha - 1) / 3;
  int col = (escolha - 1) % 3;
  
  // Verifica se a posição já está ocupada
  if (tabuleiro[lin][col] == 'X' || tabuleiro[lin][col] == 'O') {
    printf(YELLOW "Posição já ocupada! Tente outra.\n" RESET);
    return false;
  }

  // Realiza a jogada
  tabuleiro[lin][col] = jogador;

  return true;
}

/**
 * Verifica se há um vencedor no jogo.
 * 
 * Parâmetros:
 *     tabuleiro: matriz 3x3 representando o tabuleiro
 * 
 * Retorno:
 *     'X' ou 'O' se houver vencedor, '\0' caso contrário
 */
char verificarVitoria(char tabuleiro[3][3]) {
  // Verificar linhas
  for (int lin = 0; lin < 3; lin++) {
    if (tabuleiro[lin][0] == tabuleiro[lin][1] && tabuleiro[lin][1] == tabuleiro[lin][2]) {
      return tabuleiro[lin][0];
    }
  }
  
  // Verificar colunas
  for (int col = 0; col < 3; col++) {
    if (tabuleiro[0][col] == tabuleiro[1][col] && tabuleiro[1][col] == tabuleiro[2][col]) {
      return tabuleiro[0][col];
    }
  }

  // Verificar diagonal principal
  if (tabuleiro[0][0] == tabuleiro[1][1] && tabuleiro[1][1] == tabuleiro[2][2]) {
    return tabuleiro[0][0];
  }

  // Verificar diagonal secundária
  if (tabuleiro[0][2] == tabuleiro[1][1] && tabuleiro[1][1] == tabuleiro[2][0]) {
    return tabuleiro[0][2];
  }
  
  return '\0';  // Nenhum vencedor
}

/**
 * Verifica se o jogo terminou em empate.
 * 
 * Parâmetros:
 *     tabuleiro: matriz 3x3 representando o tabuleiro
 * 
 * Retorno:
 *     true se todas as posições estão ocupadas, false caso contrário
 */
bool verificarEmpate(char tabuleiro[3][3]) {
  for (int lin = 0; lin < 3; lin++) {
    for (int col = 0; col < 3; col++) {
      if (tabuleiro[lin][col] != 'X' && tabuleiro[lin][col] != 'O') return false;
    }
  }
  return true;
}

/**
 * Algoritmo Minimax com poda Alpha-Beta para a IA.
 * 
 * Este algoritmo explora todas as jogadas possíveis e escolhe
 * a melhor jogada para o jogador atual (maximizar para 'O',
 * minimizar para 'X').
 * 
 * Parâmetros:
 *     tabuleiro: matriz 3x3 representando o tabuleiro
 *     profundidade: profundidade máxima de busca
 *     jogador: jogador atual ('X' ou 'O')
 *     lin, col: ponteiros para retornar a melhor jogada
 *     alpha: melhor valor para o maximizador
 *     beta: melhor valor para o minimizador
 * 
 * Retorno:
 *     Valor da melhor jogada (1 para vitória de O, -1 para X, 0 empate)
 */
int minimax(char tabuleiro[3][3], int profundidade, char jogador, int* lin, int* col, int alpha, int beta) {
  int melhorValor;
  int melhorLin = -1;
  int melhorCol = -1;

  // Inicializa o melhor valor conforme o jogador
  if (jogador == 'O') {
    melhorValor = INT_MIN;  // Maximizar para O
  } else {
    melhorValor = INT_MAX;  // Minimizar para X
  }

  // Condição de parada: profundidade 0, vitória ou empate
  if (profundidade == 0 || verificarVitoria(tabuleiro) != '\0' || verificarEmpate(tabuleiro)) {
    char ganhador = verificarVitoria(tabuleiro);
    if (ganhador == 'O') return 1;   // IA venceu
    if (ganhador == 'X') return -1;  // Jogador venceu
    return 0;  // Empate
  }

  // Percorre todas as posições livres
  for (int l = 0; l < 3; l++) {
    for (int c = 0; c < 3; c++) {
      if (tabuleiro[l][c] != 'X' && tabuleiro[l][c] != 'O') {
        // Faz a jogada temporária
        tabuleiro[l][c] = jogador;

        // Chamada recursiva para o próximo nível
        int valor = minimax(tabuleiro, profundidade - 1, jogador == 'X' ? 'O' : 'X', NULL, NULL, alpha, beta);

        // Desfaz a jogada
        tabuleiro[l][c] = '1' + l * 3 + c;

        // Atualiza o melhor valor conforme o jogador
        if (jogador == 'O') {
          if (valor > melhorValor) {
            melhorValor = valor;
            melhorLin   = l;
            melhorCol   = c;
          }
          alpha = (valor > alpha) ? valor : alpha;
        } else {
          if (valor < melhorValor) {
            melhorValor = valor;
            melhorLin   = l;
            melhorCol   = c;
          }
          beta = (valor < beta) ? valor : beta;
        }
        
        // Poda Alpha-Beta: corta ramos desnecessários
        if (beta <= alpha) {
          goto pruning_done;
        }
      }
    }
  }

pruning_done:
  // Retorna a melhor jogada encontrada
  if (lin && col) {
    *lin = melhorLin;
    *col = melhorCol;
  }
  return melhorValor;
}


/**
 * Função principal do jogo.
 */
int main() {
  // Configura o terminal para suportar UTF-8
  system("chcp 65001");
  setlocale(LC_ALL, "pt_BR.UTF-8");

  char tabuleiro[3][3];
  char continuar = 's';
  char linha[100];
  
  // Menu inicial: escolha do modo de jogo
  while (true) {
    system(CLEAR);
    printf(CYAN "Bem-vindo ao Jogo da Velha!" RESET);
    printf("\nDeseja jogar com [A]migo ou contra o [C]omputador? ");
    if (!fgets(linha, sizeof(linha), stdin)) { continue; };
    int k = 0;
    // Ignora espaços em branco no início
    while (linha[k] != '\0'
           && (linha[k] == ' ' || linha[k] == '\t' || linha[k] == '\n' || linha[k] == '\r')) {
      k++;
    }
    break;
  }

  // Define o modo de jogo (0 = dois jogadores, 1 = contra computador)
  int modoComputador = (linha[0] == 'C' || linha[0] == 'c') ? 1 : 0;

  // Loop principal do jogo
  while (continuar == 's' || continuar == 'S') {
    inicializar(tabuleiro);
    char atual    = 'X';      // Jogador atual
    char ganhador = '\0';

    // Loop de uma partida
    while (true) {
      exibir(tabuleiro);
      
      // Jogada do jogador humano ou IA
      if (atual == 'X' || !modoComputador) {
        if (!movimentar(tabuleiro, atual)) {
          printf("\nPressione ENTER para continuar...");
          fgets(linha, sizeof(linha), stdin);
          continue;
        }
      } else if (modoComputador) {
        // Jogada da IA
        printf("Jogador %s%c%s está pensando...\n", GREEN, atual, RESET);
        int lin = -1, col = -1;
        minimax(tabuleiro, 10, 'O', &lin, &col, INT_MIN, INT_MAX);
        tabuleiro[lin][col] = atual;
      }

      // Verifica vitória
      ganhador = verificarVitoria(tabuleiro);
      if (ganhador != '\0') {
        exibir(tabuleiro);
        printf(
          "\n🎉 Jogador %s%c%s venceu! Parabéns!\n", ganhador == 'X' ? RED : GREEN, ganhador, RESET
        );
        break;
      }

      // Verifica empate
      if (verificarEmpate(tabuleiro)) {
        exibir(tabuleiro);
        printf(YELLOW "\n😐 Empate! Ninguém venceu.\n" RESET);
        break;
      }

      // Alterna o jogador
      atual = (atual == 'X') ? 'O' : 'X';
    }

    // Pergunta se deseja jogar novamente
    printf("\nDeseja jogar novamente? (s/n): ");
    if (!fgets(linha, sizeof(linha), stdin)) break;

    // Obtém a resposta do usuário
    int k = 0;
    while (linha[k] != '\0'
           && (linha[k] == ' ' || linha[k] == '\t' || linha[k] == '\n' || linha[k] == '\r'))
      k++;
    if (linha[k] == '\0') break;
    continuar = linha[k];
  }

  // Mensagem de despedida
  system(CLEAR);
  printf(CYAN "\nObrigado por jogar! Até a próxima 👋\n\n" RESET);

  return 0;
}
