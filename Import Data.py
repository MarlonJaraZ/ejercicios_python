# importar datos
# instalar SQLAlchemy: pip install SQLAlchemy
# instalar PyMySQL: pip install pyMySQL
# archivo sql

# 1. importar paquetes y funciones
from sqlalchemy import create_engine
import pandas as pd 

# 2. crear engine 
engine = create_engine ('mysql+pymysql://user:password@localhost:3306/nombre_BD')

# 3. conectar
con = engine.connect()

# 4. Consultar datos
rs = con.execute ("SELECT * FROM nombre_tabla WHERE id = 173")

# 5. Importar datos
df = pd.DataFrame(rs.fetchall())
df.columns = rs.keys()    # nombres de las columnas como estan en BD

# 6. cerrar conexion
con.close()

# ver primeras lineas
print(df.head())

# obtener nombres de las tablas
table_names = engine.table_names()
print(table_names)

################
# pandas query
# pasos 1 y 2
# aquí ya trae los nombres de los campos

df_2 = pd.read_sql_query("SELECT * FROM nombre_tabla", engine)
print(df_2.head())