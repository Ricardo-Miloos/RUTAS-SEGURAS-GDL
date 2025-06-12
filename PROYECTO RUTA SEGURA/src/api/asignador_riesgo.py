
import osmnx as ox
from shapely.geometry import Point

# Coordenadas centrales de municipios de la ZMG
municipios_centros = {
    "Guadalajara": ox.geocode("Guadalajara, Jalisco, Mexico"),
    "Zapopan": ox.geocode("Zapopan, Jalisco, Mexico"),
    "Tlajomulco de Zúñiga": ox.geocode("Tlajomulco de Zúñiga, Jalisco, Mexico"),
    "Tonalá": ox.geocode("Tonalá, Jalisco, Mexico"),
    "El Salto": ox.geocode("El Salto, Jalisco, Mexico"),
    "Ixtlahuacán de los Membrillos": ox.geocode("Ixtlahuacán de los Membrillos, Jalisco, Mexico"),
    "Juanacatlán": ox.geocode("Juanacatlán, Jalisco, Mexico")
}

# Mapa de riesgos normalizados basado en datos reales de criminalidad 2025
riesgo_normalizado = {
    "Guadalajara": 1.0,
    "Zapopan": 0.6588,
    "Tlajomulco de Zúñiga": 0.4057,
    "Tonalá": 0.2441,
    "El Salto": 0.1393,
    "Ixtlahuacán de los Membrillos": 0.0124,
    "Juanacatlán": 0.0
}

def asignar_riesgo_municipal_simple(grafo):
    for u, v, datos in grafo.edges(data=True):
        try:
            x1, y1 = grafo.nodes[u]["x"], grafo.nodes[u]["y"]
            x2, y2 = grafo.nodes[v]["x"], grafo.nodes[v]["y"]
            punto_medio = Point((x1 + x2) / 2, (y1 + y2) / 2)
        except KeyError:
            continue

        municipio_cercano = min(
            municipios_centros.items(),
            key=lambda item: punto_medio.distance(Point(item[1][1], item[1][0]))
        )[0]

        riesgo = riesgo_normalizado.get(municipio_cercano, 0.0)
        distancia = datos.get("length", 1)
        datos["riesgo"] = riesgo
        datos["peso"] = distancia * (1 + riesgo)
