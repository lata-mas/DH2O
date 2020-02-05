#Función constantes del sensor
def ecuaciones(contador,tot):
    T = ((contador*1.0)/320)
    t = ((tot* 60 )/ 6.6166666667)
    return T,t 
