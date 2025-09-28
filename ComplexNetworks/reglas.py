import numpy as np
from collections import Counter

def matrices(long, listas):                   # Recibe una lista de listas
  distancia = []
  popularidad = []
  for posicion, lista in enumerate(listas):   # Obtenemos la matriz de distancia con listas de igual longitud
    if len(lista) > long:                     # Si la lista es mayor a longitud
      lista = lista[:long]                    # Cortar la lista hasta la longitud
      listas[posicion] = lista                # Reemplazar la lista recortada
  lista = [i for num in listas for i in num]  # Convertir la lista de listas en una sola lista.
  conteo = Counter(lista)                     # Diccionario con el conteo de cada nodo en la lista.
  conteo[0] = 0                               # Agrega al diccionario la clave cero con valor cero
  for lista in listas:                        # Llenar la lista de distancia con listas de igual longitud
    if len(lista) == long:                    # Si la lista es igual a la longitud
      distancia.append(lista)                 # Agregar la lista directamente
    if len(lista) < long:                     # Si la lista es menor que longitud
      while len(lista) < long:
        lista.append(0)                       # Rellenar de ceros la lista
      distancia.append(lista)
    reordenar_lista = sorted(lista, key=lambda x: conteo.get(x,0), reverse=True) # Ordena en función de la frecuencia, de mayor a menor
    popularidad.append(reordenar_lista)       # Reordenamos para obtener la matriz de popularidad
  return popularidad, distancia

def frecuencia(matriz, vector):
  filas = len(matriz)                                           # Número de filas
  columnas = len(matriz[0])                                     # Número de columnas
  suma_seleccionados = 0                                        # Suma de nodos seleccionados
  indices_seleccionados = [i for i in range(columnas) if vector[i]!=0]  # Lista de indices seleccionados del vector
  long = len(indices_seleccionados)                             # Total de columnas seleccionadas
  seleccion = [[0 for i in range(long)] for i in range(filas)]  # Matriz de ceros para las columnas seleccionadas
  frecuencia = {}                                               # Diccionarios de frecuencias de cada nodo
  for i in range(filas):
    for posicion, indice in enumerate(indices_seleccionados):
      nodo = vector[indice]*matriz[i][indice]
      if nodo != 0:
        suma_seleccionados += 1                                 # Total de nodos seleccionados sin contar el cero
        seleccion[i][posicion] = nodo                           # Guarda los nodos seleccionados
        if nodo in frecuencia:                                  # Si ya se encuentra el nodo en el diccionario,
          frecuencia[nodo] += 1                                 # entonces suma un uno
        else:
          frecuencia[nodo] = 1                                  # Si no, colocar un uno
  if 0 in frecuencia:
    del frecuencia[0]
  return frecuencia

def nodos_seleccionados(popularidad, distancia, vector_popularidad, vector_distancia, alfa):
 frecuencias_popularidad = frecuencia(popularidad, vector_popularidad)
 frecuencias_distancia = frecuencia(distancia, vector_distancia)
 claves = set(frecuencias_popularidad.keys()) | set(frecuencias_distancia.keys())
 f_n = {}
 for nodo in claves:
    frecuencia_popularidad = frecuencias_popularidad.get(nodo, 0)
    frecuencia_distancia = frecuencias_distancia.get(nodo, 0)
    f_n[nodo] = alfa*frecuencia_popularidad + (1-alfa)*frecuencia_distancia # Modelo representativo de las reglas
 return f_n
