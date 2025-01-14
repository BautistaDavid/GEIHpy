## GeihdanePy
___

##### **It's time for the GEIH to know python** 

[![PyPI package](https://img.shields.io/badge/pip%20install-geihdanepy-red)](https://pypi.org/project/geihdanepy/) [![License](https://img.shields.io/badge/license-MIT-red)](https://github.com/BautistaDavid/geihdanepy/blob/main/LICENSE)


**Geihdanepy es un paquete de python para facilitar el uso de los datos de la Gran Encuestra Integrada de Hogares del DANE.**

## **Descripción**

El paquete ```geihdanepy``` nace de la idea de estudiantes de economía para facilitar la investigación científica - académica usando los datos de la Gran Encuesta Integrada de Hogares, una de las más importantes bases de datos que proporciona de forma abierta el Departamento Nacional de Estadística **DANE**. 

## **¿Como usar geihdanepy?**

#### Primero lo primero 

Para empezar a trabajar con geihdanepy se debe realizar la instalación del paquete usando el comando ```pip install geihdanepy```. Cuando el paquete este instalado procedemos a importarlo.

```python
import geihdanepy as geih
```

## ¡Accedemos a los datos!

Ahora que el paquete está instalado podemos seguir la siguiente sintaxis para solicitar una de las diferentes tablas que ofrece la GEIH.

```python
df = geih.datos(2015,'Octubre','Ocupados','Cabecera')
```

Por otro lado, si usted está familiarizado con la GEIH sabrá que esta cuenta principalmente con dos factores de caracterización de los datos aparte de la fecha, los cuales son el módulo y la zona a la que se hace referencia.

De manera que si quiere conocer cómo funciona la sintaxis dentro de  ```geihdanepy``` para hacer referencia los diferentes módulos y zonas puede hacerlo usando las siguientes funciones.

```python
geih.info_modulos()   # Acceder a información de los Modulos 
```

```python
geih.info_zonas()   # Acceder a información de las zonas
```

## Actualización GEIH Marco 2018

El Departamento de Estadística Nacional en colombina DANE cambio el marco metodológico de la GEIH a partir del año 2022, para el caso del módulo geihdanepy se generaron nueva funciones que permiten interactuar con la información publicada para el año 2022 y 2023 (próximamente).

```python
import geihdanepy as geih

df = geih.datos_marco_2018(2022,'Enero','Ocupados')

## Para acceder a información sobre los modulos de la GEIH Marc0 2018 dentro de las funciones

geih.info_modulos_marco2018()
```


