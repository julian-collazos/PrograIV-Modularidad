import API.api as api
import UI.ui as interfaz

lim, dep = interfaz.menu_principal()

informacion = api.consultar_datos(lim, dep)
informacion_filtrada = api.filtrar_datos(informacion)
indexes_renombrados = interfaz.renombrar_columnas(informacion_filtrada)
interfaz.mostrar_tablas(indexes_renombrados)
