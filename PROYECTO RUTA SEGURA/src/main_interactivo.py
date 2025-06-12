
from api.callejero_real import (
    descargar_grafo_guadalajara,
    visualizar_grafo,
)
from algoritmo.dijkstra_seguro import ruta_mas_segura
from api.visualizador import mostrar_ruta_en_mapa
from api.asignador_riesgo import asignar_riesgo_municipal_simple
import osmnx as ox


def main():
    print("\nDescargando grafo real de Guadalajara...")
    grafo_real = descargar_grafo_guadalajara()
    print("¡Grafo descargado!")

    print("Asignando riesgos reales por municipio...")
    asignar_riesgo_municipal_simple(grafo_real)

    print("Mostrando grafo...")
    visualizar_grafo(grafo_real)

    # Solicitar coordenadas al usuario
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
    ruta, costo = ruta_mas_segura(grafo_real, origen, destino)

    if ruta:
        print("Ruta más segura:")
        print(" -> ".join(map(str, ruta)))
        print(f"Costo total: {costo:.2f}")
        mostrar_ruta_en_mapa(grafo_real, ruta)
    else:
        print("No se encontró ruta entre los nodos seleccionados.")


if __name__ == "__main__":
    main()
