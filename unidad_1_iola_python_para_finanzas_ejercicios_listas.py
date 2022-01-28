# -*- coding: utf-8 -*-
"""Unidad 1: IOLA Python para finanzas - Ejercicios Listas.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Ja2Qcw8BPIvHHHRTCJEBIe09NkFFUZxV

# Guia de ejercicios de listas
**Profesor**: Ignacio Guardines
<br>
**telegram | twitter** :@nacho_java

#### Ejercicio 1 
- Crear una lista de números, asignarlos a una variable e imprimir dicha variable.
"""







## Posible solución
lista_numero = [1,2,3,4,5,6,7,8,9,10]
print(lista_numero)

## jupyter notebook (aca colab) nos muestra el contenido de la variable
## si esta es puesta en la ultima linea de la celda
lista_numero

"""#### Ejercicio 2 
- a la lista creada anteriormente concatenarle una nueva lista formada por ["uno","dos","tres","cuatro"] el resultado de la concatenación asignarlo a otra variable e imprimirlo.
Nota: hacerlo de las dos maneras
1) lista = lista + ... 
2) y con el syntactic sugar +=

"""







## Solución de las dos formas
## sin asignacion destructiva, lista_numero sigue manteniendo 1,2,3,4
lista_mixta = lista_numero + ["uno","dos","tres","cuatro"]
print(f"en una nueva variable {lista_mixta}")

# Aca si hay asignación destructiva, el contenido de lista_numero se re asigna
lista_numero = lista_numero + ["uno","dos","tres","cuatro"]
print(f"en la misma variable pisando el valor anterior {lista_numero}")
## como en la ejecucion anterior perdi el valor original lo vuelvo a crear

lista_numero = [1,2,3,4,5,6,7,8,9,10]
## acá tambien hay asignación destructiva
lista_numero += ["uno","dos","tres","cuatro"]
print(f"en la misma variable pisando el valor anterior y usando un atajo {lista_numero}")

"""#### Ejercicio 3
 Dada la lista =  [1,2,3,4,5,6,7,8,9,10]
- Duplicar el contenido de la lista con el operador * e imprimirlo (no modificar la lista original) 
- Acceder a la posicion 0 de la lista e imprimir su contenido
- Acceder a la ultima posicion de la lista por medio de len(lista) -1 e imprimir su contenido
- A la lista lista del ejercicio 1 (la de 10 numeros) por medio de la funcion reverse invertir los elementos
- Quitar e imprimir el ultimo elemento de la lista, imprimir ademas la lista con un elemento menos 
"""



## Solución 
## setup
lista = [1,2,3,4,5,6,7,8,9,10]
#1
print(lista * 2)

#2
print(lista[0])

#3
print(len(lista)-1)

#4
lista.reverse()
print(lista)

#5
lista.pop()
print(lista)





"""#### Ejercicio 4
Con la funcion append() agregar el elemento 1 previamente borrado con la funcion pop() a la lista anterior e imprimir la lista.

"""







## Solución 
lista.append(1)
print(lista)

"""#### Ejercicio 5
Dada la siguiente lista = [1,2,3,4,5,6,7,8,9]
- Por medio del la función pop(indice) quitar el elemento cuyo valor es 3 de la lista e imprimir la lista resultante.
- Ahora y de una mejor forma quitar el elemento 6 con la funcion list.remove(element) esta funcion busca el elemento y si lo encuentra lo borra, luego imprimir el resultado.
"""







## Solución
# setup
lista = [1,2,3,4,5,6,7,8,9]

#1 
lista.pop(2)
print(lista)

#2
lista.remove(6)
print(lista)





"""#### Ejercicio 6
Con la funcion index() buscar la posicion e imprimir el elemento cuyo valor es 3.
"""







## Solución

#setup 
## Aca en el ejercicio previo borre el elemento 3 y ademas no seria conveniente 
## que haya relacion entre ejercicios, vuelvo a crear la lista
## ahora con el generador range y con el constructor de listas list()
lista = list(range(10))
posicion_del_tres = lista.index(3)
print(lista)
print(posicion_del_tres)



"""#### Ejercicio 7
- con la funcion index(...) buscar e imprimir un elemento no presente en la lista
"""







## Solución
## aca la idea es que falle, mostrando un valueError al 
## buscar un valor inexistente

#setup 
lista = list(range(10))
lista.index(11)

"""#### Ejercicio 8
- Reemplazar el contenido de la ubicacion 5 de la lista con el valor 25 e imprimir la lista.

hint: lista[posicion] = nuevoValor
"""







## Solución
## aca la idea es asignar pero a una posicion en particular y no a la variable
## en gral

#setup 
lista = list(range(10))

lista[5] = 25
lista





"""#### Ejercicio 9
- Por medio de la función insert() agregar en el tercer lugar de la lista el valor 1000.
"""









## Solución

#setup 
lista = list(range(10))

lista.insert(3,1000)
lista

"""#### Ejercicio 10

- Contar la cantidad de veces que aparece un elemento en una lista
- Dada la lista = [2,3,4,5,2,3,3,2]  por medio de la funcion count() contar e imprimir la cantidad de veces que aparece repetido el numero 2
"""







## Solución

#setup 
lista = list(range(10))
lista.append(2)
lista.append(3)
#1
# se por haberlo definido de tal modo que deberian haber 2 veces el nro 3
print(f"Cantidad de veces que aparece el nro 3: {lista.count(3)}")

#2
#setup
lista = [2,3,4,5,2,3,3,2]
print(f"Cantitdad de veces que aparece el nro 2: {lista.count(2)}")





"""#### Ejercicio 11

Contar ahora la cantidad de veces que aparece un elemento tupla en una lista lista = ['a', ('a', 'b'), ('a', 'b'), [3, 4]]

- Contar la cantidad de veces que aparece la tupla ('a', 'b') e imprimir dicho valor 
"""





## Solución
#setup
lista = ['a', ('a', 'b'), ('a', 'b'), [3, 4]]
lista.count(('a','b'))

"""#### Ejercicio 12
Dada una lista desordenada de vocales =   ['e', 'a', 'u', 'o', 'i']
 - Ordenarla con la función sort() en modo ascendente
 - Ordenarla con la función sort() en modo descendente sort(reverse=True)
 - Utilizar la función sorted(lista)
 - Utilizar la función sorted(lista, reverse=True)
 
 En todos los casos imprimir los resultados
"""







## Solucion

#setup
vocales = ['e', 'a', 'u', 'o', 'i']

#1 
vocales.sort()
print(f"vocales en modo ascendente {vocales}")

#2
vocales.sort(reverse= True)
print(f"vocales en modo descendente {vocales}")

#3
sorted(vocales)
print(f"vocales usando sorted {vocales}")

#4
sorted(vocales, reverse=True)
print(f"vocales usando sorted y reverse en True {vocales}")







"""Ejercicio 13

Crear una lista de valores y dicha lista copiarla asignando a una nueva variable, sobre la primera lista remover un valor, e imprimir la segunda lista "copiada", comprobar que el valor removido de la primera lista tambien fué removido de la segunda.
"""







## Solucion

#Setup
lista = [1,2,3,4]
lista_2 = lista

lista.remove(1)
print(lista)
print(lista_2)

"""#### Ejercicio 14

Dada la lista del ejemplo anterior utilizar la función list.copy() asignar el valor a la lista2 y comprobar que en este caso si borro un elemento de la lista1, no se borra de la lista 2.
"""







## Solucion

#Setup
lista = [1,2,3,4]
lista_2 = lista.copy()

lista.remove(1)
print(lista)
print(lista_2)

