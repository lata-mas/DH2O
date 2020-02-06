#Función constantes del sensor
def ecuaciones(contador):
    T = ((contador*1.0)/320)
    return T 


#Función que empaqueta los datos para ser publicados en Thingsboard
def datos(T,lbl):
    data  = {lbl: 0}
    data[lbl] = T
    return data 
