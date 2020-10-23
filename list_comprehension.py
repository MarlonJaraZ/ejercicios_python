# list comprehension 
# loop en una sola linea de codigo

# algunos de nombres
nombres = ["Jacinto", "Jacobo", "Jaime", "Juan", "Jenaro"]

# extraer la 3° letra de cada nombre
# loop
tercera_letra = []
for nomb in nombres:
    tercera_letra.append(nomb[2])

print(tercera_letra)

# list comprehension

list_tercera = [letra[2] for letra in nombres ]
print(list_tercera)

# son iguales?
print(tercera_letra == list_tercera)

