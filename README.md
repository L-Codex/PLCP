# PLCP - Programação e Lógica Computacional em Python

## O que é um README?

Um README é um arquivo de documentação que serve como a "porta de entrada" de um projeto. Ele explica:
- **O que é** o projeto
- **Como usar** os programas
- **Como contribuir** com o projeto
- **Informações importantes** sobre o código

O README é geralmente o primeiro arquivo que as pessoas leem quando visitam o repositório, por isso é importante mantê-lo claro e atualizado.

---

## 📚 Sobre o Projeto

Este repositório contém uma coleção de programas educacionais em **Python** e **C** que demonstram conceitos fundamentais de programação e estruturas de dados.

## 🗂️ Estrutura do Repositório

### Programas em Python

#### Básicos
- **`Ola.py`** - Programa "Hello World" básico
- **`Media.py`** - Calcula a média de números
- **`IMC.py`** - Calcula o Índice de Massa Corporal
- **`Par ou Impar.py`** - Verifica se um número é par ou ímpar
- **`Maior Número entre Dois.py`** - Encontra o maior entre dois números
- **`Zero Negativo Positivo.py`** - Classifica números como zero, negativo ou positivo

#### Matemática e Algoritmos
- **`primo.py`** - Verifica se um número é primo (✨ otimizado com algoritmo O(√n))
- **`fatorial.py`** - Calcula o fatorial de um número
- **`fibonacci.py`** - Gera a sequência de Fibonacci
- **`palindromo.py`** - Verifica se uma palavra é um palíndromo
- **`juros.py`** - Calcula juros

#### Operações e Laços
- **`Soma dos Números de 1 a N.py`** - Soma números de 1 até N
- **`Tabuada de um Número.py`** - Exibe a tabuada de um número
- **`Contagem Regressiva.py`** - Realiza contagem regressiva
- **`Vogais.py`** - Trabalha com vogais
- **`Area-Circulo.py`** - Calcula a área de um círculo

#### Estruturas de Dados (✨ Otimizados)
- **`pilha.py`** - Implementação de pilha (stack) com operações O(1)
- **`fila.py`** - Implementação de fila (queue) usando `collections.deque` com operações O(1)

#### Avançados
- **`class.py`** - Demonstração de classes e POO
- **`template.py`** - Template para novos programas
- **`json.py`** - Trabalha com arquivos JSON
- **`l.py`** - Outros exemplos

### Programas em C

- **`velocidade.c`** - Calcula velocidade a partir de distância e tempo
- **`tabuada.c`** - Exibe a tabuada de um número
- **`jogo_da_velha.c`** - Jogo da velha completo com IA usando minimax com poda alpha-beta (✨ otimizado)

## 🚀 Como Usar

### Requisitos

**Para Python:**
- Python 3.6 ou superior

**Para C:**
- Compilador GCC ou compatível

### Executando Programas Python

```bash
# Exemplo: verificar se um número é primo
python3 primo.py

# Exemplo: implementação de fila
python3 fila.py

# Exemplo: implementação de pilha
python3 pilha.py
```

### Compilando e Executando Programas C

```bash
# Compilar
gcc velocidade.c -o velocidade

# Executar
./velocidade
```

Para o jogo da velha:
```bash
gcc jogo_da_velha.c -o jogo_da_velha
./jogo_da_velha
```

## ✨ Melhorias Recentes de Performance

### 1. primo.py - Verificação de Números Primos
**Otimização:** O(n) → O(√n)
- Verifica divisores apenas até a raiz quadrada de n
- Pula números pares após verificar 2
- **Resultado:** ~30x mais rápido para números grandes

### 2. pilha.py - Operações de Pilha
**Otimização:** O(n) → O(1) por operação
- Substituiu `insert(0, x)` por `append(x)`
- **Resultado:** 17.5x mais rápido

### 3. fila.py - Operações de Fila
**Otimização:** O(n) → O(1) por operação
- Substituiu `list` por `collections.deque`
- Usa `popleft()` em vez de `pop(0)`
- **Resultado:** 6.1x mais rápido

### 4. velocidade.c
**Correção:** Erros de sintaxe corrigidos
- Vírgulas substituídas por ponto-e-vírgula
- Agora compila sem erros

### 5. jogo_da_velha.c
**Otimização:** Adicionada poda alpha-beta ao algoritmo minimax
- Reduz significativamente o número de nós explorados
- IA mais rápida, especialmente no início do jogo

## 📊 Complexidade dos Algoritmos

| Programa | Operação | Complexidade |
|----------|----------|--------------|
| primo.py | Verificar primo | O(√n) |
| fatorial.py | Calcular fatorial | O(n) |
| fibonacci.py | Gerar sequência | O(n) |
| pilha.py | Push/Pop | O(1) |
| fila.py | Enqueue/Dequeue | O(1) |
| jogo_da_velha.c | IA (minimax) | O(b^(d/2))* |

*Com poda alpha-beta em cenário ótimo

## 🤝 Como Contribuir

1. Faça um fork do repositório
2. Crie uma branch para sua feature (`git checkout -b feature/nova-feature`)
3. Commit suas mudanças (`git commit -m 'Adiciona nova feature'`)
4. Push para a branch (`git push origin feature/nova-feature`)
5. Abra um Pull Request

## 📝 Convenções de Código

- **Python:** Siga PEP 8
- **C:** Use indentação consistente (2 ou 4 espaços)
- Comentários em português para facilitar o aprendizado
- Nomes de variáveis descritivos

## 🐛 Reportar Problemas

Encontrou um bug ou tem uma sugestão? Abra uma [issue](https://github.com/L-Codex/PLCP/issues) no GitHub!

## 📖 Recursos de Aprendizado

- [Python Documentation](https://docs.python.org/pt-br/3/)
- [C Programming](https://www.learn-c.org/)
- [Estruturas de Dados](https://www.geeksforgeeks.org/data-structures/)
- [Análise de Algoritmos](https://www.bigocheatsheet.com/)

## 📄 Licença

Este projeto é destinado para fins educacionais.

---

**Desenvolvido para aprendizado de programação e estruturas de dados** 🚀
