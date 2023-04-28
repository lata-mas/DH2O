# Dispositivo H2O

Este dispositivo se desarrollo con lel objetivo de medir la cantidad de agua que se consume en un edificio y poder implementar medidas para evitar consumos excesivos de este valioso recurso.

El dispositivo funciona con un módulo NodeMCU Lolin V3→ESP8266-12E, permitiendo interpretar los datos que recolecta el sensor YF-S201 (sensor de caudal de agua), el microcontrolador  permite interpretar datos y después enviarlos a través de Wifi a una plataforma de imternet. La ventaja más significativa es precisamente esa, que el módulo tiene wifi, permitiendo que pueda enviar datos en tiempo real a diferentes plataformas de visualización, ademas de su reducido tamaño.

A continuación se muestra el esquema general del dispositivo y algunos de sus componetes principales:

1. Sensor de caudal
2. Divisor de voltaje
3. LM324

![](https://github.com/Dispositivos-Edificio-Bioclimatico/DH2O/blob/master/Imagenes/h20_esquema_gral.png?raw=true)

[Diagrama electrico](https://github.com/Dispositivos-Edificio-Bioclimatico/DH2O/blob/master/Diagramas/DispositivoH2O1Esquem%C3%A1tico.pdf)

**Sensor de caudal**

Sensor propuesto: YFS-201

 Este sensor se acopla muy bien a la tubería de agua de cualquier edificio o casa y contiene un sensor de molino para medir la cantidad de líquido que ha pasado a través de él. También tiene un sensor magnético de efecto Hall que emite un impulso eléctrico con cada revolución. El sensor de efecto Hall está sellado para permanecer seguro y seco. El sensor viene con tres cables: Rojo (energía 5-24 VDC) Negro (tierra) Amarillo (salida de pulsos de efecto Hall) Al contar los pulsos de la salida del sensor, se puede calcular fácilmente el flujo de agua. Cada pulso es de aproximadamente 2.25 mililitros. 
 
 La señal de pulso es una simple onda cuadrada así que es bastante fácil de registrar y convertir en litros por minuto utilizando la siguiente ecuación.
 
 ![](https://github.com/Dispositivos-Edificio-Bioclimatico/DH2O/blob/master/Imagenes/EcuacionB.PNG?raw=true)


**Divisor de voltaje**

Debido a que el voltaje de operacion de nuestro microcontrolador (ESP8266) es de 3.3v y estamos ocupando una fuente de 5v para alimentar tanto al sensor de caudal como al microcontrolador se implemento un divisor de voltaje que no es mas que un arreglo de resistencias para cuidar la vida util de nuestro ESP.

**LM324**

Este integrado es un amplificador operacional sin embargo tambien tiene la funcion de comparador de voltaje, la cual estamos utilizando para este dispositivo.


La lista de la electronica y materiales del dispositivo se encuentra en el archivo  [materiales](https://github.com/Dispositivos-Edificio-Bioclimatico/DH2O/blob/master/Materiales/Lista_materiales_h2o.xlsx) o en [lista_drive](https://docs.google.com/spreadsheets/d/189IVU7i7mgoemxYWTE_gQPPNS4Jn7LhwTmuZ7sgd4DA/edit#gid=0)

- [ ] Lista de costos
- [ ] SRC completos
- [ ] Pictograma de conexión
- [ ] Esquemático de conexión
- [ ] Archivos de diseño PCB
- [ ] Archivos gerber para el maquinado del PCB
- [x] Lista de materiales
- [ ] Planos CAD
- [ ] Archivos de diseño CAD
- [ ] Archivos STL para impresión 3D
- [ ] Manual de operación
- [ ] Manual de ensamble
- [ ] Fichas técnicas o datasheet de los módulos, sensores y componentes usados
- [ ] Documento de errores, soluciones y recomendaciones

### 1.1 Sobre los autores

|Nombre|Instituto/Organización|Email|
| ------------ | ------------ | ------------ |
|Luis Fernando De Olarte Delgado|UTEZ|ferdeod16@gmail.com|
|Marco Antonio Morales Lagunes|UTEZ|marcostony001@gmail.com|
|Julio César Landa López|UTEZ|landajulioc@gmail.com|
|Miguel Ángel Gaspar|ITZ|miguel97gaz@gmail.com|
|Escobar Escobar José Williams|ITE|escobarescobarwilliams@gmail.com|
|Guillermo Barrios del Valle|IER-UNAM|gbv@ier.unam.mx|
|Guillermo Ramírez Zúñiga|IER-UNAM|guraz@ier.unam.mx|
|Giovanni Velazquez Avilez||velazquezgio96@gmail.com|

------------

# 2. Alcance

El dispositivo H2O tiene como alcance, en esta etapa, contar con toda la documentación necesaria para ser replicado de manera eficaz y eficientemente, después de ser trabajado por un grupo de personas se espera que el proyecto tenga todo lo que se necesita para que otras personas puedan entender el funcionamiento y requisitos de operación.

La audiencia a la que está destinada es:

- Por el momento a personal del IER-UNAM que se encuentra trabajando en el proyecto "Edificios demostrativos de diseño bioclimático en clima cálido subhúmedo en el Instituto de Energías Renovables UNAM".
Proyecto número 291600 del Fondo de Sustentabilidad Energética.
- Compañeros que se interesen en aportar al proyecto para mejorar o para replicarlo directamente.

------------


### 4.5.6 Contacto primario

**Inv. A tiempo completo:** Dr. Guillermo Barrios del Valle

**Email:** gbv@ier.unam.mx



**Posdoc.:** Dr. Guillermo Ramírez Zúñiga

**Email:** guraz@ier.unam.mx

### 4.5.7 Colaboradores

**Nombre:** Luis Fernando De Olarte Delgado

**Instituto:** Universidad Tecnológica Emiliano Zapata (UTEZ)

**Email:** ferdeod16@gmail.com



**Nombre:** Marco Antonio Morales Lagunes

**Instituto:** Universidad Tecnológica Emiliano Zapata (UTEZ)

**Email:** marcostony001@gmail.com



**Nombre:** Julio César Landa López

**Instituto:** Universidad Tecnológica Emiliano Zapata (UTEZ)

**Email:** landajulioc@gmail.com



**Nombre:** Miguel Ángel Gaspar

**Instituto:** Instituto Tecnológico de Zacatepec (ITZ)

**Email:** miguel97gaz@gmail.com



**Nombre:** Escobar Escobar José Williams

**Instituto:** Instituto Tecnológico de Ensenada (ITE)

**Email:** escobarescobarwilliams@gmail.com




#### Seguimiento de actividades del dispositivo H2O

|**Actividad**|**Tiempo estimado de ejecución**|**Referenciación**|
| :------------: | :------------: | :------------: |
|**1. Revisión de documentos existentes necesarios para operarlo de acuerdo a la CHECK-LIST**|2 h|[**°Documentación**](https://github.com/Dispositivos-Edificio-Bioclimatico/SensorH2O/tree/master/Documentacion) [**°Check-List**](https://github.com/Dispositivos-Edificio-Bioclimatico/SensorH2O/blob/master/ChecklistH2O.md)|
|   |   |   |
|**2. Verificar si cuenta con los materiales requeridos**|1/2 h|[**Materiales**](https://github.com/Dispositivos-Edificio-Bioclimatico/SensorH2O/tree/master/Materiales)|
|   |   |   |
|**3. Imprimir la carcasa en 3D (3 PARTES)**|16 h|[**Archivos STL**](https://github.com/Dispositivos-Edificio-Bioclimatico/SensorH2O/tree/master/CAD)|
|   |   |   |
|**4. Instalar Linux**|12 h|Puede realizarse simultáneamente con otras actividades|
|   |   |   |
|**5. Leer el manual de operación para entender lo que se hará**|1 h|[**Manual**](https://github.com/Dispositivos-Edificio-Bioclimatico/SensorH2O/blob/master/Manuales/ManualDeOperacion.md)|
|   |   |   |
|**6. Entender los diagramas de conexión**|1/2 h|[**Diagramas**](https://github.com/Dispositivos-Edificio-Bioclimatico/SensorH2O/tree/master/Diagramas)|
|   |   |   |
|**7. Conectar el ESP a la computadora y configurar el firmware de acuerdo al manual de operación**|1 h|   |
|   |   |   |
|**8. Conectar el ESP a la computadora con el circuito del dispositivo**|1 h|[**Esquemático**](https://github.com/Dispositivos-Edificio-Bioclimatico/SensorH2O/blob/master/Diagramas/EsquematicoKiCADH2O.pdf)|
|   |   |   |
|**9. Descargar e instalar el código completo (son 5 .py)**|1/2 h|[**Código H2O**](https://github.com/Dispositivos-Edificio-Bioclimatico/SensorH2O/tree/master/SRC)|
|   |   |   |
|**Ejecutar el código como primera prueba y asegurarse que funciona**|   |   |
|   |   |   |
|**11. Verificar si envía datos de telemetría correctamente a Thingsboard**|1/2 h|[**°Dashboard**](http://iot.ier.unam.mx:8080/dashboard/5825dc60-059e-11eb-9c3f-d1ead9980bc3?publicId=0e7066c0-6e70-11e8-b1f3-991d62d050bd)|
|   |   |   |
|**12. Montar el dispositivo en el lugar requerido**|1 h|   |
|   |   |   |
|**13. Dejarlo operando durante 24 horas como prueba "Burn it"**|24 h|   |
|   |   |   |
|**Tiempo total apróximado:**|**3 días**|Dependerá de la habilidad y conocimientos que se tengan, puede llevar menos tiempo o más|

------------


### 4.5.9 Fue hecho físicamente

El dispositivo sí se ha hecho de forma práctica, es decir, se ha llevado a la práctica para comprobar el funcionamiento del mismo, solo como pruebas de funcionamiento, el dispositivo completo y funcionando durante largos períodos de tiempo no se ha realizado, falta montarlo completo, que mida 1 conexión de agua y con su respectiva carcasa de protección.

### 4.5.10 Se ha comprobado la documentación

La réplica del dispositivo usando la estructura aquí mostrada y siguiendo la documentación no se ha realizado, aún está en revisión de estructura de documentación y de archivos factibles para el desarrollo eficiente.

### 4.5.11 Estándares usados

El estándar de documentación completo, no se ha seguido, pero si se ha usado el estándar para esta documentación de Open Know-How, algunos puntos se han omitido porque al no ser la estructura para documentar proyectos electrónicos, existen puntos que salen sobrando o que definitivamente no aplican para este tipo de proyectos.
El link del estándar usado es el siguiente:

[EstandarOpenKnowHow](https://app.standardsrepo.com/MakerNetAlliance/OpenKnowHow/src/branch/master/1#a40dfa47-8bff-4e28-9338-3f808ddfe6ae)


### Thingsboard

Dashboard del dispositivo H2O en la plataforma de Thingsboard:

Miguel_H2O

Las credenciales para tener acceso se deberán solicitar con alguno de los doctores.

La web (Dashboard) se encuentra aquí:

[**Miguel_H2O**](http://iot.ier.unam.mx:8080/dashboard/5825dc60-059e-11eb-9c3f-d1ead9980bc3?publicId=0e7066c0-6e70-11e8-b1f3-991d62d050bd)

------------

# 5.0 Bibliografía

[1] Open Know-How
https://app.standardsrepo.com/MakerNetAlliance/OpenKnowHow/src/branch/master/1#a40dfa47-8bff-4e28-9338-3f808ddfe6ae

[2] Github
https://github.com/

[3] EasyEDA
https://easyeda.com/editor

[4] Fritzing
https://fritzing.org/

[5] DILLINGER
https://dillinger.io/

[6] M Editor.md
https://pandao.github.io/editor.md/en.html
