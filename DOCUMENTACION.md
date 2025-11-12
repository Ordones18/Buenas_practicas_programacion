# Informe de Actividad: Herramientas y Metodologías en Ciencia de Datos
## Introducción

Este proyecto compara dos implementaciones para buscar números primos en el rango 1 a 100000:

- **`codigo_original.py`**: Implementación básica que verifica divisibilidad probando todos los enteros desde 2 hasta n-1.
- **`codigo_optimizado.py`**: Versión optimizada que reduce el trabajo comprobando hasta la raíz cuadrada de n, evita pares y usa list comprehensions, además devuelve los primos como un array de NumPy.

### Problemas identificados en la versión original:
- Recomprobaciones innecesarias: la función `es_primo` prueba divisores hasta n-1 en lugar de hasta √n.
- Iteración por todos los números incluyendo pares, lo que duplica el trabajo innecesariamente.
- Uso de listas y `append` dentro del bucle que provoca muchas operaciones de Python a nivel interpretado.

El objetivo de la optimización fue reducir el tiempo de ejecución manteniendo la exactitud de los resultados.

![Rama de trabajo optimización-codigo](imagenes/figura1.jpg)

---

## Optimización

### Técnicas aplicadas

1. **Límite del bucle a la raíz cuadrada de n**: En `es_primo_optimizado` se usa `math.isqrt(n)` para limitar la comprobación de divisores hasta √n, reduciendo la complejidad por verificación.

2. **Saltar pares**: Se detecta y descarta el caso par (excepto el 2), iterando solo por impares a partir de 3.

3. **List comprehensions**: En `encontrar_primos_optimizado` se crea la lista de primos impares con una list comprehension, lo cual reduce el gasto computacional de Python frente a `append`.

4. **Uso de NumPy**: La salida final se convierte en `np.array` para demostrar cómo integrarlo y para acelerar posibles operaciones vectorizadas posteriores.

5. **Microperfilado con cProfile**: Se usó `python -m cProfile` para localizar las funciones más costosas y guiar las optimizaciones.

Se implementaron diversas técnicas de optimización que permitieron mejorar significativamente el rendimiento del código. Se logró reducir la cantidad de comprobaciones necesarias al verificar únicamente hasta la raíz cuadrada de cada número, y se excluyeron los números pares excepto el 2, lo que agilizó considerablemente el proceso. Además, se utilizaron list comprehensions para crear listas de forma más eficiente, evitando el uso repetitivo de `append` que ralentizaba la ejecución.

---

## Resultados

### Código Original

![Resultados código original](imagenes/figura2.jpg)

En las mediciones del código original se obtuvo la siguiente evidencia:
- Se encontraron **9592 números primos** en el rango 1 a 100000.
- Tiempo total de ejecución: **45.44 segundos**.
- Perfil con cProfile: **109603 llamadas**, tiempo acumulado: **44.989 segundos**.

La función `es_primo` consumió la mayor parte del tiempo de ejecución:
- Llamada **100,000 veces**.
- Tiempo acumulado: **42.62 segundos** de CPU.

Esto indica que prácticamente todo el coste de la ejecución se consumía verificando divisores con un algoritmo que probaba hasta n-1.

![Resultados de Profiling_original](imagenes/figura3.jpg)

Esta información permite concluir que la estrategia de verificación de primalidad del código original es extremadamente ineficiente para el dominio evaluado. El alto número de llamadas y el gran `tottime` asociado a `es_primo` muestran que la complejidad por número convierte el proceso en algo impracticable para límites grandes.

### Código Optimizado

![Resultados código optimizado](imagenes/figura4.jpg)

**Salida del código optimizado:**

En la versión optimizada:
- Se mantienen los mismos resultados: **9592 primos** hasta 100000.
- Tiempo de ejecución: **0.1120 segundos**.
- Perfil de cProfile: **211579 llamadas**, tiempo total: **0.890 segundos**.

La función `es_primo_optimizado`:
- Llamada **49,999 veces**.
- Coste acumulado: **0.158 segundos**.

Esto refleja que cada verificación es mucho más económica gracias a limitar las comprobaciones hasta la raíz cuadrada de n y evitar pares.

![Resultados Profiling_optimizado](imagenes/figura5.jpg)

El perfil muestra también tiempo extra por cargar e inicializar NumPy y por llamadas internas, por eso el número total de llamadas puede subir, aunque el tiempo principal baje mucho. La mayor mejora viene de cambiar el algoritmo: verificar solo hasta √n, no probar pares y usar list comprehensions.

### Comparación de tiempos

![Resultados comparativos original vs optimizado](imagenes/figura6.jpg)

**Resultados comparativos:**
- Código original: **45.47 segundos**
- Código optimizado: **0.2804 segundos**
- Mejora: **162.2x más rápido**
- Reducción: **99.4%**

**Salida comparada:**


La comparación muestra una mejora drástica: el código original tarda aproximadamente 45.7 segundos mientras que la versión optimizada registra tiempos alrededor de 0.28 segundos, es decir, una aceleración del orden de 150x–260x según la medición usada. Ambos scripts devuelven los mismos 9592 primos, por lo que la optimización no altera la corrección. Esta ganancia proviene sobre todo de cambios algorítmicos; la sobrecarga de librerías como NumPy es pequeña frente al ahorro obtenido.

![Gráficas de comparación de los tiempos](imagenes/figura7.jpg)

La gráfica muestra los tiempos de ejecución del código original frente al código optimizado para buscar primos hasta 100000. La barra roja representa el tiempo del código original y la verde el tiempo optimizado. Como se ve, la versión optimizada reduce drásticamente el tiempo de ejecución. Esto se debe principalmente a cambiar el algoritmo de verificación y a usar un código más eficiente en Python.

---

## Conclusiones

- La optimización aplicada mostró beneficios claros: el tiempo de ejecución se redujo drásticamente mientras se mantuvo la salida correcta (mismo número de primos y mismos primeros valores). Esto hace que el programa sea mucho más práctico para límites grandes y demuestra que mejorar el algoritmo (comprobar hasta √n y evitar pares) es mucho más efectivo que microajustes o cambios menores. Además, el uso de list comprehensions y la conversión a un array de NumPy facilitan el manejo de los resultados y pueden acelerar operaciones posteriores si se necesitaran.

- Para trabajos futuros se recomienda añadir pruebas automáticas que confirmen la equivalencia funcional entre versiones y benchmarks que calculen la media y desviación de varias ejecuciones para obtener medidas más robustas.