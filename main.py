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
unique_id = 'ccfb8fa0-4157-11ea-9ffe-35550336f914'   
token = 'PLcwc21L7r7JuGvfHHVi' 

#Etiquetas para publicar en thingsboard
lbl  = 'Litros'
lbl1 = 'flujo'

#variables para los intentos de conexión
cnt_boot = 0                
cnt = 0

#configuración del network
sta_if = network.WLAN(network.STA_IF)
sta_if.active(True)
                      
#Conexión a internet
ap_if = network.WLAN(network.AP_IF)
sta_if.connect(red,clave)

print ("antes")

#-------------------------Loop infinito----------------------------------
while True:                      

#Función que realiza el conteo digital del pin 
  contador1,tot1 = conteo(4)

#Función para las ecuaciones del sensor
  T1,t1 = ecuaciones(contador1,tot1)

  try:

#Empaquetado de datos para publicar en Thingsboard
    datS1,dat1S1 = datos(T1,t1,lbl,lbl1)

#publicación de datos en thingsboard
    print("Publishing data")
    publish_thingsboard(token, unique_id,datS1)
    publish_thingsboard(token, unique_id,dat1S1)

#Reinicio de variables
    cnt_boot = 0
    reinicio(contador1) #función que reinicia el contador
    cnt = 1

#reintentar conexión en caso de fallo
  except Exception as inst:
    print(inst)
    do_connect(red,clave);
    cnt_boot += 1
    cnt += 1
    print("Fail {}".format(cnt_boot))
    if cnt >1:
        contador1 = contador1
    if cnt_boot > 10: #si falla la reconexión mas de diez veces se reinicia el dispositivo
      machine.reset()
    time.sleep(1)
  time.sleep(30)
  
      
