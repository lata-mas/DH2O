#Función constantes del sensor
def ecuaciones(contador,tot):
    T = ((contador*1.0)/320)
    t = ((tot* 60 )/ 6.6166666667)
    return T,t 


#Función que empaqueta los datos para ser publicados en Thingsboard
def datos(T,t):
    data  = {'Litros': 0}
    data1 = {'Flujo':0}
    data['Litros'] = T
    data1['Flujo'] = t
    return data,data1 
