# algunos ejercicios de graficas con Seaborn

# importar librerias 

import pandas as pd 
import seaborn as sns
import matplotlib.pyplot as plt

# importar datos 

df_grant = pd.read_csv("datos\schoolimprovement2010grants.csv",index_col= 0)

# conozcamos los datos
# dimensiones - tamaño
df_grant.shape

# primeras filas
df_grant.head()

# tipos de datos cada columna
df_grant.info()

# estadistica columna numerica
df_grant.describe()

# grafica displot seaborn 
sns.distplot(df_grant["Award_Amount"])
plt.show()

# modificar los bins
sns.distplot(df_grant["Award_Amount"],
            bins = 20)

# ocultar la curva KDE = kernel density estimate
sns.distplot(df_grant["Award_Amount"],
            bins = 20,
            kde = False)

plt.show()

# sombra en la curva y rug plot
sns.distplot(df_grant["Award_Amount"],
            hist = False,
            rug = True,
            kde_kws = {"shade" : True})

plt.show()