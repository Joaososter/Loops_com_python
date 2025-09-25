
# 🔄 Estruturas de Repetição (Loops) com Python

Este repositório serve como um guia de referência e consulta rápida sobre as **estruturas de repetição (loops)** na linguagem Python. Loops são ferramentas **fundamentais** na programação, permitindo a execução repetida de um bloco de código, o que economiza tempo e torna os programas mais eficientes e sustentáveis.

> **💡 O que são Loops?** Um loop é uma estrutura que permite indicar a repetição de uma tarefa em um determinado número de vezes. Isso evita a repetição manual de código, o que é contraproducente e torna o programa suscetível a falhas.

---

## 1. Por Que Precisamos de Repetições?

Imagine ter que repetir o mesmo código (como uma estrutura `if`) dez mil vezes para verificar 10.000 linhas de um arquivo. Isso é ineficiente, tedioso e extremamente propenso a falhas, tornando o programa menos passível de manutenção.

**No Contexto de Negócios (Business):**

| Tarefa Comum no Negócio | Solução com Loop |
| :--- | :--- |
| **Processamento de Dados:** Percorrer centenas de linhas em uma planilha do Excel ou extrair dados de uma página web. | Usar um loop para percorrer o arquivo, linha por linha, aplicando a mesma lógica a cada registro. |
| **Geração de Relatórios:** Exibir uma tabuada simples para um usuário. | O loop executa o cálculo de forma automatizada para todos os valores. |
| **Automação de Tarefas:** Verificar constantemente se existem novos arquivos de dados chegando para serem carregados dentro do banco relacional. | Criar um **loop infinito proposital**, pois nem sempre teremos um número definido de repetições. |

---

## 2. Tipos de Loops em Python

Existem dois tipos principais de laços de repetição na maioria das linguagens de programação: o laço **enquanto (`while`)** e o laço **para (`for`)**.

### 2.1. O Laço `while` (Enquanto)

O loop `while` é um laço de repetição **baseado em condição**. Ele continua executando o bloco de código **enquanto** uma condição específica for verdadeira. Não temos um número definido de repetições, apenas uma condição que permite ao loop continuar ou parar.

#### 🚀 Uso Principal
Usado quando você **não tem um número definido de repetições** e precisa que o laço continue *enquanto* uma condição for satisfeita.

#### 📝 Sintaxe e Conceito (Python)

Um exemplo clássico é forçar o usuário a acertar uma resposta (a resposta para a vida, o universo e tudo mais, que é "42").

```python
# Criação da variável com um valor inicial para a condição
resposta = "0"

# O loop ocorre ENQUANTO a resposta for diferente de "42"
while (resposta != "42"):
    # Para cada uma das repetições, o usuário vai submeter uma resposta
    resposta = input("Qual a resposta para a vida, universo e tudo mais?")

# Quando o laço terminar, a condição foi atendida
print("Parabéns, você acertou!")
````

#### Variável Contadora no `while`

A **variável contadora** é uma variável que será usada como condição do loop, sendo incrementada (ou decrementada) a cada volta realizada.

```python
i = 0 # Inicia o contador em 0
while (i < 10): # Repete enquanto 'i' for menor que 10
    print(f"Mais uma mensagem, com i valendo: {i}") # Mensagem exibida
    i = i + 1 # Incrementa a variável a cada volta
# Resultado: Imprime 10 vezes, de 0 a 9.
```

**Pontos de Atenção:** Para manter a equivalência com o laço de incremento, o laço de decremento deve ser ajustado para iniciar em `i=9` e ter a condição `i>=0`.

-----

### 2.2. O Laço `for` (Para)

O laço `for` é a estrutura mais apropriada quando estamos diante de um problema que exige um **número determinado de repetições**. A ideia é determinar um ponto inicial e um ponto final, e a própria estrutura se encarrega de controlar o número de voltas, dispensando a variável contadora manual.

#### 🚀 Uso Principal

Usado para **número determinado de repetições** e para **percorrer objetos iteráveis** (como listas, tuplas, strings, dicionários e o próprio `range`).

#### 📝 A Função `range()`

Em Python, o `for` utiliza a função `range()` para definir o intervalo de valores que a variável contadora assumirá.

| Sintaxe `range()` | Exemplo | Descrição |
| :--- | :--- | :--- |
| `range(fim)` | `range(10)` | Inicia em **0** e vai **até 9** (10 voltas). |
| `range(início, fim)` | `range(1, 15)` | Inicia em **1** e vai **até 14** (14 voltas). |
| `range(início, fim, passo)` | `range(1, 10, 2)` | Inicia em **1**, vai **até 9**, pulando de **2 em 2**. Gerará: 1, 3, 5, 7 e 9. |

#### 💡 Exemplo Prático: Cálculo de Média de Pesos

Este problema exige que se repita uma tarefa 100 vezes (100 caixas) para calcular o peso total e a média.

```python
peso_total = 0.0 # Variável para armazenar o peso total

# Loop para repetir por 100 vezes a solicitação de peso
for x in range(1, 101):
    # Para cada volta, solicita o peso da caixa atual
    peso_atual = float(input("Informe o peso da caixa atual:"))
    
    # Soma o peso da caixa atual ao total
    peso_total = peso_total + peso_atual
    
# A média só pode ser calculada depois que todos os pesos são informados (FORA do loop)
media = peso_total / 100

print("O peso total de caixas é {}. \nA média de peso é {}".format (peso_total, media))
```

-----

## 3\. Resumo e Dicas de Escolha

| Critério | Laço `while` (Enquanto) | Laço `for` (Para) |
| :--- | :--- | :--- |
| **Principal Característica** | Repetição **baseada em condição**. Continua *enquanto* a condição for verdadeira. | Repetição **baseada em iteração**. |
| **Contagem** | Deve ser controlada manualmente com uma variável contadora e ajuste de condição. | Automática, gerenciada pelo `range()` ou pela coleção sendo percorrida. |
| **Quando Usar** | Criação de **menus**, loops potencialmente infinitos, quando o número de repetições é **indeterminado** ou **desconhecido**. | Processamento de objetos iteráveis (listas, strings), ou quando o número de repetições é **conhecido e fixo**. |

```
```
