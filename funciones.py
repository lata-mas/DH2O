from machine import Pin      #libreria para utilizar los GPIO's de la esp

#---------------Clase para el conteo digital del pin-----------------#
class Conteo:

#Función que inicializa los valores de la clase
  def __init__(self, pin=0,label=''):
    #global contador
    self.contador = 0
    self.T = 0
    self.data = 0
    self.label = ''
    self.inpt = Pin(pin, Pin.IN)

#Metodo callback que realiza el conteo
  def my_callback(self,l):
    #global contador
    self.contador = self.contador +1
    #return self.contador

#Metodo que detecta un cambio en el pin
  def irq(self):
    self.inpt.irq(trigger=Pin.IRQ_RISING, handler=self.my_callback)

#Metodo de constantes del sensor
  def ecuaciones(self):
      self.T = ((self.contador*1.0)/320)
      return self.T 

#Metodo que empaqueta los datos para ser publicados en Thingsboard
  def datos(self):
      self.data  = {self.label: 0}
      self.data[self.label] = self.T
      return self.data 
#-------------------------------------------------------------------------#
