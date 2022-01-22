# Este programa lê a humidade e mostra, durante 30s, uma imagem diferente, consoante o nivel de humidade

# importar a biblioteca do SenseHat
from sense_hat import SenseHat
from time import sleep

# Inicializar o SenseHat e a rotação dos sensores
sense = SenseHat()
sense.set_rotation(270)

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

sleep(30)

sense.clear()