"""
IMC.py - Calculadora de Índice de Massa Corporal

Descrição:
    Este script calcula o IMC (Índice de Massa Corporal) do usuário
    com base no peso e altura informados. O programa também classifica
    o resultado de acordo com os padrões da OMS (Organização Mundial da Saúde).

Fórmula:
    IMC = peso / altura²

Classificações:
    - Abaixo do peso: IMC < 18.5
    - Normal: 18.5 ≤ IMC < 24.9
    - Sobrepeso: 25 ≤ IMC < 29.9
    - Obesidade grau 1: 30 ≤ IMC < 34.9
    - Obesidade grau 2: 35 ≤ IMC < 39.9
    - Obesidade grau 3: IMC ≥ 40

Autor: Projeto PLCP
"""


def calcular_imc(peso, altura):
    """
    Calcula o IMC (Índice de Massa Corporal).
    
    Parâmetros:
        peso (float): Peso do usuário em quilogramas (kg).
        altura (float): Altura do usuário em metros (m).
    
    Retorno:
        float: O valor do IMC calculado.
    """
    # Aplica a fórmula: IMC = peso / altura²
    imc = peso / (altura ** 2)
    return imc


def classificar_imc(imc):
    """
    Classifica o IMC de acordo com os padrões da OMS.
    
    Parâmetros:
        imc (float): O valor do IMC a ser classificado.
    
    Retorno:
        str: A classificação correspondente ao IMC informado.
    """
    # Verifica cada faixa de IMC e retorna a classificação apropriada
    if imc < 18.5:
        return "Abaixo do peso"
    elif 18.5 <= imc < 24.9:
        return "Normal"
    elif 25 <= imc < 29.9:
        return "Sobrepeso"
    elif 30 <= imc < 34.9:
        return "Obesidade grau 1"
    elif 35 <= imc < 39.9:
        return "Obesidade grau 2"
    else:
        return "Obesidade grau 3"


def main():
    """
    Função principal do programa.
    
    Solicita peso e altura ao usuário, calcula o IMC e exibe a classificação.
    """
    try:
        # Entrada: solicita o peso e altura do usuário
        peso = float(input("Digite seu peso (em kg): "))
        altura = float(input("Digite sua altura (em metros): "))
        
        # Validação: verifica se os valores são positivos
        if peso <= 0 or altura <= 0:
            print("Erro: Peso e altura devem ser valores positivos.")
            return
        
        # Processamento: calcula o IMC
        imc = calcular_imc(peso, altura)
        
        # Processamento: obtém a classificação do IMC
        classificacao = classificar_imc(imc)
        
        # Saída: exibe o resultado formatado com 2 casas decimais
        print(f"O seu IMC é {imc:.2f}. Classificação: {classificacao}.")
        
    except ValueError:
        # Tratamento de erro para entrada inválida
        print("Erro: Por favor, digite valores numéricos válidos.")


# Bloco que permite a execução direta do script
if __name__ == '__main__':
    main()
