# PLCP - Programação e Lógica Computacional

## 📚 Sobre o Projeto

Este repositório contém uma coleção de programas educacionais organizados por semestre/disciplina do curso de Ciência da Computação. Os códigos estão comentados em português para facilitar o aprendizado de estudantes.

---

## 🗂️ Estrutura do Repositório

### 📘 1º Semestre - PLCP (Pensamento Lógico Computacional em Python)

Esta disciplina introduz os fundamentos da programação utilizando Python.

#### Programas Básicos
| Arquivo | Descrição |
|---------|-----------|
| `Ola.py` | Programa "Hello World" básico |
| `Media.py` | Calcula a média aritmética de três números |
| `IMC.py` | Calcula o Índice de Massa Corporal |
| `Area-Circulo.py` | Calcula a área de um círculo |
| `Par ou Impar.py` | Verifica se um número é par ou ímpar |
| `Maior Número entre Dois.py` | Encontra o maior entre dois números |
| `Zero Negativo Positivo.py` | Classifica números como zero, negativo ou positivo |

#### Estruturas de Repetição (Laços)
| Arquivo | Descrição |
|---------|-----------|
| `Contagem Regressiva.py` | Realiza contagem regressiva |
| `Soma dos Números de 1 a N.py` | Soma números de 1 até N |
| `Tabuada de um Número.py` | Exibe a tabuada de um número |
| `Vogais.py` | Conta vogais em uma palavra |

#### Matemática e Algoritmos
| Arquivo | Descrição | Complexidade |
|---------|-----------|--------------|
| `primo.py` | Verifica se um número é primo | O(√n) |
| `fatorial.py` | Calcula o fatorial de um número | O(n) |
| `fibonacci.py` | Gera a sequência de Fibonacci | O(n) |
| `palindromo.py` | Verifica se uma palavra é palíndromo | O(n) |
| `juros.py` | Calcula juros compostos | O(1) |

#### Estruturas de Dados
| Arquivo | Descrição | Complexidade |
|---------|-----------|--------------|
| `pilha.py` | Implementação de Pilha (LIFO) | O(1) push/pop |
| `fila.py` | Implementação de Fila (FIFO) | O(1) enqueue/dequeue |
| `l.py` | Operações com Listas | - |

#### Programação Orientada a Objetos e Arquivos
| Arquivo | Descrição |
|---------|-----------|
| `class.py` | Demonstração de classes e POO |
| `json.py` | Manipulação de arquivos JSON |
| `template.py` | Template para novos programas |

---

### 📗 2º Semestre - Programação Estruturada em C

Esta disciplina aprofunda conceitos de programação utilizando a linguagem C.

| Arquivo | Descrição |
|---------|-----------|
| `velocidade.c` | Calcula velocidade média |
| `tabuada.c` | Exibe a tabuada de um número |
| `jogo_da_velha.c` | Jogo da Velha com IA (Minimax + Alpha-Beta) |

---

## 🚀 Como Executar

### Requisitos

**Para Python:**
- Python 3.6 ou superior

**Para C:**
- Compilador GCC ou compatível

### Executando Programas Python

```bash
# Navegar até o diretório do projeto
cd PLCP

# Executar qualquer programa Python
python3 Ola.py
python3 IMC.py
python3 primo.py
```

### Compilando e Executando Programas C

```bash
# Compilar um programa C
gcc velocidade.c -o velocidade

# Executar o programa compilado
./velocidade

# Para o jogo da velha (Windows)
gcc jogo_da_velha.c -o jogo_da_velha
./jogo_da_velha
```

---

## 📝 Padrão de Código

Todos os scripts seguem um padrão consistente:

### Python
```python
"""
nome_arquivo.py - Descrição breve

Descrição:
    Explicação detalhada do que o script faz.

Autor: Projeto PLCP - Xº Semestre
"""

def funcao_principal():
    """
    Docstring explicando a função.
    """
    # Comentário explicativo
    pass

def main():
    # Entrada: descrição
    # Processamento: descrição
    # Saída: descrição
    pass

if __name__ == '__main__':
    main()
```

### C
```c
/**
 * nome_arquivo.c - Descrição breve
 * 
 * Descrição:
 *     Explicação detalhada.
 * 
 * Autor: Projeto PLCP - Xº Semestre
 */

#include <stdio.h>

int main() {
    // Comentários explicativos
    return 0;
}
```

---

## 🤝 Como Contribuir

1. Faça um fork do repositório
2. Crie uma branch para sua feature (`git checkout -b feature/nova-feature`)
3. Commit suas mudanças (`git commit -m 'Adiciona nova feature'`)
4. Push para a branch (`git push origin feature/nova-feature`)
5. Abra um Pull Request

### Convenções
- Comentários em português
- Seguir PEP 8 para Python
- Indentação consistente em C
- Nomes de variáveis descritivos

---

## 📖 Recursos de Aprendizado

- [Python Documentation (PT-BR)](https://docs.python.org/pt-br/3/)
- [Learn C](https://www.learn-c.org/)
- [Estruturas de Dados](https://www.geeksforgeeks.org/data-structures/)
- [Big-O Cheat Sheet](https://www.bigocheatsheet.com/)

---

## 📄 Licença

Este projeto é destinado para fins educacionais.

---

**Desenvolvido para aprendizado de programação** 🚀
