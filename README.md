# Algoritmo Genético

**Minimizar:**

<img src="https://latex.codecogs.com/gif.latex?\dpi{200}&space;\tiny&space;f(\vec{x})=(x_1-10)^2&plus;5(x_{2}-12)^2&plus;x_3^4&plus;3(x_{4}-11)^2&plus;10x_{5}^{6}&plus;7x_{6}^2&plus;x_{7}^4-4x_{6}x_{7}-10x_{6}-8x_7" title="\tiny f(\vec{x})=(x_1-10)^2+5(x_{2}-12)^2+x_3^4+3(x_{4}-11)^2+10x_{5}^{6}+7x_{6}^2+x_{7}^4-4x_{6}x_{7}-10x_{6}-8x_7" />

Sujeta a:

- <img src="https://latex.codecogs.com/gif.latex?g1(\vec{x}):-127&plus;2x_1^2&plus;3x_2^4&plus;x_3&plus;4x_4^2&plus;5x_5\leq0" title="g1(\vec{x}):-127+2x_1^2+3x_2^4+x_3+4x_4^2+5x_5\leq0" />

- <img src="https://latex.codecogs.com/gif.latex?g2(\vec{x}):-282&plus;7x_1&plus;3x_2&plus;10x_3^2&plus;x_4-x_5\leq&space;0" title="g2(\vec{x}):-282+7x_1+3x_2+10x_3^2+x_4-x_5\leq0" />

- <img src="https://latex.codecogs.com/gif.latex?g3(\vec{x}):-196&plus;23x_1&plus;x_2^2&plus;6x_6^2-8x_7\leq&space;0" title="g3(\vec{x}):-196+23x_1+x_2^2+6x_6^2-8x_7\leq0" />

- <img src="https://latex.codecogs.com/gif.latex?g4(\vec{x}):4x_1^2&plus;x_2^2-3x_1x_2&plus;2x_3^2&plus;5x_6-11x_7\leq0" title="g4(\vec{x}):4x_1^2+x_2^2-3x_1x_2+2x_3^2+5x_6-11x_7\leq0" />

Donde <img src="https://latex.codecogs.com/gif.latex?-10\leq{x_i}\leq10,(i&space;=&space;1,&space;...,&space;7)" title="-10\leq{x_i}\leq10,(i = 1, ..., 7)" />.

## Características del Algoritmo

- 30 ejecuciones independientes.
- Tamaño de población = 200.
- Número de evaluaciones máximas: 220,000.
- **Reportar:** Mejor, mediana, peor, desviación estándar, de los mejores y gráfica de convergencia del mejor, peor y mediana.

## Análisis de Resultados

El documento interactivo con los resultados se encuentra hosteado en: https://manolomon.github.io/algoritmo-genetico/
