from api.callejero_real import (
    descargar_grafo_guadalajara,
    visualizar_grafo,
)
from algoritmo.dijkstra_seguro import ruta_mas_segura
from api.visualizador import mostrar_ruta_en_mapa
from api.asignador_riesgo import asignar_riesgo_municipal_simple


def main():
    print("\nDescargando grafo real de Guadalajara...")
    grafo_real = descargar_grafo_guadalajara()
    print("¡Grafo descargado!")

    print("Asignando riesgos reales por municipio...")
    asignar_riesgo_municipal_simple(grafo_real)

    print("Mostrando grafo...")
    visualizar_grafo(grafo_real)

    # Selección de dos nodos aleatorios (puedes cambiar por IDs específicos)
    nodos = list(grafo_real.nodes())
    origen = nodos[0]
    destino = nodos[5]

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




