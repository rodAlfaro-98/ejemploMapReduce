# Ejemplo de implementación de MapReduce

- [Ejemplo de implementación de MapReduce](#ejemplo-de-implementación-de-mapreduce)
  - [Bibliotecas empleadas](#bibliotecas-empleadas)
    - [PyPDF2](#pypdf2)
    - [spacy](#spacy)
  - [Archivos contenidos dentro del proyecto](#archivos-contenidos-dentro-del-proyecto)
    - [`userFunctions.py`](#userfunctionspy)
    - [`documentReader.py`](#documentreaderpy)
    - [`test_documentReader.py`](#test_documentreaderpy)
    - [`main.py`](#mainpy)

El presente proyecto es un ejemplo de implementación de MapReduce. A diferencia de una implementación real y completa de la biblioteca, este proyecto funciona de forma local en una sola máquina y únicamente con las funciones definidas por el usuario. Sin embargo, logra ilustrar el funcionamiento básico de MapReduce.

El proyecto funciona recibiendo un documento PDF sencillo y devolviendo un diccionario que contiene las palabras significativas contenidas dentro del documento asociadas a una lista de las ubicaciones en las que se puede encontrar dicha palabra.

## Bibliotecas empleadas

### PyPDF2

### spacy

## Archivos contenidos dentro del proyecto

### `userFunctions.py`

Este archivo representa lo sería creado por un usuario en una implementación real de la biblioteca MapReduce. Contiene la definición de las funciones `Map` y `Reduce`:

- `Map`: Recibe un parámetro `documents` de tipo `list`, el cual representa un documento ya procesado y dividido por un [`DocumentReader`](#documentreaderpy). Devuelve una lista `list` con los pares llave-valor intermedios.
- `Reduce`: Recibe la lista de pares llave-valor `list` y devuelve un diccionario `map` con las palabras asociadas a la lista de sus ubicaciones.

### `documentReader.py`

Contiene la definición de la función `DocumentReader`. Esta función recibe una cadena `docName` que indica el nombre del archivo del PDF que se quiere procesar. Su propósito es separar el contenido del documento por línea y por palabra (empleando la biblioteca [PyPDF2](#pypdf2)), y además utilizar procesamiento inteligente del lenguaje para asegurarse de mantener únicamente palabras significativas (empleando la biblioteca [spacy](#spacy)). El resultado final es una lista de listas `texts`.

### `test_documentReader.py`

Contiene las pruebas unitarias para probar el [`DocumentReader`](#documentreaderpy) junto con las [funciones del usuario](#userfunctionspy) empleando `unittest`. Se realizan dos pruebas: En la primera, el programa debe devolver un valor ya conocido de ubicaciones de una cierta palabra. En la segunda, se comprueba la aparición de una excepción en caso de intentar obtener las ubicaciones de una palabra que no existe en el documento.

### `main.py`

Contiene un ejemplo de un programa en el que se emplean los elementos de la implementación. A partir del PDF `beemovie.pdf`, se le piden al usuario palabras de las que desee conocer su ubicación en el documento. El programa contiene mecanismos para evitar la interrupción de la ejecución en caso de que el usuario ingrese una palabra no contenida en el documento, así como la opción de mostrar el índice ordenado de todas las palabras y su ubicación.
