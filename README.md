Consigna del TP4 de AED - UTN - FRC

Nuestro cliente de librería digital ha diversificado su negocio a otras plataformas,
por lo cual nos pide un nuevo sistema que acompañe esta evolución.

Los libros ahora se encuentran en un archivo de texto libros.csv

Título, Cantidad de revisiones, Año de publicación,
código de idioma (un valor entre 1 y 27), Rating e ISBN.

abrir el archivo con:
m = open("libros.csv", mode="rt", encoding="utf8")

Se pide desarrollar un menú con las siguientes opciones:

    *Cargar*: Cargar el contenido del archivo en un vector de registros de libros,
    que siempre debe mantenerse ordenado por isbn (Omitir la primera línea del archivo,
    que contiene el nombre de los campos)

    *Sumar revisión*: El usuario puede optar por buscar el libro por ISBN o por título.
    Según el criterio elegido se debe ingresar por teclado el ítem a buscar.
    Si existe en el vector el libro con el criterio buscado,  mostrar sus datos y
    sumar una revisión al mismo. Si no existe mostrar un mensaje por pantalla.

    *Mayor Revisiones*: Buscar en el vector el libro con mayor cantidad de revisiones.
    Informar si su rating es mayor, menor o igual al rating promedio de su mismo idioma.

    *Popularidad 2000*: A partir del vector, generar una matriz donde cada fila sea un idioma
    y cada columna un año de publicación. La celda debe contener el libro que tenga
    mayor rating para ese idioma y año (si hubiera varios, elegir sólo uno)
    sólo para los libros publicados entre el año 2000 y el 2020 (ambos incluídos).

    *Publicaciones por década*: A partir del vector, generar un vector de conteo
    donde cada celda representa una década entre 1900 y 2000. La celda debe indicar
    cuántos libros se publicaron en ese año. Mostrar todas las cantidades mayores a cero.
    Informar además cuál fue la década con más publicaciones.
    Si varias tuvieran la misma cantidad, informar todas.

    *Guardar populares*: Si la matriz de la opción 4 ya fue generada, almacenar
    su contenido registros por registro (omitiendo las celdas vacías) en un archivo binario
    llamado populares.dat e informar la cantidad de registros grabados.
    Si la matriz aún no fue generada, informarlo.

    *Mostrar archivo*: Listar el contenido del archivo generado en el punto anterior.
