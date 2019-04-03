# Algoritmo Genético

**Minimizar:**
$$f(\vec{x})=(x_{1} − 10)^2 + 5(x_{2} − 12)^{2} + x_{3}^{4} + 3(x_{4} − 11)^2 +
10x_{5}^{6} + 7x_{6}^2 + x_{7}^{4} − 4x_{6}x_{7} − 10x_{6} − 8x_{7}$$

Sujeta a:

- $g1(\vec{x}) : −127 + 2x_{1}^{2} + 3x_{2}^{4} + x_{3} + 4x_{4}^{2} + 5x_{5} ≤ 0$

- $g2(\vec{x}) : −282 + 7x_{1} + 3x_{2} + 10x_{3}^{2} + x_{4} − x_{5} ≤ 0$

- $g3(\vec{x}) : −196 + 23x_{1} + x_{2}^{2} + 6x_{6}^{2} − 8x_{7} ≤ 0$

- $g4(\vec{x}) : 4x_{1}^{2} + x_{2}^{2} − 3x_{1}x_{2} + 2x_{3}^2 + 5x_{6} − 11x_{7} ≤ 0$

Donde $−10 ≤ x_{i} ≤ 10(i = 1, ..., 7)$.

## Características del Algoritmo

- 30 ejecuciones independientes.
- Tamaño de población = 200.
- Número de evaluaciones máximas: 220,000.
- **Reportar:** Mejor, mediana, peor, desviación estándar, de los mejores y gráfica de convergencia del mejor, peor y mediana.
