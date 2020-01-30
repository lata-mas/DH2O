from wifi import do_connect  #importa función para conexión wifi de wifi.py
from machine import Pin      #libreria para utilizar los GPIO's de la esp
from funcion import *        #importar la función para publicar el thingsboard

#importar librerías
import time
import utime
import network
import sys

#Declaración de variables
T=0
contador = 0
tot=0
t = 0

#función que realizara el conteo digital para el sensor
def my_callback(l):
    global contador,tot
    contador = contador +1
    tot = contador  

#declarar el pin de entrada como trigger y mandando a llamar la función callback  
inpt = Pin(4, Pin.IN)
inpt.irq(trigger=Pin.IRQ_RISING, handler=my_callback)    


#configuración del network
sta_if = network.WLAN(network.STA_IF)
sta_if.active(True)

#Declaración de labels y arreglos para exportar a thingsboard
label  = 'Litros'
label1 = 'flujo'
data  = {label: 0}
data1 = {label1:0}
red = 'IER'                #Red de internet
clave = 'acadier2014'      #contraseña de la red

#credenciales del dispositivo configurado en thingsboard
unique_id = 'cd95f150-dfa3-11e9-b63c-1566f7f95663'   
token = 'Ods8RX9h6I2Vdq2gIvbf'                       

#Conexión a internet
ap_if = network.WLAN(network.AP_IF)
sta_if.connect(red,clave)
cnt_boot = 0                 #conteo de intentos de conexión
cont = 0
print ("antes")

while True:                       #Loop infinito

#Constantes de conversión del sensor
  T = ((contador*1.0)/320)
  t = ((tot* 60 )/ 6.6166666667)

  try:

#publicación de dtos en thingsboard
    data[label] = T
    data1[label1] = t
    print("Publishing data")
    publish_thingsboard(token, unique_id,data)
#    publish_thingsboard(token, unique_id,data1)
    cnt_boot = 0
    contador = 0
    cont = 1

#reintentar conexión en caso de fallo
  except Exception as inst:
    print(inst)
    do_connect(red,clave);
    cnt_boot += 1
    cont += 1
    print("Fail {}".format(cnt_boot))
    if cont >1:
        contador = contador
    if cnt_boot > 10: #si falla la reconexión mas de diez veces se reinicia el dispositivo
      machine.reset()
    time.sleep(1)
  time.sleep(30)
  
      
