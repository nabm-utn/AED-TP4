from libro import Libro
import os.path
import pickle


def busqueda_binaria_indice(arreglo, nuevo_isbn):
    """
    Encuentra mediante búsqueda binaria la posición de inserción
    de un nuevo libro en un arreglo, de acuerdo a su isbn.
    Si el isbn ya existe en el arreglo, entonces retorna ¿la posición anterior?
    """
    min = 0
    max = len(arreglo) - 1
    while min <= max:
        mid = min + (max - min) // 2
        if arreglo[mid].isbn > nuevo_isbn:
            max = mid - 1
        else:
            min = mid + 1
    return min


def insertar_libro(arreglo, libro):
    """
    Inserta un libro en el arreglo de manera que este se mantenga ordenado según ISBN.
    Utiliza el algoritmo de inserción directa con búsqueda binaria
    """
    indice = busqueda_binaria_indice(arreglo, libro.isbn)
    arreglo[indice:indice] = [libro]


def revisar_orden(arreglo):
    """
    Revisa que los libros de un arreglo estén ordenados de manera ascendente por ISBN.
    """
    for i in range(1, len(arreglo)):
        if arreglo[i].isbn < arreglo[i-1].isbn:
            return False
    return True


def cargar(catalogo, filename="libros.csv"):
    """
    Cargar el contenido del archivo en un vector de registros de libros,
    que siempre debe mantenerse ordenado por isbn (Omitir la primera línea del archivo,
    que contiene el nombre de los campos)
    """
    file = open(filename, "rt", encoding="utf8")
    lines = file.readlines()[1:]
    for line in lines:
        args = line.strip().split(",")
        insertar_libro(catalogo, Libro(*args))
    print("Catalogo ordenado:", revisar_orden(catalogo))


def sumar_revision():
    """
    El usuario puede optar por buscar el libro por ISBN o por título.
    Según el criterio elegido se debe ingresar por teclado el ítem a buscar.
    Si existe en el vector el libro con el criterio buscado,  mostrar sus datos y
    sumar una revisión al mismo. Si no existe mostrar un mensaje por pantalla.
    """
    pass


def libro_revisado(catalogo):
    revisiones_max = 0
    libro_mas_revisado = None
    for libro in catalogo:
        if libro.revisiones > revisiones_max:
            revisiones_max = libro.revisiones
            libro_mas_revisado = libro
    return libro_mas_revisado


def subvector_idioma(catalogo, idioma):
    subvector = []
    for libro in catalogo:
        if libro.idioma == idioma:
            subvector.append(libro)
    return subvector


def calcular_rating_promedio(catalogo):
    contador = 0
    acumulador = 0
    for libro in catalogo:
        contador += 1
        acumulador += libro.rating
    if contador != 0:
        return acumulador / contador
    return None


def menor_votado(catalogo):
    """
    Buscar en el vector el libro con mayor cantidad de revisiones.
    Informar si su rating es mayor, menor o igual al rating promedio de su mismo idioma.
    """
    libro = libro_revisado(catalogo)
    libros_mismo_idioma = subvector_idioma(catalogo, libro.idioma)
    rating_promedio = calcular_rating_promedio(libros_mismo_idioma)
    print("El libro con más revisiones es:")
    print(libro)
    print("El rating promedio para el idioma {} es: {}".format(libro.idioma, rating_promedio))


def mejor_libro_por_año(catalogo, año):
    rating_max = 0
    mejor_libro = Libro("none", 0, 0, 0, 0, "__________")
    for libro in catalogo:
        if libro.año == año and libro.rating > rating_max:
            mejor_libro = libro
            rating_max = libro.rating
    return mejor_libro


def mostrar_matriz(matriz):
    txt = "\t\t" + "\t\t".join(["{:04d}".format(i) for i in range(2000, 2021)])
    for idioma in range(1, 28):
        txt += "\n{:02d}\t".format(idioma) + "\t".join([libro.isbn for libro in matriz[idioma-1]])
    print(txt+"\n")


def popularidad_2000(catalogo):
    """
    A partir del vector, generar una matriz donde cada fila sea un idioma
    y cada columna un año de publicación. La celda debe contener el libro que tenga
    mayor rating para ese idioma y año (si hubiera varios, elegir sólo uno)
    sólo para los libros publicados entre el año 2000 y el 2020 (ambos incluídos).
    """
    matriz = []
    for idioma in range(1, 28):
        fila = []
        subvector = subvector_idioma(catalogo, idioma)
        for año in range(2000, 2021):
            fila.append(mejor_libro_por_año(subvector, año))
        matriz.append(fila)
    return matriz


def publicaciones_por_decada(catalogo):
    """
    A partir del vector, generar un vector de conteo
    donde cada celda representa una década entre 1900 y 2000. La celda debe indicar
    cuántos libros se publicaron en ese año. Mostrar todas las cantidades mayores a cero.
    Informar además cuál fue la década con más publicaciones.
    Si varias tuvieran la misma cantidad, informar todas.
    """
    decadas = [str(i) for i in range(1900, 2001, 10)]
    publicaciones = [0] * 11
    i = 0
    for libro in catalogo:
        i += 11
        if 1900 <= libro.año <= 2009:
            bin = (libro.año - 1900) // 10
            if bin > 0:
                publicaciones[bin] += 1

    publicaciones_max = 0
    decadas_productivas = []
    for i in range(11):
        if publicaciones[i] > publicaciones_max:
            publicaciones_max = publicaciones[i]
            decadas_productivas = [decadas[i]]
        elif publicaciones[i] == publicaciones_max:
            decadas_productivas.append(publicaciones[i])

    print("Decada | Publicaciones")
    for i in range(11):
        if publicaciones[i] > 0:
            print("{:>6} | {:<}".format(decadas[i], publicaciones[i]))
    print("decada(s) con más publicaciones: " + ", ".join(decadas_productivas))


def guardar_populares(matriz, filename):
    """
    Si la matriz de la opción 4 ya fue generada, almacenar
    su contenido registros por registro (omitiendo las celdas vacías) en un archivo binario
    llamado populares.dat e informar la cantidad de registros grabados.
    Si la matriz aún no fue generada, informarlo.
    """
    archivo = open(filename, "wb")
    libros_grabados = 0
    for fila in matriz:
        for libro in fila:
            if libro:
                libros_grabados += 1
                pickle.dump(libro, archivo)
    print("Trabajo completado con éxito!")
    print("Se grabaron {} registros en el archivo \"{}\"".format(libros_grabados, filename))


def mostrar_archivo(filename):
    """
    Listar el contenido del archivo generado en el punto anterior.
    """
    filesize = os.path.getsize(filename)
    archivo = open(filename, "rb")

    print("Libros contenidos en el archivo: \"{}\"\n".format(filename))
    while archivo.tell() < filesize:
        libro = pickle.load(archivo)
        print(libro)
