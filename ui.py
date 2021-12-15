from tabulate import tabulate


def menu_principal():
    limite = input("Digite la cantidad de datos que desea consultar: ")
    departamento = input("Ingrese el nombre del departamento del que desea conocer los datos: ")
    nombre_departamento = departamento.upper()
    return limite, nombre_departamento


def renombrar_columnas(datos_filtrados):
    datos_filtrados.columns = ['Ciudad de ubicacion', 'Departamento', 'Edad', 'Tipo',
                               'Estado', 'Pais de procedencia']
    return datos_filtrados


def mostrar_tablas(datos_renombrados):
    print(tabulate(datos_renombrados, headers='keys', tablefmt='psql'))
