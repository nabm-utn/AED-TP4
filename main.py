from logic import cargar, sumar_revision, menor_votado, popularidad_2000
from logic import publicaciones_por_decada, guardar_populares, mostrar_archivo


def catalogo_vacio(catalogo):
    if len(catalogo) == 0:
        print("No hay libros cargados en el catalogo. Le sugerimos que se dirija a la opción 1 del menu principal")
        input("...")
        return True
    return False


def menu_de_opciones(catalogo):
    opcion = None
    menu = """
Bienvenido a PyBooks!
-----------------------------------------------------
Menú de opciones   |  Libros disponibles: {}
-----------------------------------------------------
1.) Cargar
2.) Sumar revisión
3.) Menor votado
4.) Popularidad 2000
5.) Publicaciones por década
6.) Guardar populares
7.) Mostrar archivo
8.) Finalizar programa"""
    while opcion != '8':
        print(menu.format(len(catalogo)))
        opcion = input('Ingrese opción: ')
        if opcion == '1':
            cargar(catalogo, "libros.csv")
        elif opcion == '2':
            if catalogo_vacio(catalogo):
                continue
            sumar_revision()
            input("...")
        elif opcion == '3':
            if catalogo_vacio(catalogo):
                continue
            menor_votado(catalogo)
            input("...")
        elif opcion == '4':
            if catalogo_vacio(catalogo):
                continue
            popularidad_2000()
            input("...")
        elif opcion == '5':
            if catalogo_vacio(catalogo):
                continue
            publicaciones_por_decada()
            input("...")
        elif opcion == '6':
            if catalogo_vacio(catalogo):
                continue
            guardar_populares()
            input("...")
        elif opcion == '7':
            if catalogo_vacio(catalogo):
                continue
            mostrar_archivo()
            input("...")
        elif opcion == '8':
            confirmacion = input('Seleccionó finalizar programa. ¿Está seguro que desea salir? s/n: ')
            if confirmacion == 's' or confirmacion == 'S':
                print('Gracias por utilizar este programa. Hasta pronto.')
            else:
                opcion = None
        else:
            print('La opción ingresada no es válida')


if __name__ == "__main__":
    catalogo_principal = []
    menu_de_opciones(catalogo_principal)
