from machine import Pin #libreria para utilizar los GPIO's de la esp

#Se inicializan variables de conteo
contador=0
tot=0

#función que realizara el conteo digital del sensor
def conteo(pin):

    #función callback suma cada pulso digital
    def my_callback(l):
        global contador,tot
        contador = contador +1
        tot = contador 

    #declara pin como Trigger y manda a llamar función callback 
    inpt = Pin(pin, Pin.IN)
    inpt.irq(trigger=Pin.IRQ_RISING, handler=my_callback) 
    return contador,tot

#función que reinicia la variable de conteo
def reinicio(l):
    global contador
    contador=0
    return contador

#Función constantes del sensor
def ecuaciones(contador,tot):
    T = ((contador*1.0)/320)
    t = ((tot* 60 )/ 6.6166666667)
    return T,t 


#Función que empaqueta los datos para ser publicados en Thingsboard
def datos(T,t,label,label1):
    data  = {label: 0}
    data1 = {label1:0}
    data[label] = T
    data1[label1] = t
    return data,data1 


