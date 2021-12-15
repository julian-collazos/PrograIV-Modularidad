import pandas as pd
from sodapy import Socrata

# Unauthenticated client only works with public data sets. Note 'None'
# in place of application token, and no username or password:
client = Socrata("www.datos.gov.co", None)


def consultar_datos(limite_registros, nombre_departamento):
    results = client.get("gt2j-8ykr", limit=limite_registros, departamento_nom=nombre_departamento)
    # Convert to pandas DataFrame
    results_df = pd.DataFrame.from_records(results)
    return results_df


def filtrar_datos(datos_df):
    datos_filtrados = datos_df.loc[:, ['ciudad_municipio_nom', 'departamento_nom', 'edad', 'fuente_tipo_contagio',
                                       'estado', 'pais_viajo_1_nom']]
    return datos_filtrados
