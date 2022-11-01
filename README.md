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

Importamos PyPDF2 con la finalidad de poder obtener el contenido del documento pdf. Para esto usamos la siguiente función:

- `PyPDF2.PdfReader`: se encarga de leer el documento pdf y retornar un objeto de tipo PdfReader. Este objeto nos permite acceder a las páginas del documento mediante el uso de índices como si fuera un arreglo (reader.pages[i]) e igualmente nos permite obtener una lista con las páginas dentro del documento (reader.pages)

### spacy

Esta biblioteca se utiliza con la finalidad de poder eliminar las palabras dentro del pdf que aparecen muy seguido pero no aportan nada a nuestro documento. Para esto usamos los siguientes elementos:

- `spacy.lang.en`: importamos las funcionalidades de Spacy para trabajar con palabras y frases en inglés.
- `spacy.lang.en.stop_words`: importamos un diccionario que nos indica si una palabra entra en la categoría de stopword (palabras que aparecen mucho pero no aportan nada).

Dentro del programa creamos un objeto nlp (natural language processor) a partir de las funcionalidas del idioma inglés importadas de Spacy (nlp = English()). Posteriormente procesamos cada palabra del documento para obtener las categorías de la palabra (doc = nlp(k)). Después de esto obtenemos el lexema de cada palabra (lexeme = nlp.vocab[word]) y finalmente revisamos si la palabra entra dentro de la categoría de stopwords para ver si la incluimos al índice o no (lexeme.is_stop == False).

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
