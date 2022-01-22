# Este programa mostra uma mesagem na matriz LED do senseHat

# importar a biblioteca do SenseHat
from sense_hat import SenseHat

# Inicializar o SenseHat e a rotação dos sensores
sense = SenseHat()
sense.set_rotation(270)

sense.show_message("Astro Pi")

# mudar velocidade, velocidade padrão é 0.1
sense.show_message("Astro Pi", scroll_speed=0.05)

# variavel com tupple (R,G,B)
red = (255,0,0)
green = (0,255,0)

# Texto com cores
sense.show_message("Astro Pi", text_colour=red, back_colour=green)