# Proyecto: Optimización de búsqueda de números primos

Este repositorio contiene una versión original y una versión optimizada de un script para buscar números primos en el rango 1..100000. El objetivo es comparar tiempos y mostrar técnicas sencillas de optimización reducción de complejidad, uso de list comprehensions y uso de NumPy para manipular resultados.

Contenido principal

- `codigo_original.py` — implementación básica que verifica divisibilidad probando divisores desde 2 hasta n-1.
- `codigo_optimizado.py` — versión optimizada: comprueba divisores solo hasta √n, evita pares y usa list comprehensions; devuelve primos como un array de NumPy.
- `tiempos_graficos.py` — script que ejecuta ambos scripts, mide tiempos y genera una gráfica comparativa.
- `profiling_original.txt`, `profiling_optimizado.txt` — ejemplos de salidas del profiler (si se generaron).
- `DOCUMENTACION.md` — documentación del proyecto (introducción, optimización, resultados y conclusiones).


