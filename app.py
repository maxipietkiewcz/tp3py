import pandas as pd
import random

#Funcion que como parametro recibe la cantidad de numeros aleatorios, el minimo y el maximo
def generar_numeros_aleatorios(cantidad, minimo, maximo): 
    
    numeros_aleatorios = [random.randint(minimo, maximo) for _ in range(cantidad)] 
    return numeros_aleatorios

numeros_aleatorios = generar_numeros_aleatorios(38, 18, 30) # {1,2,3}
                                                            #["a", "b", "c"] 
                                                            # []

def analisis_estadistico(numeros_aleatorios): #Funcion de analisis estadistico que como parametro recibe una lista de numeros aleatorios en este caso
    if len(numeros_aleatorios) == 0: #Si la lista de numeros aleatorios esta vacia
        print("La lista de numeros aleatorios esta vacia")
    elif any(not isinstance(num, (int, float)) for num in numeros_aleatorios): #Si la lista contiene elementos no numericos
        print("La lista contiene elementos no numéricos")
    elif not isinstance(numeros_aleatorios, list): #Si la lista no es de tipo lista
        print("El parámetro ingresado no es una lista")
    else:

        df = pd.DataFrame(numeros_aleatorios, columns=["Edades"]) #Se crea un dataframe con la lista de numeros aleatorios

        #Agrupa los datos por la columna "Edades" y calcula el tamaño de cada grupo,
        #luego reinicia el índice del DataFrame resultante y le asigna el nombre "fi" a la columna "fi".
        df = df.groupby("Edades").size().reset_index(name="fi") 

        df["Fi"] = df["fi"].cumsum() #Se calcula la suma acumulada de la columna "fi"
        df["fr"] = df["fi"] / df["fi"].sum() #Se calcula el porcentaje de cada grupo
        df["Fr"] = df["fr"].cumsum() #Se calcula la suma acumulada de la columna "fr"
        df["pi%"] = df["fr"] * 100 #Se calcula el porcentaje de cada grupo
        df["Pi%"] = df["pi%"].cumsum() #Se calcula la suma acumulada de la columna "pi%"

        print(df) #Se imprime el dataframe

analisis_estadistico(numeros_aleatorios) #Se llama a la funcion
