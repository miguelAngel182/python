#Código no hecho por mi
from collections import Counter
import re

def mostrar_frecuencia_palabras(texto, top_n=10):
    palabras = re.findall(r'\b\w+\b', texto.lower())
    contador = Counter(palabras)
    for palabra, frecuencia in contador.most_common(top_n):
        print(f"{palabra}: {frecuencia}")

if __name__ == "__main__":
    texto = input("Introduce el texto a analizar:\n")
    mostrar_frecuencia_palabras(texto)