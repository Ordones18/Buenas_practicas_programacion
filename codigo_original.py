import time

def es_primo(n):
    """Verifica si un número es primo"""
    if n < 2:
        return False
    
    # Verificar todos los números desde 2 hasta n-1
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

def encontrar_primos(limite):
    """Encuentra primos hasta el límite dado"""
    primos = []
    
    for numero in range(1, limite + 1):
        if es_primo(numero):
            primos.append(numero)
    
    return primos

# Medición de tiempo
limite = 100000
inicio = time.time()

primos = encontrar_primos(limite)

fin = time.time()
tiempo_ejecucion = fin - inicio

print(f"SALIDA CÓDIGO ORIGINAL:")
print(f"Primos encontrados: {len(primos)}")
print(f"Tiempo ejecución: {tiempo_ejecucion:.2f} segundos")
print(f"Primeros 10: {primos[:10]}")