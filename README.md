# Astro Pi

Este guia é fortemente inspirado no [guia passo a passo](https://projects.raspberrypi.org/pt-PT/projects/astro-pi-mission-zero) presente na página do projeto.

## O que é o Astro PI?

O Astro PI é um computador 

![Astro Pi](https://www.raspberrypi.org/app/uploads/2021/08/Astro-PI-IRvis-900x506.jpg)

## O que é a Mission Zero?

Em conjunto com a Agência Espacial Europeia (ESA), a Raspberry Pi Foundation quer introduzir mais jovens ao mundo da programação, para isso criaram a Mission Zero em que vão ter a opurtunidade de fazer um pequeno programa para ler a humidade na ISS e enviar uma mensagem as astronautas.

## Porquê aprender programação?

## Como programar em python

https://trinket.io/mission-zero

### Hello World

Vamos fazer o programa mais básico possivel, escrever escrever uma mensagem na linha de comandos. Para isso vamos usar a função `print()`

```python
print("Hello World")
```

### Fazer contas

Computadores são só maquinas de calcular glorificadas, portanto a primeira coisa que tem de aprender a fazer é fazer contas.

No python existem estes operadores para fazer contas:
```python
Adição: x + y
Subtração: x - y
Multiplicação: x * y
Divisão: x / y
Disisão inteira: x // y
Resto: x % y
Potencia: x ** y
```

Assim consegues fazer a tua primeira conta, 1+1 e mostrar o resultado na linha de comandos:

```python
print(1+1)
```

### Variáveis

Já sabes fazer contas usando o python, mas isso é um pouco inutil se não conseguires guardar os resultados. É para isso que servem variáveis.

Uma váriavel é como se fosse um post it onde o computador escreve um numero para poder utilizar mais tarde. Para conseguirem encontrar a variável mais tarde tem de lhe dar um nome.

```python
# Atribuir um valor a cada variável
x = 1
y = 2

# Colocar o Resultado de uma conta numa variável
soma = x + y
```

Os nomes das variáveis tem de seguir algumas regras (diferentes para cada linguagem de programação) no caso do python:

 - Tem de começar com uma letra ou um underscore;
 - Não pode começar com um numero;
 - O nome só pode conter caracteres alpha-numericos (numeros e letras) e underscores;
 - Os nomes das variáveis são case-sensitive, ou seja usar letras maiusculas ou minusculas importa. Por exemplo `foo` será uma variável diferente de `FOO` ou `Foo`;
 - Nomes de funções ou comandos do python não podem ser usados (por exemplo: `print`, `while`, `if`, etc...)

Os nomes das variáveis também devem fazer sentido, de forma a conseguirem olhar para o programa e perceberem o que está a fazer.

```python
# exemplo de maus nomes para variáveis
banana = 4
batata = 5

coelho = banana * batata

print(coelho)

# exemplo de bons nomes para variáveis
base = 4
altura = 5

area = base * altura

print(area)
```

### Condições

Outra coisa importante que o computador sabe fazer é verificar condições. Para isso vamos usar um `if...else`.

```python
if condição:
    faz isto
else:
    faz isto
```

Como o nome indica, se a condição for verdadeira a primeira parte do código vai ser executada, caso contrário, a segunda parte vai ser executada.

A condição vai consistir na comparação de dois numeros (ou variáveis). Para fazer esa comparação pecisam de usar os operadores de comparação:

```python
Maior que: x > y       # verdadeiro se x for maior que y
Menor que: x < y       # verdadeiro se x for menor que y
Igual: x == y          # verdadeiro se x for igual a y
Diferente: x != y      # verdadeiro se x for diferente de y
Maior ou igual: x >= y # verdadeiro se x for maior ou igual y
Menor ou igual: x <= y # verdadeiro se x for menor ou igual y
```

### Ver se um numero é par

Vamos então aplicar isto para fazer um programa que, dado um numero, escreva na linha de comandos de é par ou não.

Solução:

```python
numero = 2

if numero % 2 == 0:
    print("O numero é par")
else:
    print("O numero é impar")
```

### Contar até dez

Vamos então tentar algo um pouco mais complexo: contar até 10.

```python
print("0")
print("1")
print("2")
print("3")
print("4")
print("5")
print("6")
print("7")
print("8")
print("9")
print("10")
```

Pronto, está bem podem fazer isso, mas se eu vos pedir para contarem até 1000000? Se calhar é melhor fazer isto de uma forma mais inteligente...

### Loops

Todas as linguagens de programação oferecem loops que vão facilitar muito esta tarefa. Um loop (ou um ciclo), como o nome indica permite executar uma secção de código várias vezes. No python existem dois tipos de loop: `for` e `while`. Vamos começar por ver o `while`.

```python
while condição
    faz isto
```

O `while` funciona de uma forma parecida ao `if`, a diferença é que, em vez de executar o código apenas uma vez, o `while` repete o código várias vezes enquanto a condição for verdadeira.

Assim torna-se fácil contar até qualquer numero:

```python
LIMITE = 10

i = 0
while i <= LIMITE:
    print(i)
    i += 1 # equivalente a i = i + 1

print("Acabado")
```


## Sense Hat
- Inicializações
        
```python
# importar a biblioteca do SenseHat
from sense_hat import SenseHat

# Inicializar o SenseHat e a rotação dos sensores
sense = SenseHat()
sense.set_rotation(270)
```

- Mostrar Mensagem

```python
sense.show_message("Astro Pi")

# mudar velocidade, velocidade padrão é 0.1
sense.show_message("Astro Pi", scroll_speed=0.05)
```

Caracteres aceites:

```
+-*/!"#$><0123456789.=)(

ABCDEFGHIJKLMNOPQRSTUVWXYZ

abcdefghijklmnopqrstuvwxyz

?,;:|@%[&_']\~
```

- Escolher nome do computador

```python
sense.show_message("My name should be Ada Lovelace")
```

- Escolher cores
- Seletor de cores: [https://www.w3schools.com/colors/colors_rgb.asp](https://www.w3schools.com/colors/colors_rgb.asp)

```python
# variavel com tupple (R,G,B)
red = (255,0,0)
green = (0,255,0)
sense.show_message("Astro Pi", text_colour=red, back_colour=green)
```

- Imagens

```python
# definir variáveis
w = (255, 255, 255)
b = (0, 0, 0)
g = (50,50,50)
s = (200,255,200)
r = (255,0,0)

# imagem a desenhar (8x8)
picture = [
    g, b, b, b, b, b, b, g,
    b, g, g, g, g, g, g, b,
    b, g, b, b, g, w, g, g,
    b, g, b, b, g, g, g, g,
    b, g, g, g, s, s, g, g,
    b, g, r, g, g, g, g, g,
    b, g, g, g, g, g, g, b,
    g, b, b, b, b, b, b, g
    ]

# desenhar a imagem
sense.set_pixels(picture)
```

- Sleep

```python
from time import sleep

sleep(2)
```

- Ler humidade

```python
# ler humidade
humidade = sense.get_humidity()

# arredondar para uma casa decimal
humidade = round(humidade, 1)

# mostrar no escrã
sense.show_message(str(humidade))

# concatenar strings
sense.show_message( "It is " + str(humidade) + " %" )
```

- Reagir à humidade

```python
# definir cores
o=(255,130,0)
b=(0,0,255)
c=(0,150,255)
e=(80,80,80)
g=(0,255,0)
y=(255,255,0)

# definir imagens
wet = [
    b, b, b, b, b, b, b, b,
    b, b, b, b, b, b, b, b,
    b, o, b, o, o, o, b, b,
    b, o, o, o, o, e, o, b,
    b, o, o, o, o, o, o, b,
    b, o, b, o, o, o, b, b,
    b, b, b, b, b, b, b, b,
    b, b, b, b, b, b, b, b
]

dry = [
    c, c, g, g, c, c, c, c,
    c, c, g, g, c, g, c, c,
    g, c, g, g, c, g, c, c,
    g, c, g, g, c, g, c, c,
    g, g, g, g, g, g, c, c,
    c, c, g, g, c, c, c, c,
    y, y, y, y, y, y, y, y,
    y, y, y, y, y, y, y, y
]

# obter humidade
humid = sense.get_humidity()

# decidir que imagem mostrar
humid = sense.get_humidity()
if humid >= 40:
    sense.set_pixels(wet)
else:
    sense.set_pixels(dry)
```