# este es el primer comentarios para el archivo de prueba.
# esperemos que todo funciones correctamente

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

x = pd.read_csv("datos/cars.csv")

print(x)

# seleccion
sns.countplot(x["drives_right"])
