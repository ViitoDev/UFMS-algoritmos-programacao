# Módulo 1 - Introdução a algoritmos e programação

Este módulo apresenta os fundamentos da computação e os primeiros conceitos necessários para resolver problemas por meio de algoritmos e programas em Python.

## 1. História e fundamentos da computação

### Por que aprender a programar?

Aprender a programar ajuda a:

- desenvolver a capacidade de resolver problemas;
- desenvolver o pensamento computacional;
- compreender como os computadores recebem e executam instruções;
- aprender uma linguagem que serve de base para outras linguagens de programação.

A linguagem utilizada neste curso é o **Python**, por possuir sintaxe simples e ser bastante usada no ensino introdutório de programação.

### Alguns marcos históricos

- **Ábaco (aproximadamente 2400 a.C.)**: instrumento antigo usado para realizar cálculos.
- **Pascalina (1642)**: máquina mecânica de calcular criada por Blaise Pascal.
- **Máquina Analítica (1822)**: projeto de Charles Babbage que antecipou características dos computadores programáveis.
- **Z1 (1938)**: considerado um dos primeiros computadores eletromecânicos programáveis.
- **Colossus (1943)**: computador usado para auxiliar a decodificação de mensagens durante a Segunda Guerra Mundial.
- **ENIAC (1946)**: um dos primeiros computadores eletrônicos de propósito geral; ocupava uma sala inteira e consumia muita energia.
- **Xerox Alto (1973)**: um dos primeiros computadores pessoais com mouse e interface gráfica.

Atualmente, os computadores aparecem em desktops, laptops, tablets e smartphones. Eles combinam capacidade de processamento, armazenamento, entrada, saída e conectividade.

### Hardware e software

- **Hardware**: conjunto das partes físicas do computador, como processador, memória, teclado e tela.
- **Software**: conjunto de programas e instruções que orientam o funcionamento do hardware.

Um computador é uma máquina capaz de executar programas. Um programa é uma sequência lógica e precisa de instruções para realizar uma tarefa.

### Bits e processamento

Toda informação digital é representada internamente por **bits**, unidades que podem assumir os valores `0` ou `1`. Esses valores correspondem, de forma simplificada, a estados desligado e ligado nos circuitos eletrônicos.

O **microprocessador** interpreta e executa instruções, realizando operações como:

- mover dados;
- somar e subtrair valores;
- comparar informações;
- executar operações lógicas e aritméticas.

### Evolução das linguagens de programação

1. **Linguagem de máquina**: utiliza instruções representadas diretamente em código binário.
2. **Assembly**: usa símbolos mnemônicos e nomes para representar instruções, registradores e endereços, mas ainda mantém uma relação próxima com o hardware.
3. **Linguagens de alto nível**: utilizam sintaxe e conceitos mais próximos da linguagem humana. Um compilador ou interpretador traduz o código para instruções que o computador consegue executar.

Exemplo em Java:

```java
public class HelloPrinter {
    public static void main(String[] args) {
        System.out.println("Hello world!");
    }
}
```

O mesmo exemplo em Python é mais conciso:

```python
print("Hello world!")
```

## 2. Computadores, programas e erros

### O comando `print`

O `print` exibe informações na saída do programa:

```python
print("3 + 4 + 5")
```

Saída:

```text
3 + 4 + 5
```

Quando a expressão não está entre aspas, o Python realiza o cálculo antes de exibir o resultado:

```python
print(3 + 4 + 5)
```

Saída:

```text
12
```

### Principais tipos de erro

- **Erro de sintaxe**: ocorre quando o código não segue as regras da linguagem. O interpretador não consegue traduzi-lo ou executá-lo.
- **Erro de execução**: ocorre durante a execução, como ao tentar dividir um número por zero.
- **Erro de lógica**: o programa é executado, mas produz um resultado diferente do esperado porque o algoritmo está incorreto.

Exemplos:

```python
print(nome_inexistente)
```

O nome não foi definido e causa um `NameError`.

```python
print(27 / 0)
```

A divisão por zero causa um `ZeroDivisionError`.

## 3. Processo de resolução de problemas

A construção de um programa pode ser organizada em quatro etapas, semelhantes aos princípios de resolução de problemas de Pólya:

### 1. Requisitos: compreender o problema

É necessário descobrir **qual problema deve ser resolvido**. Para isso, identifique:

- dados de entrada;
- cálculos e transformações necessários;
- casos especiais;
- dados de saída;
- condições que o problema precisa atender.

### 2. Algoritmo: elaborar um plano

O algoritmo descreve **como resolver o problema** por meio de uma sequência finita de passos. Ele deve ser independente da linguagem de programação escolhida.

Uma analogia comum é a receita de bolo: os ingredientes representam os dados e os passos representam as instruções para obter o resultado.

As principais formas de representar um algoritmo são:

- linguagem natural;
- pseudocódigo ou PORTUGOL;
- fluxograma.

O pseudocódigo é útil porque facilita a compreensão da lógica sem exigir preocupação imediata com a sintaxe de uma linguagem específica.

### 3. Codificação: implementar a solução

Nesta etapa, o algoritmo é transformado em código. Neste curso, a linguagem escolhida é Python.

A linguagem natural nem sempre é adequada para executar instruções, pois pode ser ambígua. Por exemplo, a frase “calcule cinco mais cinco vezes dez” pode ser interpretada como `5 + 5 * 10` ou como `(5 + 5) * 10`. A linguagem de programação exige uma expressão precisa.

### 4. Testes: revisar a solução

Um programa não está concluído apenas porque foi escrito. É necessário executar testes para verificar:

- erros de sintaxe;
- erros de execução;
- resultados incorretos;
- casos normais e casos especiais.

## 4. Algoritmos e ordenação

Algoritmos também podem ser usados para organizar dados. Um exemplo é ordenar cartas de um mesmo naipe do menor valor para o maior.

### Insertion Sort

1. Pegue uma carta da pilha.
2. Coloque-a na posição correta entre as cartas já organizadas.
3. Repita até que todas as cartas estejam ordenadas.

### Selection Sort

1. Procure a menor carta que ainda está na pilha.
2. Retire essa carta e coloque-a ao final da sequência ordenada.
3. Repita até terminar.

### Bubble Sort

1. Compare cartas vizinhas.
2. Troque-as quando estiverem fora de ordem.
3. Repita as passagens até que nenhuma troca seja necessária.

### Bogo Sort

Embaralhe as cartas repetidamente até que, por acaso, elas fiquem ordenadas. É um método extremamente ineficiente, usado apenas como exemplo humorístico.

## 5. Arquitetura abstrata do computador

Uma forma simples de representar o funcionamento de um computador é:

1. **Entrada**: recebe dados por teclado, mouse, câmera ou outros dispositivos.
2. **Processamento**: o processador executa o programa e transforma os dados.
3. **Armazenamento**: a memória e os discos guardam dados temporariamente ou permanentemente.
4. **Saída**: apresenta resultados por tela, impressora, alto-falante ou outros dispositivos.

Uma analogia é imaginar um atendente de help desk:

- os escaninhos representam variáveis e memórias;
- a caixa de entrada representa o teclado;
- a caixa de saída representa o monitor;
- a folha de instruções representa o programa;
- a calculadora representa as operações do processador.

Essa é uma **abstração**: uma representação simplificada que desconsidera detalhes complexos e mantém apenas os elementos importantes para compreender o problema.

## 6. Pseudocódigo e variáveis

Pseudocódigo é uma forma concisa de descrever um algoritmo. Ele não precisa obedecer exatamente à sintaxe do Python.

### Soma de dois números

Pseudocódigo:

```text
Leia A
Leia B
SOMA <- A + B
Escreva SOMA
```

Em Python:

```python
A = int(input())
B = int(input())
SOMA = A + B
print(SOMA)
```

Uma **variável** é um nome associado a um valor armazenado na memória. Na analogia dos escaninhos, cada variável identifica um espaço onde um dado pode ser guardado.

As operações mais comuns são:

- `input()`: recebe dados da entrada;
- `print()`: envia dados para a saída;
- `=`: atribui um valor a uma variável;
- `int()`: converte um valor para inteiro.

## 7. Tipos primitivos de dados

- **Inteiro (`int`)**: números sem parte decimal, como `10` e `-3`.
- **Real (`float`)**: números com parte decimal, como `3.14`.
- **Texto (`str`)**: sequência de caracteres, como `"Python"`.
- **Lógico (`bool`)**: valor `True` ou `False`.

Conhecer o tipo de cada dado é importante para escolher operações compatíveis e evitar resultados inesperados.

## 8. Operadores e expressões

Uma expressão combina valores, variáveis e operadores para produzir um resultado.

### Operadores aritméticos

| Operador | Operação | Exemplo | Resultado |
| --- | --- | --- | --- |
| `**` | Potenciação | `2 ** 3` | `8` |
| `*` | Multiplicação | `5 * 3` | `15` |
| `/` | Divisão | `5 / 3` | `1.666...` |
| `//` | Divisão inteira | `5 // 3` | `1` |
| `%` | Resto da divisão | `5 % 3` | `2` |
| `+` | Soma | `5 + 3` | `8` |
| `-` | Subtração | `5 - 3` | `2` |

Parênteses podem ser usados para alterar a ordem de avaliação:

```python
(1 + 2) * 3  # 9
```

De modo geral, a ordem de prioridade é: parênteses, potenciação, operadores unários, multiplicação/divisão e soma/subtração.

### Operadores relacionais

Operadores relacionais comparam valores e produzem `True` ou `False`:

| Operador | Significado | Exemplo |
| --- | --- | --- |
| `<` | Menor que | `5 < 3` |
| `<=` | Menor ou igual | `5 <= 3` |
| `>` | Maior que | `5 > 3` |
| `>=` | Maior ou igual | `5 >= 3` |
| `==` | Igual a | `5 == 3` |
| `!=` | Diferente de | `5 != 3` |

### Operadores lógicos

Operadores lógicos combinam ou modificam valores booleanos:

| Operador | Significado | Exemplo |
| --- | --- | --- |
| `not` | Negação | `not True` resulta em `False` |
| `and` | E lógico | `True and False` resulta em `False` |
| `or` | OU lógico | `True or False` resulta em `True` |

## 9. Exemplos do diretório

### `hello-world.py`

```python
print("Hello world!")
```

Demonstra a saída de texto usando `print`.

### `soma.py`

```python
a = 10
b = 20
soma = a + b
print(a, "+", b, "=", soma)
```

Demonstra a criação de variáveis, a soma de valores e a exibição de múltiplos elementos.

## Resumo do módulo

Ao final deste módulo, é importante compreender que:

- programas são sequências de instruções precisas;
- algoritmos descrevem soluções antes da implementação;
- um problema deve ser entendido antes de ser codificado;
- variáveis armazenam dados e possuem tipos;
- operadores permitem calcular, comparar e combinar valores;
- testes são essenciais para encontrar erros de sintaxe, execução e lógica;
- Python será a linguagem usada para transformar algoritmos em programas executáveis.
