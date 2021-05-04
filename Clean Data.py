# Clean Data ejemplos
import pandas as pd 
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# importar datos
df_bikes = pd.read_csv('datos/ride_sharing_new.csv',
                        index_col= 0)

print(df_bikes.head())

# ver tipo de datos de cada columna
df_bikes.info()

################## variable categorica 

# convertir columna "user_type" a variable categorica
df_bikes["user_type_cat"] = df_bikes["user_type"].astype("category")

df_bikes["user_type_cat"].dtype
df_bikes["user_type_cat"].describe()

# grafico por tipo de usuario
sns.countplot(x = "user_type_cat", data = df_bikes)
plt.show()
############## eliminar texto .str.strip
# el campo duracion está como texto:

df_bikes["duration"].head()
df_bikes["duration"].describe()

# cada valor esta compañado del texto "minutes"

# eliminar el texto con .strip()
df_bikes["duration_texto"] = df_bikes["duration"].str.strip("minutes")
df_bikes["duration_texto"].head()

# sige como texto, ahora a numero
df_bikes["duration_time"] = df_bikes["duration_texto"].astype("int")
df_bikes["duration_time"].describe()

# histograma de la duracion
sns.distplot(df_bikes["duration_time"])

# el maximo es irregular, por ello el histograma tiene cola muy larga
# vamor a verlo

df_bikes[df_bikes["duration_time"]> 120]
# de hecho son 83 registros de mas de 120 minutos.

###### Fechas
# columna de año de nacimiento

df_bikes["user_birth_year"].head()
df_bikes["user_birth_year"].describe()

# año minimo es 1901, es decir, personas de mas de 100 años!
# calculemos edad basados en el año 2020

df_bikes["age"]  = 2020 - df_bikes["user_birth_year"]
df_bikes["age"].describe()
# edad min 19 años, promedio 36. Percentil 75% es de 42 años.

df_bikes["age"].value_counts() 

# histograma
sns.distplot(df_bikes["age"])

################# Duplicados, usamos .duplicated e indicamos el campo

duplicados = df_bikes.duplicated(subset = "bike_id", keep = False)
duplicados.value_counts()
df_bikes["bike_id"].value_counts()

############## crear rangos para agrupar datos
# rango numericos

# importar nuevo dataset

airlines = pd.read_csv("datos/airlines_final.csv",
                        index_col= 0)

print(airlines.head())

# info
airlines.info()

# la idea es crear grupos a partir del campo wait_min,
# que representa el tiempo de espera: 1 hora, 2 hora y mas 2 horas

# crear los rangos
rangos = [0, 60, 180, np.inf]

# crear las etiquetas de los rangos de espera
rangos_etiq = ["corta", "media", "larga"]

# creamos nueva columna usando pd.cut 

airlines["tiempo_espera"] = pd.cut(airlines["wait_min"], 
                                    bins = rangos,
                                    labels = rangos_etiq)

# verificamos contenido .unique()
airlines["tiempo_espera"].unique()

# grafica
sns.countplot(airlines["tiempo_espera"])

# ahora agrupamos con texto.
# agrupar por dias labores (weekday) y fin de semana (weekend)
airlines["day"].unique()

# creamos diccionario para mapear dato del campo "day"
mapear = {"Monday":"weekday",
          "Tuesday":"weekday",
          "Wednesday":"weekday",
          "Thursday":"weekday",
          "Friday":"weekday",
          "Saturday":"weekend",
          "Sunday":"weekend"}

# Usamos reemplazar en nueva columna
airlines["tipo_dia"] = airlines["day"].replace(mapear)

#grafica
sns.countplot(airlines["tipo_dia"])

####### eliminar partes de texto
# elimar los prefijos en los nombres 

# reemplazar Dr. Mr. Miss. Ms.
airlines['full_name'] = airlines['full_name'].str.replace("Dr.","")
airlines['full_name'] = airlines['full_name'].str.replace("Mr.","")
airlines['full_name'] = airlines['full_name'].str.replace("Miss","")
airlines['full_name'] = airlines['full_name'].str.replace("Ms.","")

# verificamos
assert airlines['full_name'].str.contains('Ms.|Mr.|Miss|Dr.').any() == False

######### tratar fechas
# introduccion a trabajar con fechas

df_bancos = pd.read_csv("datos/banking_dirty.csv",
                        index_col = 0)

df_bancos.head()

# cambiar formato en el campo datetime

df_bancos["account_opened"] = pd.to_datetime(df_bancos["account_opened"],
                                            # detecta el formato
                                            infer_datetime_format = True,
                                            # trata errores con missin value
                                            errors = "coerce")

df_bancos["account_opened"].head(n=20)
df_bancos["account_opened"].isna().sum()

# consistencia en campos con suma de otros campos
# validar que inv_amount sea igual a la suma de los fondos A B C D

columnas_fondos = ['fund_A','fund_B','fund_C','fund_D']

# validamos y creamos objetos con True - False
# axis = 1 configurar que la suma sea por filas
ver_fondos = df_bancos[columnas_fondos].sum(axis = 1) == df_bancos["inv_amount"]

# creamos df consistentes e inconsistentes

consistente_inversion = df_bancos[ver_fondos]
print(consistente_inversion.head())

# al usar el ~ trae los False 
inconsistente_inversion = df_bancos[~ver_fondos]
print(inconsistente_inversion.head())

print("numero de registros inconsistentes en inversion ", inconsistente_inversion.shape[0])

####### missin values

df_bancos.isna().sum()      # no missing values

# visualizar missing data matrix

import missingno as msno

msno.matrix(df_bancos)
plt.show()


tabla_excel = pd.read_excel("datos\Datos.xlsx")

tabla_excel.head()
tabla_excel.describe()
tabla_excel.info()

# muestra los NaN
tabla_excel.isna() 

# por columna imprime si hay NaN
tabla_excel.isna().any()

# cuenta los NaN
tabla_excel.isna().sum()

# grafica de NaN
tabla_excel.isna().sum().plot(kind = "bar")
plt.show()

type(tabla_excel)

# seleccionar las 5 primeras columnas 
definitiva = tabla_excel.iloc[:,0:6]

# ver primera filas
definitiva.head()

sns.countplot(x = "Cuenta", data=definitiva)
plt.show()
