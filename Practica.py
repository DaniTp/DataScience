import numpy as np

print(np.__version__)

arreglo = np.array([1,2,3,4,5,6,7,8,9])

print(arreglo)

print(type(arreglo))

print(arreglo*10)

#print(help(np.array))

#Dimensiones de un array
#Array 2d (matrices):

arreglo2d = np.array([[1,2,3],[4,5,6],[7,8,9]])
print("Arreglo 2d:")
print(arreglo2d)


print("\n\nArreglo 3d:")
arreglo3d = np.array([[[1,2,3],[4,5,6]],[[7,8,9],[10,11,12]],[[13,14,15],[16,17,18]]])

print(arreglo3d)

#Para saber el numero de dimensiones
print(arreglo2d.ndim)


arr6d = np.array([1,2],ndmin=6)
print(arr6d)

print(arr6d.ndim)

#Para conocer el tamaño:
print("tiene tamaño de ", arreglo2d.size)

#Para una posición:
print(arreglo[0])
print(arreglo2d[1][2])

#cuando se pone el valor -1 empieza a contar por el final
print(arreglo[-1])

print(arreglo)

#Para imprimir una parte del arreglo se usa un inicio y final arreglo[inicio:final]
print(arreglo[2:5])

#si no se le indica el inicio entonces lo toma como el primer elemento, si no se indica final es hasta el final
print(arreglo[2:])

#se le puede agregar un tercer valor que es para que avance de n en n
print(arreglo[0:9:2])

print(arreglo[::3])

#Para cortar un array de 2d
print(arreglo2d[0:2,1:2])