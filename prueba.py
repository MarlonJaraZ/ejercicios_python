# este es el primer comentarios para el archivo de prueba.
# esperemos que todo funciones correctamente

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

data = pd.read_csv("datos/cars.csv")

print(data)

# seleccion
grafica = sns.countplot(data["drives_right"])
grafica.set_title("Titulo")
grafica.set(xlabel = "titulo eje x",
            ylabel = "titulo eje y")
plt.show()
