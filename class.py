import json

class Pessoa:
    def __init__(self, nome, idade, email):
        self.nome = nome
        self.idade = idade
        self.email = email

def coletar_dados():
    nome = input("Digite o nome: ")
    idade = int(input("Digite a idade: "))
    email = input("Digite o email: ")
    return Pessoa(nome, idade, email)

def salvar_em_json(pessoa, nome_arquivo="pessoa.json"):
    with open(nome_arquivo, "w", encoding="utf-8") as f:
        json.dump(pessoa.__dict__, f, ensure_ascii=False, indent=4)
    print(f"Dados salvos em {nome_arquivo} com sucesso!")

if __name__ == "__main__":
    pessoa = coletar_dados()
    salvar_em_json(pessoa)
