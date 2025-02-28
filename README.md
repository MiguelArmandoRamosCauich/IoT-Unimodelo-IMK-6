# Sistema de Monitoreo de Temperatura IoT

## Descripción
Este proyecto implementa un sistema de monitoreo de temperatura basado en **IoT** con una **Raspberry Pi Pico W** y un **sensor LM35**. Los datos son enviados a **ThingSpeak**, donde se pueden visualizar y analizar mediante **MathWorks**.

## Tecnologías Utilizadas
- **MicroPython**: Para la programación de la Raspberry Pi Pico W.
- **ThingSpeak**: Para almacenar y visualizar datos en la nube.
- **MATLAB (MathWorks)**: Para el análisis de datos y generación de alertas.

## Instalación y Configuración
El LM35 es conectado a al A0 de la Raspberry Pi Pico W, a este último se le sube el archivo main.py del repositorio, el resultado de esto se debería de ver de la siguiente manera:

![image alt](https://github.com/MiguelArmandoRamosCauich/IoT-Unimodelo-IMK-6/blob/be7d7410841e02affcfeead9e20c787c26a87708/Images/ThinSpeakDa.png)

Después de obtener todos los datos necesarios puedes crear una gráfica para ver todos los datos:

![image alt](https://github.com/MiguelArmandoRamosCauich/IoT-Unimodelo-IMK-6/blob/be7d7410841e02affcfeead9e20c787c26a87708/Images/DatosFin.png)

Para el análisis de los datos y la creación de alertas se utiliza el archivo analisis_temperatura.m del repositorio en análisis de MatWorks, este te debe de dar un resultado como:

![image alt](https://github.com/MiguelArmandoRamosCauich/IoT-Unimodelo-IMK-6/blob/be7d7410841e02affcfeead9e20c787c26a87708/Images/MatWorksRes.png)

Una vez que ya se tiene todos los datos y el análisis de MatWorks ya se le puede dar cualquier uso que se quiera para la información recopilada.
