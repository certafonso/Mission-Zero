# Este programa lê a humidade e mostra-a na matriz LED do SenseHat

# importar a biblioteca do SenseHat
from sense_hat import SenseHat

# Inicializar o SenseHat e a rotação dos sensores
sense = SenseHat()
sense.set_rotation(270)

# ler humidade
humidade = sense.get_humidity()

# arredondar para uma casa decimal
humidade = round(humidade, 1)

# mostrar no escrã
sense.show_message(str(humidade))

# concatenar strings
sense.show_message( "It is " + str(humidade) + " %" )