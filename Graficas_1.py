import numpy as np
import matplotlib.pyplot as plt


rng = np.random.default_rng(42)

# Datos de calificaciones de los estudiantes
matematicas = rng.integers(50, 100, 20)
ciencias = rng.integers(40, 95, 20)
literatura = rng.integers(60, 100, 20)

# Datos de errores para el gráfico de barras de error
errores_matematicas = rng.uniform(2, 5, 2)
errores_matematicas = [min(errores_matematicas), max(errores_matematicas)]

errores_ciencias = rng.uniform(1, 4, 2)
errores_ciencias = [min(errores_ciencias), max(errores_ciencias)]

errores_literatura = rng.uniform(3, 6, 2)
errores_literatura = [min(errores_literatura), max(errores_literatura)]

plt.scatter(matematicas, ciencias, color='blue')
plt.title('relación entre las calificaciones de Matemáticas y Ciencias .')
plt.xlabel('calificaciones de Matemáticas')
plt.ylabel('Calificaciones de ciencias')

plt.show()

#Gráfico de barras de error:
labels = ['Matemáticas', 'Ciencias', 'Literatura']
means = [np.mean(matematicas), np.mean(ciencias), np.mean(literatura)]
errors = [np.mean(errores_matematicas), np.mean(errores_ciencias), np.mean(errores_literatura)]


plt.errorbar(labels, means, yerr=errors, fmt='o', capsize=5)
plt.title('Calificaciones promedio y errores correspondientes en las tres materias')
plt.ylabel('Calificaciones promedio')
plt.show()

#Histograma:


c_matematicas = matematicas
plt.hist(c_matematicas, bins=10)
plt.title('Distribución de las Calificaciones de Matematicas')
plt.xlabel('Calificaciones de Matematicas')
plt.ylabel('Frecuencia')

plt.show()