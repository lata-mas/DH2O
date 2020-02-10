# SensorH2O
Repositorio para el proyecto de los sensores de flujo de agua para el nuevo edificio

Esta versión del proyecto se conforma de un código modular para facilitar la manipulación de ciertos parametros que nos ayuden
a monitorear el flujo de agua en una toma.

a continuación se explican cada una de las funciones definidas en el archivo "funciones.py"

******Clase conteo********

Esta clase crea un objeto, este objeto será el sensor que se utilizara parala medición del flujo de agua.
La clase se compone de seis metodos. 

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

------Metodo publica----------
Este metodo se encarga de verificar si hay algún consumo de agua, de serlo así lamacena los datos, en cuanto detecta que ya no lo hay comineza un conteo, el conteo se interrumpe si vuelve a haber consumo, si el conteo concluye, publica los datos en Thingsboard.
