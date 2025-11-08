#include <limits.h>
#include <locale.h>
#include <stdbool.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define CLEAR "cls"

// Cores ANSI
#define RED    "\033[31m"
#define GREEN  "\033[32m"
#define YELLOW "\033[33m"
#define BLUE   "\033[34m"
#define CYAN   "\033[36m"
#define RESET  "\033[0m"

void inicializar(char tabuleiro[3][3]) {
  char c = '1';
  for (int i = 0; i < 3; ++i) {
    for (int j = 0; j < 3; ++j) { tabuleiro[i][j] = c++; }
  }
}

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

/* Faz a leitura segura da jogada usando fgets + sscanf para evitar problemas com scanf */
bool movimentar(char tabuleiro[3][3], char jogador) {
  char linha[100];
  int escolha;

  printf(
    "Jogador %s%c%s, escolha uma posição (1-9): ", jogador == 'X' ? RED : GREEN, jogador, RESET
  );

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

  int lin = (escolha - 1) / 3;
  int col = (escolha - 1) % 3;
  if (tabuleiro[lin][col] == 'X' || tabuleiro[lin][col] == 'O') {
    printf(YELLOW "Posição já ocupada! Tente outra.\n" RESET);
    return false;
  }

  tabuleiro[lin][col] = jogador;

  return true;
}

char verificarVitoria(char tabuleiro[3][3]) {
  // Verificar linhas e colunas
  for (int lin = 0; lin < 3; lin++) {
    if (tabuleiro[lin][0] == tabuleiro[lin][1] && tabuleiro[lin][1] == tabuleiro[lin][2]) {
      return tabuleiro[lin][0];
    }
  }
  for (int col = 0; col < 3; col++) {
    if (tabuleiro[0][col] == tabuleiro[1][col] && tabuleiro[1][col] == tabuleiro[2][col]) {
      return tabuleiro[0][col];
    }
  }

  // Verificar diagonais
  if (tabuleiro[0][0] == tabuleiro[1][1] && tabuleiro[1][1] == tabuleiro[2][2]) {
    return tabuleiro[0][0];
  }

  if (tabuleiro[0][2] == tabuleiro[1][1] && tabuleiro[1][1] == tabuleiro[2][0]) {
    return tabuleiro[0][2];
  }
  return '\0';
}

bool verificarEmpate(char tabuleiro[3][3]) {
  for (int lin = 0; lin < 3; lin++) {
    for (int col = 0; col < 3; col++) {
      if (tabuleiro[lin][col] != 'X' && tabuleiro[lin][col] != 'O') return false;
    }
  }
  return true;
}

int minimax(char tabuleiro[3][3], int profundidade, char jogador, int* lin, int* col, int alpha, int beta) {
  int melhorValor;
  int melhorLin = -1;
  int melhorCol = -1;

  if (jogador == 'O') {
    melhorValor = INT_MIN;
  } else {
    melhorValor = INT_MAX;
  }

  if (profundidade == 0 || verificarVitoria(tabuleiro) != '\0' || verificarEmpate(tabuleiro)) {
    char ganhador = verificarVitoria(tabuleiro);
    if (ganhador == 'O') return 1;
    if (ganhador == 'X') return -1;
    return 0;
  }

  for (int l = 0; l < 3; l++) {
    for (int c = 0; c < 3; c++) {
      if (tabuleiro[l][c] != 'X' && tabuleiro[l][c] != 'O') {
        tabuleiro[l][c] = jogador;

        int valor = minimax(tabuleiro, profundidade - 1, jogador == 'X' ? 'O' : 'X', NULL, NULL, alpha, beta);

        tabuleiro[l][c] = '1' + l * 3 + c;

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
        
        // Alpha-beta pruning
        if (beta <= alpha) {
          goto pruning_done;
        }
      }
    }
  }

pruning_done:
  if (lin && col) {
    *lin = melhorLin;
    *col = melhorCol;
  }
  return melhorValor;
}


int main() {
  system("chcp 65001");
  setlocale(LC_ALL, "pt_BR.UTF-8");

  char tabuleiro[3][3];
  char continuar = 's';
  char linha[100];
  while (true) {
    system(CLEAR);
    printf(CYAN "Bem-vindo ao Jogo da Velha!" RESET);
    printf("\nDeseja jogar com [A]migo ou contra o [C]omputador? ");
    if (!fgets(linha, sizeof(linha), stdin)) { continue; };
    int k = 0;
    while (linha[k] != '\0'
           && (linha[k] == ' ' || linha[k] == '\t' || linha[k] == '\n' || linha[k] == '\r')) {
      k++;
    }
    break;
  }

  int modoComputador = (linha[0] == 'C' || linha[0] == 'c') ? 1 : 0;

  /* pega primeiro caractere não branco */
  while (continuar == 's' || continuar == 'S') {
    inicializar(tabuleiro);
    char atual    = 'X';
    char ganhador = '\0';

    while (true) {
      exibir(tabuleiro);
      if (atual == 'X' || !modoComputador) {
        if (!movimentar(tabuleiro, atual)) {
          printf("\nPressione ENTER para continuar...");
          /* consumir até o final da linha (caso haja restos) */
          fgets(linha, sizeof(linha), stdin);
          continue;
        }
      } else if (modoComputador) {
        printf("Jogador %s%c%s está pensando...\n", GREEN, atual, RESET);
        int lin = -1, col = -1;
        minimax(tabuleiro, 10, 'O', &lin, &col, INT_MIN, INT_MAX);
        tabuleiro[lin][col] = atual;
      }

      ganhador = verificarVitoria(tabuleiro);
      if (ganhador != '\0') {
        exibir(tabuleiro);
        printf(
          "\n🎉 Jogador %s%c%s venceu! Parabéns!\n", ganhador == 'X' ? RED : GREEN, ganhador, RESET
        );
        break;
      }

      if (verificarEmpate(tabuleiro)) {
        exibir(tabuleiro);
        printf(YELLOW "\n😐 Empate! Ninguém venceu.\n" RESET);
        break;
      }

      atual = (atual == 'X') ? 'O' : 'X';
    }

    printf("\nDeseja jogar novamente? (s/n): ");
    if (!fgets(linha, sizeof(linha), stdin)) break;

    /* pega primeiro caractere não branco */
    int k = 0;
    while (linha[k] != '\0'
           && (linha[k] == ' ' || linha[k] == '\t' || linha[k] == '\n' || linha[k] == '\r'))
      k++;
    if (linha[k] == '\0') break;
    continuar = linha[k];
  }

  system(CLEAR);
  printf(CYAN "\nObrigado por jogar! Até a próxima 👋\n\n" RESET);

  return 0;
}
