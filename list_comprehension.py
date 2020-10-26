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

###### Otro Ejemplo #########

# list comprehension 

pair2 = [(num1, num2) for num1 in range (0,2) for num2 in range(6,8)] 
print(pair2)

# condicional list comprehension
# podemos agregar condicionales IF en el "iterable" o en el "output exp"

# iterable

[num_cond ** 2 for num_cond in range(10) if num_cond % 2 == 0]
# devuelve los cuadrados hasta el numero 10 unicamente de los numeros pares.

# en output exp

[num_cond2 ** 2 if num_cond2 % 2 == 0 else 0 for num_cond2 in range (10)]
# devuelve los cuadrados hasta el 10, si el resultado es impar, regresa 0