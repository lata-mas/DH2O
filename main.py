from wifi import do_connect  #importa función para conexión wifi de wifi.py
from funcion import *        #importar la función para publicar el thingsboard
from funciones import *      #funciones para hacer el código modular

#importar librerías
import time
import utime
import network
import sys

#Datos de la red de internet
red = 'IER'                #Red de internet
clave = 'acadier2014'      #contraseña de la red

#credenciales del dispositivo configurado en thingsboard
unique_id = 'fd382bc0-49d5-11ea-9ffe-35550336f914'
token = 'Njk5bs2q53mUSXfdvlqc'

#Etiquetas para publicar en thingsboard
lbl  = 'Litros 1'

#variables para los intentos de conexión
cnt_boot = 0
cont = 0

#configuración del network
sta_if = network.WLAN(network.STA_IF)
sta_if.active(True)

#Conexión a internet
ap_if = network.WLAN(network.AP_IF)
sta_if.connect(red,clave)

print ("antes")

#Declaración del sensor1
Sensor1 = Conteo(pin = 2) #Pin al que estará asignado el sensor
Sensor1.irq()


#-------------------------Loop infinito----------------------------------
while True:

#Función para las ecuaciones del sensor
  T1 = ecuaciones(Sensor1.contador)

  try:

#Empaquetado de datos para publicar en Thingsboard
    datS1 = datos(T1,lbl)

#publicación de datos en thingsboard
    print("Publishing data S1")
    if T1 != 0.0:
        publish_thingsboard(token, unique_id,datS1)
    else:
        print("No hay datos")

 #Reinicio de variables
    cnt_boot = 0
    Sensor1.contador = 0
    cont = 1

#reintentar conexión en caso de fallo
  except Exception as inst:
    print(inst)
    do_connect(red,clave);
    cnt_boot += 1
    cont += 1
    print("Fail {}".format(cnt_boot))
    if cont >1:
        Sensor1.contador = Sensor1.contador
    if cnt_boot > 10: #si falla la reconexión mas de diez veces se reinicia el dispositivo
      machine.reset()
    time.sleep(1)
  time.sleep(10)
