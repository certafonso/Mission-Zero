# Mission Zero

Este guia é fortemente inspirado no [guia passo a passo](https://projects.raspberrypi.org/pt-PT/projects/astro-pi-mission-zero) presente na página do projeto.

## O que é o Astro PI?

O Astro PI é um computador 

![Astro Pi](https://www.raspberrypi.org/app/uploads/2021/08/Astro-PI-IRvis-900x506.jpg)

## O que é a Mission Zero?

Em conjunto com a Agência Espacial Europeia (ESA), a Raspberry Pi Foundation quer introduzir mais jovens ao mundo da programação, para isso criaram a Mission Zero em que vão ter a opurtunidade de fazer um pequeno programa para ler a humidade na ISS e enviar uma mensagem as astronautas.

## Como programar em python

Um programa de computador é apenas um ficheiro de texto escrito numa linguagem especifica, que o computador vai compilar em instruções que o processador do computador consegue entender.

Para programarem em python a unica coisa que precisam e escrever o vosso programa usando um editor de texto qualquer (podem usar o notepad, mas normalmente usa-se um editor mais avançado como o VSCode que faz coisas mais avançadas como detetar erros ou completar comandos). Tendo o vosso programa escrito só precisam de o correr, tendo o python instalado no computador.

No entanto, nesta atividade vamos usar um editor de codigo online chamado [trinket](https://trinket.io/mission-zero). Assim vamos puder escrever o nosso codigo e corre-lo sem precisar de instalar nada no computador. Além disso, este site simula o computador Astro PI.

### Hello World

Vamos começar por fazer o programa mais básico possivel, escrever escrever uma mensagem na linha de comandos. Para isso vamos usar a função `print()`.

```python
print("Hello World")
```

Dentro dos parenteses tem aqui a que se chama o argumento da função. A função print tem apenas um argumento: o texto que irá ser escrito. Este texto tem de estar entre aspas para o python o reconhecer como texto (string), e não como um comando ou variável.

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
```

O código acima, apesar de dar para perceber que se estão a multiplicar dois numeros, não está escrito da melhor maneira. Não dá para perceber o que significa cada numero, ou qual o significado do seu produto. 

Um exemplo de bons nomes de variáveis seria este:

```python
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

Se um numero for par, o resto da sua divisão por 2 será 0. Assim, para verificarmos se o numero é par precisamos de verificar essa condição (`numero % 2 == 0`), se a condição for verdadeira, o numero é par e escrevemos isso no ecrã, caso contrário, o numero é impar e então escrevemos isso no ecrã.

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

Todas as linguagens de programação oferecem loops que vão facilitar muito esta tarefa. Um loop (ou um ciclo), como o nome indica permite executar uma secção de código várias vezes de seguida. No python existem dois tipos de loop: `for` e `while`. Vamos começar por ver o `while`.

```python
while condição:
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

### Bibliotecas

Para fazer coisas comuns, muitas vezes já houve alguém a fazer esse código e o disponibilizou para toda a gente poder usar livremente. A esses conjuntos de programas chamam-se bibliotecas.

Para importarem uma destas bibliotecas para poderem usar no vosso programa usam o seguinte código:

```python
# importar a biblioteca time
import time

# mostrar o tempo atual
print(time.asctime())
```

O código acima importa a biblioteca `time` e depois usa função `asctime()` dessa biblioteca para imprimir no ecrã a data e hora atual.

Outra maneira, muita vezes preferivel, de fazer o mesmo é esta:

```python
# importar a função asctime da biblioteca time
from time import asctime

# mostrar o tempo atual
print(asctime())
```

Com este exemplo estamos a importar apenas a função que queremos usar. Esta forma é preferivel se apenas precisarmos de algumas funções da biblioteca uma vez que o programa apenas coloca na memória as funções que vamos utilizar e não gasta espaço com coisas que não nos são uteis.

Quando instalam o python já existem algumas bibliotecas instaladas, por exemplo a biblioteca `math` que tem algumas funções matemáticas como funções trigonométricas e constantes como o pi. No entanto, para participar na Mission Zero, só podemos usar a biblioteca `random` que permite gerar numeros aleatórios, a biblioteca `time` que permite fazer coisas relacionadas com tempo, como obter a data ou fazer uma pausa no programa e a bilioteca `sense_hat` que nos permite controlar o sense hat.

## Sense Hat

Chega de teoria, vamos então começar a utilizar o nosso computador!

### Inicializações

Primeiro vamos importar a biblioteca do sense hat e fazer algumas inicializações.
        
```python
# importar a biblioteca do SenseHat
from sense_hat import SenseHat

# Inicializar o SenseHat e a rotação dos sensores
sense = SenseHat()
sense.set_rotation(270)
```

### Mostrar Mensagem

Depois de feitas as inicializações vamos então aos básicos: mostrar texto no ecrã LED. Para isso usamos a função `show_message()`.

```python
sense.show_message("Astro Pi")

# mudar velocidade, velocidade padrão é 0.1
sense.show_message("Astro Pi", scroll_speed=0.05)
```

Esta função apenas aceita estes caracteres:

```
+-*/!"#$><0123456789.=)(

ABCDEFGHIJKLMNOPQRSTUVWXYZ

abcdefghijklmnopqrstuvwxyz

?,;:|@%[&_']\~
```

### Mudar as cores

Escrever apenas texto a branco é aborrecido... Felizmente a função `show_message()` permite-nos escolher a cor do texto e do fundo.

```python
# variavel com tupple (R,G,B)
red = (255,0,0)
green = (0,255,0)
sense.show_message("Astro Pi", text_colour=red, back_colour=green)
```

Para definir as cores estamos a usar um tipo diferente de variáveis chamado tupple. Ao abrimos parenteses podemos por mais do que um número dentro de uma variável, estes números tem de estar separados por virgulas.

Para definir uma cor estamos a definir 3 numeros diferentes (todos podem tomar valores entre 0 e 255). O primeiro é a quantidade de vermelho que a cor tem, o segundo a quantidade de verde e, por ultimo a quantidade de azul. A mistura destas 3 cores dá-nos a nossa cor.

Para facilitar a escolha de cores podem usar este [site](https://www.w3schools.com/colors/colors_rgb.asp) para misturarem a cor que quiserem.

### Imagens

Também podem desenhar uma imagem no ecrã, para isso usa-se a função `set_pixels()`:

```python
# definir cores
w = (255, 255, 255)
b = (0, 0, 0)
g = (50,50,50)
s = (200,255,200)
r = (255,0,0)

# imagem a desenhar (8x8)
imagem = [
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
sense.set_pixels(imagem)
```

Para definir a imagem usa-se uma lista, que funciona da mesma forma que um tupple, mas usando-se parenteses retos. O primeiro elemento desta lista representa o primeiro pixel na linha de cima, o segundo representa o pixel seguinte, e por aí fora.

A vantagem das listas em relação às tupples é que podes alterar um elemento especifico da lista, por exemplo:

```python
# definir a lista
lista = [1,2,3,4,5,6]

# mudar o 1º elemento da lista para 3
lista[0] = 3

# mudar o 6º elemento da lista para ser igual ao 3º
lista[5] = lista[2]
```

Para conseguires desenhar melhor a tua imagem, podes começar por a desenhar numa folha quadriculada e depois passa-la para o programa.

### Sleep

Se quiserem mostrar várias imagens diferentes precisam de fazer uma pausa no programa para dar tempo de se ver a imagem. Conseguem fazer isso através da função `sleep()` da biblioteca `time`.

```python
# importar a função
from time import sleep

# fazer uma pausa no programa durante 2 segundos
sleep(2)
```

### Ler humidade

O objetivo do programa que estão a fazer é mostrar a humidade aos astronautas da ISS. Para lerem a humidade do sensor usam a função `get_humidity`.

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

### Ideias

Está na hora de criares o teu programa, tens aqui algumas ideias de coisas que podes fazer:

- Desenhar o lenço do grupo
- Fazer transições entre imagens
- Reagir à humidade, se estiver acima de um valor mostram uma mensagem/imagem, se estiver abaixo mostram outra.
- Mostrar a data
- Tentar usar tudo o que aprenderam agora

### Ideias para explorar mais

Se já acabaste o teu programa e queres explorar mais tens aqui algumas ideias:

- [Flappy Astronaut](https://projects.raspberrypi.org/en/projects/flappy-astronaut/0)
- [Marble Maze](https://projects.raspberrypi.org/en/projects/sense-hat-marble-maze/0)
- [Jogo da Vida](https://pt.wikipedia.org/wiki/Jogo_da_vida)

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