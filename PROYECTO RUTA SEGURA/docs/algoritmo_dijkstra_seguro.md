
# Algoritmo de Ruta Segura (Dijkstra Modificado)

Este algoritmo utiliza el grafo real de calles de la ZMG, donde cada arista tiene un atributo `riesgo`.

## ¿Cómo funciona?

1. Se asigna un peso a cada arista como:

   ```
   peso = distancia * (1 + riesgo)
   ```

2. Se usa `networkx.shortest_path()` con ese peso modificado para calcular la ruta más segura entre dos nodos.

3. Se compara contra la ruta más corta en términos de distancia.

## Ventajas

- Integra distancia y peligrosidad.
- Penaliza calles más peligrosas.
- Escalable para mapas más grandes o pesos más complejos.
