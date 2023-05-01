# Dispositivo H2O

Este dispositivo se desarrollo con lel objetivo de medir la cantidad de agua que se consume en un edificio y poder implementar medidas para evitar consumos excesivos de este valioso recurso.

El dispositivo funciona con un módulo NodeMCU Lolin V3→ESP8266-12E, permitiendo interpretar los datos que recolecta el sensor YF-S201 (sensor de caudal de agua), el microcontrolador  permite interpretar datos y después enviarlos a través de Wifi a una plataforma de imternet. La ventaja más significativa es precisamente esa, que el módulo tiene wifi, permitiendo que pueda enviar datos en tiempo real a diferentes plataformas de visualización, ademas de su reducido tamaño.

A continuación se muestra el esquema general del dispositivo y algunos de sus componetes principales:

1. Sensor de caudal
2. Divisor de voltaje
3. LM324

![](https://github.com/Dispositivos-Edificio-Bioclimatico/DH2O/blob/master/Imagenes/h20_esquema_gral.png?raw=true)

[Diagrama electrico](https://github.com/Dispositivos-Edificio-Bioclimatico/DH2O/blob/master/Diagramas/DispositivoH2O1Esquem%C3%A1tico.pdf)


### 1 Sobre los autores

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
|José Diego Salgado Nieto||salgadojosediego@gmail.com|

------------

# Alcance

El dispositivo H2O tiene como alcance, en esta etapa, contar con toda la documentación necesaria para ser replicado de manera eficaz y eficientemente, después de ser trabajado por un grupo de personas se espera que el proyecto tenga todo lo que se necesita para que otras personas puedan entender el funcionamiento y requisitos de operación.

------------


### Contacto primario

**Inv. A tiempo completo:** Dr. Guillermo Barrios del Valle

**Email:** gbv@ier.unam.mx



**Posdoc.:** Dr. Guillermo Ramírez Zúñiga

**Email:** guraz@ier.unam.mx

### Colaboradores

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


**Nombre:** Salgado Nieto josé Diego
**Insituto** Universidad Tecnológica Emiliano Zapata (UTEZ)
**Email:** salgadojosediego@gmail.com




#### Seguimiento de actividades del dispositivo H2O

|**Actividad**|**Tiempo estimado de ejecución**|**Referenciación**|
| :------------: | :------------: | :------------: |
|**1. Revisión de documentos existentes necesarios para operarlo de acuerdo a la CHECK-LIST**|2 h|[**°Documentación**](https://github.com/Dispositivos-Edificio-Bioclimatico/SensorH2O/tree/master/Documentacion) |
|   |   |   |
|**2. Verificar si cuenta con los materiales requeridos**|1/2 h|[**Materiales**](https://github.com/Dispositivos-Edificio-Bioclimatico/DH2O/tree/master/Documentacion/Materiales)|
|   |   |   |
|**3. Imprimir la carcasa en 3D (3 PARTES)**|16 h|[**Archivos STL**](https://github.com/Dispositivos-Edificio-Bioclimatico/DH2O/tree/master/carcasa)|
|   |   |   |
|**4. Leer el manual de operación para entender lo que se hará**|1 h|[**Manual**](https://github.com/Dispositivos-Edificio-Bioclimatico/DH2O/blob/master/Documentacion/Manuales/ManualDeOperacion.md)|
|   |   |   |
|**5. Entender los diagramas de conexión**|1/2 h|[**Diagramas**](https://github.com/Dispositivos-Edificio-Bioclimatico/DH2O/blob/master/Diagramas/H2O-Esquem%C3%A1tico_2023ver2-KiCad.pdf)|
|   |   |   |
|**6. Descargar e instalar el código completo (son 5 .py)**|1/2 h|[**Código H2O**](https://github.com/Dispositivos-Edificio-Bioclimatico/DH2O/tree/master/codigo)|
|   |   |   |
|**7. Ejecutar el código como primera prueba y asegurarse que funciona**|   |   |
|   |   |   |
|**8. Montar el dispositivo en el lugar requerido**|1 h|   |
|   |   |   |
|**9. Dejarlo operando durante 24 horas como prueba "Burn it"**|24 h|   |
|   |   |   |
|**10. Tiempo total apróximado:**|**3 días**|Dependerá de la habilidad y conocimientos que se tengan, puede llevar menos tiempo o más|

------------

### Thingsboard

Dashboard del dispositivo H2O en la plataforma de Thingsboard:

Miguel_H2O

Las credenciales para tener acceso se deberán solicitar con alguno de los doctores.

La web (Dashboard) se encuentra aquí:

[**Miguel_H2O**](http://iot.ier.unam.mx:8080/dashboard/5825dc60-059e-11eb-9c3f-d1ead9980bc3?publicId=0e7066c0-6e70-11e8-b1f3-991d62d050bd)

------------

# Bibliografía

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
