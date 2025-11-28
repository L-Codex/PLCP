"""
json.py - Manipulação de arquivos JSON (Agenda de Contatos)

Descrição:
    Este script demonstra como trabalhar com arquivos JSON em Python.
    Coleta dados de um contato (nome, celular e email) e os salva
    em um arquivo JSON estruturado.

Conceitos abordados:
    - Dicionários em Python
    - Listas
    - Serialização JSON
    - Escrita de arquivos

Autor: Projeto PLCP - 1º Semestre
"""

import json


def coletar_contato():
    """
    Coleta os dados de um contato via entrada do usuário.
    
    Retorno:
        dict: Dicionário com os dados do contato.
    """
    # Cria um dicionário para armazenar os dados
    contato = {}
    
    # Entrada: solicita os dados ao usuário
    contato["Nome"] = input("Nome: ")
    contato["Celular"] = input("Celular: ")
    contato["Email"] = input("E-mail: ")
    
    return contato


def salvar_contatos(lista_contatos, nome_arquivo="dados.json"):
    """
    Salva a lista de contatos em um arquivo JSON.
    
    Parâmetros:
        lista_contatos (list): Lista de dicionários com os contatos.
        nome_arquivo (str): Nome do arquivo JSON (padrão: "dados.json").
    """
    # Abre o arquivo para escrita
    with open(nome_arquivo, "w") as arquivo:
        # Salva a lista como JSON com indentação
        json.dump(lista_contatos, arquivo, indent=4)
    
    print(f"Contato salvo em {nome_arquivo} com sucesso!")


def main():
    """
    Função principal do programa.
    
    Coleta um contato e o salva em arquivo JSON.
    """
    # Coleta os dados do contato
    contato = coletar_contato()
    
    # Cria uma lista e adiciona o contato
    lista = []
    lista.append(contato)
    
    # Salva a lista em arquivo JSON
    salvar_contatos(lista)


# Bloco que permite a execução direta do script
if __name__ == '__main__':
    main()
