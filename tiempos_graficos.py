import matplotlib.pyplot as plt
import subprocess
import time

def medir_tiempo_ejecucion(archivo):
    """Mide el tiempo de ejecución de un script Python"""
    inicio = time.time()
    resultado = subprocess.run(['python', archivo], capture_output=True, text=True)
    fin = time.time()
    return fin - inicio, resultado.stdout

# Medir ambos códigos
tiempo_original, salida_original = medir_tiempo_ejecucion('codigo_original.py')
tiempo_optimizado, salida_optimizado = medir_tiempo_ejecucion('codigo_optimizado.py')

# Mostrar resultados en consola
print(f"\n{'='*50}")
print("RESULTADOS COMPARATIVOS")
print(f"{'='*50}")
print(f"Código original: {tiempo_original:.2f} segundos")
print(f"Código optimizado: {tiempo_optimizado:.4f} segundos")
print(f"Mejora: {tiempo_original/tiempo_optimizado:.1f}x más rápido")
print(f"Reducción: {((tiempo_original - tiempo_optimizado)/tiempo_original)*100:.1f}%")

# Crear gráficos comparativos
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))

# Gráfico de barras comparativo
nombres = ['Original', 'Optimizado']
tiempos = [tiempo_original, tiempo_optimizado]
colores = ["#FD0000", "#019414"]

barras = ax1.bar(nombres, tiempos, color=colores, alpha=0.8, edgecolor='black')
ax1.set_ylabel('Tiempo (segundos)')
ax1.set_title('Comparación de Tiempos de Ejecución')
ax1.grid(axis='y', alpha=0.3)

# Añadir valores en las barras
for barra in barras:
    height = barra.get_height()
    ax1.text(barra.get_x() + barra.get_width()/2., height + 0.1,
             f'{height:.2f}s', ha='center', va='bottom', fontweight='bold')

# Gráfico de mejora porcentual
mejora = ((tiempo_original - tiempo_optimizado) / tiempo_original) * 100
etiquetas_pie = ['Tiempo ahorrado', 'Tiempo restante']
valores_pie = [mejora, 100 - mejora]
colores_pie = ["#00740F", "#E90707"]

ax2.pie(valores_pie, labels=etiquetas_pie, autopct='%1.1f%%', 
        colors=colores_pie, startangle=90, explode=(0.1, 0))
ax2.set_title(f'Mejora del Rendimiento\n{mejora:.1f}% más rápido')

plt.tight_layout()
plt.savefig('comparativa_optimizacion.png', dpi=300, bbox_inches='tight')
plt.show()

# Mostrar salida de los programas
print("\nSALIDA CÓDIGO ORIGINAL:")
print(salida_original)
print("\nSALIDA CÓDIGO OPTIMIZADO:")
print(salida_optimizado)