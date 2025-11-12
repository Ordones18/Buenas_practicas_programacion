import time
import math
import numpy as np

def es_primo_optimizado(n):
    """Verifica si es primo con optimizaciones"""
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    
    # Solo verificar hasta √n y solo números impares
    limite_superior = math.isqrt(n)
    for i in range(3, limite_superior + 1, 2):
        if n % i == 0:
            return False
    return True

def encontrar_primos_optimizado(limite):
    """Encuentra primos usando técnicas optimizadas"""
    # Iniciar con el 2 y agregar primos impares con list comprehension
    primos = [2] + [num for num in range(3, limite + 1, 2) 
                    if es_primo_optimizado(num)]
    
    return np.array(primos)

# Medición de tiempo
limite = 100000
inicio = time.time()

primos = encontrar_primos_optimizado(limite)

fin = time.time()
tiempo_ejecucion = fin - inicio

print(f"SALIDA CÓDIGO OPTIMIZADO:")
print(f"Primos encontrados: {len(primos)}")
print(f"Tiempo ejecución: {tiempo_ejecucion:.4f} segundos")
print(f"Primeros 10: {primos[:10]}")
