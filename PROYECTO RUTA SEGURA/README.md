
#  Rutas Seguras para Peatones en la Zona Metropolitana de Guadalajara

Este proyecto consiste en un sistema de GPS que permite encontrar rutas seguras para peatones en la Zona Metropolitana de Guadalajara (ZMG), priorizando zonas con menor índice de criminalidad por encima de la distancia más corta.

Combina grafos geográficos con datos reales de criminalidad (2025), integrando visualización de rutas y comparativas entre la ruta más corta y la más segura.

---

##  Justificación

Las aplicaciones de navegación tradicionales priorizan distancia o tiempo, sin considerar el riesgo para peatones. En zonas con alta incidencia delictiva, esto representa un problema grave de seguridad.

Este proyecto busca brindar una alternativa más segura, especialmente útil para personas que caminan mucho por la ciudad.

---

##  Tecnologías utilizadas

- Python 3.11
- NetworkX (estructuras de grafo)
- OSMnx (grafo real de calles desde OpenStreetMap)
- Folium (visualización de rutas en mapas)
- Pandas (procesamiento de datos delictivos)
- Scikit-learn (búsqueda de nodos cercanos)

---

##  Estructura del proyecto

```
ruta_segura/
├── data/                    # Datos crudos y procesados (CSV, XLSX)
├── docs/                    # Documentación técnica (diagramas, referencias)
├── notebooks/               # Análisis exploratorios
├── src/
│   ├── api/                 # Carga de datos, visualización y mapas
│   ├── algoritmo/           # Lógica de rutas seguras
│   ├── grafo/               # Construcción del grafo base
│   └── main_comparativo.py  # Script principal con comparación de rutas
```

---

##  Cómo ejecutar el proyecto

1. Descarga el ZIP.
2. Instala las dependencias con:

```bash
pip install -r requirements.txt
```

3. Ejecuta el script principal desde la terminal:

```bash
python src/main_comparativo.py
```
nota: habrá 3 mains en el proyecto, main_comparativo muestra la ruta mas segura vs la ruta mas corta, main_interactivo muestra solamente la ruta mas segura, y el main es una versión mas cruda del proyecto, que no permite al usuario introducir coordenadas (es la primera versión). 

4. Ingresa las coordenadas de inicio y destino cuando se te pidan. Puedes copiarlas de google maps o cualquier mapa web con coordenadas.
5. Se generará un archivo `rutas_comparadas.html` o `rutas_seguras` (dependiendo de cual main hayas ejecutado) para visualizar el mapa. Este archivo lo encontrarás en la carpeta del proyecto, en la ruta donde hayas descomprimido el .zip

NOTA: Cuando el mapa del grafo aparezca en pantalla, se debe cerrar la ventana emergente del mismo para que siga corriendo la consola.
---

##  Fuentes de datos

- Delitos registrados en Jalisco 2025: datos oficiales (INEGI / IIEG)
- OpenStreetMap: para grafo de calles caminables en la ZMG

---

##  Características implementadas

- Construcción de grafo real peatonal en Guadalajara
- Asignación de riesgos por municipio con datos reales
- Algoritmo de ruta más segura (Dijkstra modificado)
- Comparación visual con la ruta más corta (por distancia)
- Mapa interactivo HTML generado con Folium
- Elección personalizada de puntos de inicio y destino

---

##  Posibles mejoras futuras

-  Usar datos delictivos por colonia o cuadrante
-  Heatmaps dinámicos de zonas peligrosas
-  Interfaz web 
-  Versión móvil
-  Escoger la calle directamente en el mapa en lugar de introducir manualmente las      coordenadas
---

##  Autor

- Ricardo Yahir Ochoa Hernández

## Profesora

- Ximena Aquino Pérez