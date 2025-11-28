"""
juros.py - Calculadora de Juros Compostos

Descrição:
    Este script calcula o montante final de um investimento
    utilizando a fórmula de juros compostos.

Fórmula:
    M = P × (1 + i)^t

    Onde:
    - M = Montante final
    - P = Capital inicial (principal)
    - i = Taxa de juros (em decimal)
    - t = Tempo de investimento

Autor: Projeto PLCP - 1º Semestre
"""


def juros_compostos(p, r, t):
    """
    Calcula o montante usando juros compostos.
    
    Parâmetros:
        p (float): Capital inicial (principal).
        r (float): Taxa de juros (em decimal, ex: 0.05 para 5%).
        t (int): Tempo de investimento em períodos.
    
    Retorno:
        float: O montante final após o período de investimento.
    """
    # Aplica a fórmula de juros compostos: M = P × (1 + i)^t
    return p * (1 + r) ** t


def main():
    """
    Função principal do programa.
    
    Solicita os dados do investimento e calcula o montante final.
    """
    try:
        # Entrada: solicita os dados do investimento
        c = float(input('Digite o capital inicial: '))
        i = float(input('Digite a taxa de juros (em %): ')) / 100  # Converte para decimal
        t = int(input('Digite o tempo de rendimento: '))
        
        # Validação: verifica se os valores são válidos
        if c < 0 or i < 0 or t < 0:
            print("Erro: Os valores devem ser positivos.")
            return
        
        # Processamento: calcula o montante
        montante = juros_compostos(c, i, t)
        
        # Saída: exibe o resultado formatado
        print(f'O montante é: {montante:,.2f}')
        
    except ValueError:
        # Tratamento de erro para entrada inválida
        print("Erro: Por favor, digite valores numéricos válidos.")


# Bloco que permite a execução direta do script
if __name__ == '__main__':
    main()