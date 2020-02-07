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
lbl2 = 'Litros 2'
lbl3 = 'Litros 3'
lbl4 = 'Litros 4'
lbl5 = 'Litros 5'

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

#Declaración del sensor2
Sensor2 = Conteo(pin = 4) #Pin al que estará asignado el sensor
Sensor2.irq()

#Declaración del sensor3
Sensor3 = Conteo(pin = 5) #Pin al que estará asignado el sensor
Sensor3.irq()

#Declaración del sensor4
Sensor4 = Conteo(pin = 18) #Pin al que estará asignado el sensor
Sensor4.irq()

#Declaración del sensor5
Sensor5 = Conteo(pin = 19) #Pin al que estará asignado el sensor
Sensor5.irq()

#-------------------------Loop infinito----------------------------------
while True:

#Función para las ecuaciones del sensor
  T1 = ecuaciones(Sensor1.contador)
  T2 = ecuaciones(Sensor2.contador)
  T3 = ecuaciones(Sensor3.contador)
  T4 = ecuaciones(Sensor4.contador)
  T5 = ecuaciones(Sensor5.contador)

  try:

#Empaquetado de datos para publicar en Thingsboard
    datS1 = datos(T1,lbl)
    datS2 = datos(T2,lbl2)
    datS3 = datos(T3,lbl3)
    datS4 = datos(T4,lbl4)
    datS5 = datos(T5,lbl5)

#publicación de datos en thingsboard
    print("Publishing data S1")
    publish_thingsboard(token, unique_id,datS1)

    print("Publishing data S2")
    publish_thingsboard(token, unique_id,datS2)

    print("Publishing data S3")
    publish_thingsboard(token, unique_id,datS3)

    print("Publishing data S4")
    publish_thingsboard(token, unique_id,datS4)

    print("Publishing data S5")
    publish_thingsboard(token, unique_id,datS5)

 #Reinicio de variables
    cnt_boot = 0
    Sensor1.contador = 0
    Sensor2.contador = 0
    Sensor3.contador = 0
    Sensor4.contador = 0
    Sensor5.contador = 0
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
        Sensor2.contador = Sensor2.contador
        Sensor3.contador = Sensor3.contador
        Sensor4.contador = Sensor4.contador
        Sensor5.contador = Sensor5.contador
    if cnt_boot > 10: #si falla la reconexión mas de diez veces se reinicia el dispositivo
      machine.reset()
    time.sleep(1)
  time.sleep(10)
