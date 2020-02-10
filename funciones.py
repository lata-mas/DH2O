from machine import Pin      #libreria para utilizar los GPIO's de la esp
from funcion import *        #importar la función para publicar el thingsboard

#---------------Clase para el conteo digital del pin-----------------#
class Conteo:

#Función que inicializa los valores de la clase
  def __init__(self, pin=0,seg = 0,label='',token='',unique_id=''):
    self.contador = 0
    self.T = 0
    self.data = 0
    self.con = 0
    self.label = label
    self.token = token
    self.seg = seg
    self.unique_id = unique_id
    self.inpt = Pin(pin, Pin.IN)

#Metodo callback que realiza el conteo
  def my_callback(self,l):
    self.contador = self.contador +1

#Metodo que detecta un cambio en el pin
  def irq(self):
    self.inpt.irq(trigger=Pin.IRQ_RISING, handler=self.my_callback)

#Metodo de constantes del sensor
  def ecuaciones(self):
      self.T = ((self.contador*1.0)/320)

#Metodo que empaqueta los datos para ser publicados en Thingsboard
  def datos(self):
      self.data  = {self.label: 0}
      self.data[self.label] = self.T 

#Metodo que realiza la publicación de datos por persona
  def publica(self):
    if self.inpt.value() == 1:  #entrada ON
        self.con = 0
    else:                          #entrada OFF
        if self.T != 0:                    #si flujo >0
            self.con = self.con +1
            if self.con == self.seg*10:               #si contador = 10
                print("Publicando datos del sensor ",self.label[-1])
                publish_thingsboard(self.token,self.unique_id,self.data)
                self.contador = 0
                self.con = 0
    print('sensor ',self.label[-1],' = ',self.con)
#-------------------------------------------------------------------------#
