# Este programa mostra uma imagem de um astronauta na matriz LED do SenseHat

# importar a biblioteca do SenseHat
from sense_hat import SenseHat

# Inicializar o SenseHat e a rotação dos sensores
sense = SenseHat()
sense.set_rotation(270)

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