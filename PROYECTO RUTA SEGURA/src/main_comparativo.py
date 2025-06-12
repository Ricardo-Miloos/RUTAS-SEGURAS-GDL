
from api.callejero_real import (
    descargar_grafo_guadalajara,
    visualizar_grafo,
)
from algoritmo.dijkstra_seguro import ruta_mas_segura
from api.visualizador_comparativo import mostrar_rutas_comparadas
from api.asignador_riesgo import asignar_riesgo_municipal_simple
import osmnx as ox
from networkx import shortest_path, shortest_path_length


def main():
    print("\nDescargando grafo real de Guadalajara...")
    grafo_real = descargar_grafo_guadalajara()
    print("¡Grafo descargado!")

    print("Asignando riesgos reales por municipio...")
    asignar_riesgo_municipal_simple(grafo_real)

    print("Mostrando grafo...")
    visualizar_grafo(grafo_real)

    try:
        print("\nIngresa las coordenadas del punto de inicio:")
        lat_origen = float(input("Latitud: "))
        lon_origen = float(input("Longitud: "))
        print("\nIngresa las coordenadas del punto de destino:")
        lat_destino = float(input("Latitud: "))
        lon_destino = float(input("Longitud: "))

        origen = ox.distance.nearest_nodes(grafo_real, X=lon_origen, Y=lat_origen)
        destino = ox.distance.nearest_nodes(grafo_real, X=lon_destino, Y=lat_destino)

    except Exception as e:
        print(f"Error al procesar coordenadas: {e}")
        return

    print(f"\nCalculando ruta más segura entre {origen} y {destino}...")
    ruta_segura, costo_seguro = ruta_mas_segura(grafo_real, origen, destino)

    print("Calculando ruta más corta (sin considerar riesgo)...")
    ruta_corta = shortest_path(grafo_real, origen, destino, weight="length")
    costo_corto = shortest_path_length(grafo_real, origen, destino, weight="length")

    if ruta_segura:
        print("\n✅ Comparación de rutas:")
        print("Ruta más segura:")
        print(" -> ".join(map(str, ruta_segura)))
        print(f"  Costo total (seguridad): {costo_seguro:.2f}")

        print("\nRuta más corta:")
        print(" -> ".join(map(str, ruta_corta)))
        print(f"  Costo total (distancia): {costo_corto:.2f}")

        mostrar_rutas_comparadas(grafo_real, ruta_segura, ruta_corta)
    else:
        print("No se encontró ruta entre los nodos seleccionados.")


if __name__ == "__main__":
    main()
