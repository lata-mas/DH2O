from machine import Pin      #libreria para utilizar los GPIO's de la esp

#---------------Clase para el conteo digital del pin-----------------#
class Conteo:

#Función que inicializa los valores de la clase
  def __init__(self, pin=0):
    #global contador
    self.contador = 0
    self.inpt = Pin(pin, Pin.IN)

#Función callback que realiza el conteo
  def my_callback(self,l):
    #global contador
    self.contador = self.contador +1
    return self.contador

#Función que detecta un cambio en el pin
  def irq(self):
    self.inpt.irq(trigger=Pin.IRQ_RISING, handler=self.my_callback)
#--------------------------------------------------------------------#

#Función constantes del sensor
def ecuaciones(contador):
    T = ((contador*1.0)/320)
    return T 


#Función que empaqueta los datos para ser publicados en Thingsboard
def datos(T,lbl):
    data  = {lbl: 0}
    data[lbl] = T
    return data 
