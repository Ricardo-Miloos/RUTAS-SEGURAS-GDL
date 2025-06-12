
# Análisis Exploratorio: Riesgo Delictivo en ZMG

Aquí muestro como se visualiza y explora los datos de criminalidad antes de integrarlos al sistema.

## Cargar datos

```python
import pandas as pd

df = pd.read_excel("../data/2025.xlsx")
df.head()
```

## Filtrar por municipios de la ZMG

```python
municipios_zmg = [
    "GUADALAJARA", "ZAPOPAN", "SAN PEDRO TLAQUEPAQUE",
    "TONALÁ", "EL SALTO", "TLALPAN", "TLAJOMULCO DE ZÚÑIGA"
]
df_zmg = df[df["Municipio"].str.upper().isin(municipios_zmg)]
df_zmg["Municipio"].value_counts()
```

## Visualizar número de delitos por municipio

```python
import matplotlib.pyplot as plt

conteo = df_zmg["Municipio"].value_counts()
conteo.plot(kind="bar", title="Delitos por municipio en la ZMG")
plt.ylabel("Número de registros")
plt.show()
```
