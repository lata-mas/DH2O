# SensorH2O
Repositorio para el proyecto de los sensores de flujo de agua para el nuevo edificio del IER-UNAM.

Esta versión del proyecto se conforma de un código modular para facilitar la manipulación de ciertos parámetros que nos ayuden a monitorear el flujo de agua en una tubería o si se requiere hasta 8 tuberías.

En este repositorio se encuentran los codigos requeriods parael funcionamiento del dispositivo.
El mismo se conforma por:

- main.py
- wifi.py
- funciones.py
- funcion.py

A continuación se explicara brevemente el funcionamiento de cada modulo

#### main.py

Este es el principal script de dispositivo y se ejcuta inmediatamente el ESP es alimentado.

Se encarga de declarar las variables las variables necesarias para activar al sensor por medio del llamado a funciones.py
entra en un bucle while y realiza las mediciones, espera 10 segundos a una nueva acción y publica el resultado en Thinsboard.


## funciones.py

**Clase conteo**

Esta clase crea un objeto, este objeto será el sensor que se utilizará para la medición del flujo de agua.

La clase se compone de seis métodos. 

**Método init**

El método **init** no es más que para definir la varibale contador y la variable de entrada pin.

**Método callback**

El método **callback** es el que sirve para aumentar en 1 la variable contador cada señal recibida.

**Método irq**

El método **irq** es el que detecta cada pulso digital y envía la señal al metodo callback.

**Método ecuaciones**

Este método es el que aplica las constantes de conversión al conteo de pulsos digitales para así obtener una variable en Litros.

**Método datos**

Este método tan solo sirve para empaquetar los datos junto con una etiqueta para que estén listos.
para ser publicados en Thingsboard.	

**Método publica**

Este metodo se encarga de verificar si hay algún consumo de agua, de serlo así almacena los datos, en cuanto detecta que ya no lo hay, comineza un conteo, el conteo se interrumpe si vuelve a haber consumo, si el conteo concluye, publica los datos en Thingsboard.


#### wifi.py y funcion.py
Esots archivos son los encargados de realizar la conexión a internet y al servidor de Thingsboard del IER-UNAM


**Última actualización de códigos por José Diego**

