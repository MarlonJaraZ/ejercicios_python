# Clean Data ejemplos
import pandas as pd 
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