"""
class.py - Demonstração de Classes e Programação Orientada a Objetos

Descrição:
    Este script demonstra o uso de classes em Python e como
    salvar dados de objetos em arquivos JSON. Implementa uma
    classe Pessoa com atributos nome, idade e email.

Conceitos abordados:
    - Definição de classes
    - Método __init__ (construtor)
    - Atributos de instância
    - Serialização JSON

Autor: Projeto PLCP - 1º Semestre
"""

import json


class Pessoa:
    """
    Classe que representa uma pessoa.
    
    Atributos:
        nome (str): Nome da pessoa.
        idade (int): Idade da pessoa.
        email (str): Email da pessoa.
    """
    
    def __init__(self, nome, idade, email):
        """
        Inicializa uma nova instância de Pessoa.
        
        Parâmetros:
            nome (str): Nome da pessoa.
            idade (int): Idade da pessoa.
            email (str): Email da pessoa.
        """
        self.nome = nome
        self.idade = idade
        self.email = email


def coletar_dados():
    """
    Coleta os dados de uma pessoa via entrada do usuário.
    
    Retorno:
        Pessoa: Uma nova instância de Pessoa com os dados informados.
    """
    # Entrada: solicita os dados ao usuário
    nome = input("Digite o nome: ")
    idade = int(input("Digite a idade: "))
    email = input("Digite o email: ")
    
    # Cria e retorna uma nova instância de Pessoa
    return Pessoa(nome, idade, email)


def salvar_em_json(pessoa, nome_arquivo="pessoa.json"):
    """
    Salva os dados de uma pessoa em um arquivo JSON.
    
    Parâmetros:
        pessoa (Pessoa): A instância de Pessoa a ser salva.
        nome_arquivo (str): Nome do arquivo JSON (padrão: "pessoa.json").
    """
    # Abre o arquivo para escrita com codificação UTF-8
    with open(nome_arquivo, "w", encoding="utf-8") as f:
        # Converte o objeto para dicionário e salva como JSON
        json.dump(pessoa.__dict__, f, ensure_ascii=False, indent=4)
    
    print(f"Dados salvos em {nome_arquivo} com sucesso!")


# Bloco que permite a execução direta do script
if __name__ == "__main__":
    try:
        # Coleta os dados do usuário
        pessoa = coletar_dados()
        
        # Salva os dados em arquivo JSON
        salvar_em_json(pessoa)
        
    except ValueError:
        print("Erro: Por favor, digite uma idade válida.")
