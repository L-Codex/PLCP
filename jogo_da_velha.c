#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>
#include <string.h>
#include <locale.h>

#ifdef _WIN32
#define CLEAR "cls"
#else
#define CLEAR "clear"
#endif

// Cores ANSI (se o seu terminal não suportar, aparecerão códigos)
#define RED     "\x1b[31m"
#define GREEN   "\x1b[32m"
#define YELLOW  "\>x1b[33m"
#define BLUE    "\x1b[34m"
#define CYAN    "\x1b[36m"
#define RESET   "\x1b[0m"

char board[3][3];

void initBoard() {
    char c = '1';
    for (int i = 0; i < 3; ++i)
        for (int j = 0; j < 3; ++j)
            board[i][j] = c++;
}

void printBoard() {
    system(CLEAR);
    printf(CYAN "\n╔══════════════════════════════╗\n" RESET);
    printf(CYAN "║        JOGO DA VELHA         ║\n" RESET);
    printf(CYAN "╚══════════════════════════════╝\n\n" RESET);

    printf("       1   2   3\n");
    printf("     ┌───┬───┬───┐\n");
    for (int i = 0; i < 3; ++i) {
        printf("   %d │", i + 1);
        for (int j = 0; j < 3; ++j) {
            char c = board[i][j];
            if (c == 'X') printf(RED " %c " RESET, c);
            else if (c == 'O') printf(GREEN " %c " RESET, c);
            else printf(" %c ", c);
            if (j < 2) printf("│");
        }
        printf("│\n");
        if (i < 2) printf("     ├───┼───┼───┤\n");
    }
    printf("     └───┴───┴───┘\n\n");
}

/* Faz a leitura segura da jogada usando fgets + sscanf para evitar problemas com scanf */
bool makeMove(char player) {
    char line[100];
    int choice;

    printf("Jogador %s%c%s, escolha uma posição (1-9): ", 
        (player == 'X' ? RED : GREEN), player, RESET);

    if (!fgets(line, sizeof(line), stdin)) {
        printf(YELLOW "Erro na leitura. Tente novamente.\n" RESET);
        return false;
    }
    if (sscanf(line, "%d", &choice) != 1) {
        printf(YELLOW "Entrada inválida! Digite um número de 1 a 9.\n" RESET);
        return false;
    }
    if (choice < 1 || choice > 9) {
        printf(YELLOW "Posição inválida! Escolha entre 1 e 9.\n" RESET);
        return false;
    }

    int row = (choice - 1) / 3;
    int col = (choice - 1) % 3;
    if (board[row][col] == 'X' || board[row][col] == 'O') {
        printf(YELLOW "Posição já ocupada! Tente outra.\n" RESET);
        return false;
    }

    board[row][col] = player;
    return true;
}

char checkWin() {
    for (int i = 0; i < 3; ++i)
        if (board[i][0] == board[i][1] && board[i][1] == board[i][2])
            return board[i][0];
    for (int j = 0; j < 3; ++j)
        if (board[0][j] == board[1][j] && board[1][j] == board[2][j])
            return board[0][j];
    if (board[0][0] == board[1][1] && board[1][1] == board[2][2])
        return board[0][0];
    if (board[0][2] == board[1][1] && board[1][1] == board[2][0])
        return board[0][2];
    return '\0';
}

bool isTie() {
    for (int i = 0; i < 3; ++i)
        for (int j = 0; j < 3; ++j)
            if (board[i][j] != 'X' && board[i][j] != 'O')
                return false;
    return true;
}

int main() {
    system("chcp 65001");
    setlocale(LC_ALL, "pt_BR.UTF-8");

    char again = 's';
    char line[100];

    while (again == 's' || again == 'S') {
        initBoard();
        char current = 'X';
        char winner = '\0';

        while (true) {
            printBoard();
            if (!makeMove(current)) {
                printf("\nPressione ENTER para continuar...");
                /* consumir até o final da linha (caso haja restos) */
                fgets(line, sizeof(line), stdin);
                continue;
            }
            winner = checkWin();
            if (winner != '\0') {
                printBoard();
                printf(BLUE "\n🎉 Jogador %s%c%s venceu! Parabéns!\n" RESET,
                    (winner == 'X' ? RED : GREEN), winner, RESET);
                break;
            }
            if (isTie()) {
                printBoard();
                printf(YELLOW "\n😐 Empate! Ninguém venceu.\n" RESET);
                break;
            }
            current = (current == 'X') ? 'O' : 'X';
        }

        /* Pergunta se quer jogar novamente de forma segura */
        printf("\nDeseja jogar novamente? (s/n): ");
        if (!fgets(line, sizeof(line), stdin)) break;
        /* pega primeiro caractere não branco */
        int k = 0;
        while (line[k] != '\0' && (line[k] == ' ' || line[k] == '\t' || line[k] == '\n' || line[k] == '\r')) k++;
        if (line[k] == '\0') break;
        again = line[k];
    }

    system(CLEAR);
    printf(CYAN "\nObrigado por jogar! Até a próxima 👋\n\n" RESET);
    return 0;
}

