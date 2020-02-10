# SensorH2O
Repositorio para el proyecto de los sensores de flujo de agua para el nuevo edificio

Esta versión del proyecto se conforma de un código modular para facilitar la manipulación de ciertos parametros que nos ayuden
a monitorear el flujo de agua en una toma.

a continuación se explican cada una de las funciones definidas en el archivo "funciones.py"

******Clase conteo********

Esta clase es utilizada para realizar el conteo de los pulsos digitales emitidos por el sensor
y deuelve el conteo en la variable contador.
La clase se compone de cinco metodos. 

--------Metodo init-------
El metodo init no es más que para definir la varibale 
contador y la variable deentrada pin.

------Metodo callback--------
El metodo callback es el que sirve para aumentar en 1 la variable contador cada señal recibida.

------Metodo irq---------
El metodo irq es el que detecta cada pulso digital y envía la señal al metodo callback.

------Metodo ecuaciones------
Este metodo es el que aplica las contantes de conversión al conteo de pulsos digitales para así
obtener una variable en Litros.

------Metodo datos-----------
Este metodo tan solo sirve para empaquetar los datos junto con una etiqueta para que estén listos
para ser publicados en Thingsboard.
