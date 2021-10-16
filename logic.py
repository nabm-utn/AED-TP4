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
    if revisar_orden(catalogo):
        print("Se ha cargado el catálogo con éxito!")
    else:
        print("Ha ocurrido un error.")


def busqueda_secuencial_titulo(catalogo, titulo):
    for libro in catalogo:
        if libro.titulo == titulo:
            return libro
    return False


def solicitar_isbn():
    isbn = input('Código de Identificación (ISBN): ')
    while len(isbn) == 0:
        print("El código no puede estar vacío...")
        isbn = input('Código de Identificación (ISBN): ')
    return isbn


def solicitar_titulo():
    titulo = input('Título: ')
    while len(titulo) == 0:
        titulo = input('Título (No puede estar vacío): ')
    return titulo


def sumar_revision(catalogo):
    """
    El usuario puede optar por buscar el libro por ISBN o por título.
    Según el criterio elegido se debe ingresar por teclado el ítem a buscar.
    Si existe en el vector el libro con el criterio buscado,  mostrar sus datos y
    sumar una revisión al mismo. Si no existe mostrar un mensaje por pantalla.
    """
    opcion = None
    menu = """
Cómo desea realizar su búsqueda?
1) Busqueda por ISBN
2) Búsqueda por título
3) Volver al menú principal
"""
    while opcion != "3":
        libro = None
        print(menu)
        opcion = input('Ingrese opción: ')
        if opcion == "1":
            isbn = solicitar_isbn()
            indice = busqueda_binaria_indice(catalogo, isbn) - 1
            libro = catalogo[indice]
        elif opcion == "2":
            titulo = solicitar_titulo()
            libro = busqueda_secuencial_titulo(catalogo, titulo)

        if libro:
            print("Se encontró su libro!")
            print(libro)
            print("\nAñadiendo revisión...")
            libro.revisiones += 1
            print("Este libro tiene ahora {} revisiones!".format(libro.revisiones))

        else:
            if opcion != "3":
                print("No se encontró su libro. Intente realizar otra búsqueda.")


def libro_mas_revisado(catalogo):
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
        promedio = acumulador / contador
        return round(promedio, 2)
    return None


def mayor_revisiones(catalogo):
    """
    Buscar en el vector el libro con mayor cantidad de revisiones.
    Informar si su rating es mayor, menor o igual al rating promedio de su mismo idioma.
    """
    libro = libro_mas_revisado(catalogo)
    libros_mismo_idioma = subvector_idioma(catalogo, libro.idioma)
    rating_promedio = calcular_rating_promedio(libros_mismo_idioma)
    print("El libro con más revisiones es:")
    print(libro)
    print("El rating promedio para el idioma {} es: {}".format(libro.idioma, rating_promedio))
    msj = "...\nEl rating de su libro es {} con respecto al promeido para su idioma..."
    if libro.rating > rating_promedio:
        msj = msj.format("mayor")
    elif libro.rating < rating_promedio:
        msj = msj.format("menor")
    else:
        msj = msj.format("igual")
    print(msj)


def popularidad_2000(catalogo):
    matriz = [[Libro("none", 0, 0, 0, 0, "__________") for año in range(2000, 2021)] for idioma in range(1, 28)]
    for libro in catalogo:
        if 2000 <= libro.año <= 2020 and libro.rating > matriz[libro.idioma - 1][libro.año - 2000].rating:
            matriz[libro.idioma - 1][libro.año - 2000] = libro
    print("Se ha generado la matriz con éxito!")
    return matriz


def mostrar_matriz(matriz):
    txt = "\t\t" + "\t\t".join(["{:04d}".format(i) for i in range(2000, 2021)])
    for idioma in range(1, 28):
        txt += "\n{:02d}\t".format(idioma) + "\t".join([libro.isbn for libro in matriz[idioma-1]])
    print(txt+"\n")


def publicaciones_por_decada(catalogo):
    """
    A partir del vector, generar un vector de conteo
    donde cada celda representa una década entre 1900 y 2000. La celda debe indicar
    cuántos libros se publicaron en esa decada. Mostrar todas las cantidades mayores a cero.
    Informar además cuál fue la década con más publicaciones.
    Si varias tuvieran la misma cantidad, informar todas.
    """
    decadas = [str(i) for i in range(1900, 2000, 10)]
    publicaciones = [0] * 10
    for libro in catalogo:
        if 1900 <= libro.año <= 1999:
            bin = (libro.año - 1900) // 10
            if bin > 0:
                publicaciones[bin] += 1

    publicaciones_max = 0
    decadas_productivas = []
    for i in range(10):
        if publicaciones[i] > publicaciones_max:
            publicaciones_max = publicaciones[i]
            decadas_productivas = [decadas[i]]
        elif publicaciones[i] == publicaciones_max:
            decadas_productivas.append(publicaciones[i])

    print("Decada | Publicaciones")
    for i in range(10):
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
    if not os.path.exists(filename):
        print("El archivo no existe!")
        return
    filesize = os.path.getsize(filename)
    archivo = open(filename, "rb")

    print("Libros contenidos en el archivo: \"{}\"\n".format(filename))
    while archivo.tell() < filesize:
        libro = pickle.load(archivo)
        print(libro)
