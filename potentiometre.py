from machine import ADC, Pin
from time import *

can = ADC(Pin(34))               # crée un objet ADC sur la broche 34
can.atten(ADC.ATTN_11DB)         # étendue totale : 3.3V
#ADC.width(ADC.WIDTH_10BIT)       # change la résolution du convertisseur à 10bits

while True:
    pot = can.read()        # conversion analogique-numérique 0-4095
    print("CAN =", pot)     # affichage sur la console REPL de la valeur numérique
    sleep_ms(100)
"""

from machine import Pin, ADC, PWM
from time import sleep

# Configuration du potentiomètre (entrée analogique)
pot = ADC(Pin(34))
pot.atten(ADC.ATTN_11DB)  # Plage de 0 à 3.3V

# Configuration de la LED (sortie PWM)
led = PWM(Pin(5), freq=5000)

while True:
    # Lecture de la valeur du potentiomètre (0 à 4095)
    pot_value = pot.read()
    
    # Conversion de la valeur du potentiomètre en valeur de PWM (0 à 1023)
    pwm_value = int(pot_value / 4095 * 1023)
    
    # Ajustement de la luminosité de la LED
    led.duty(pwm_value)
    
    # Pause pour éviter de surcharger le processeur
    sleep(0.1)
"""