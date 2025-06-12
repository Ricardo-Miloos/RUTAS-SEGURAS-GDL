
import osmnx as ox
import random

def descargar_grafo_guadalajara():
    """
    Descarga el grafo de calles peatonales de la ZMG desde OpenStreetMap.
    """
    # Define el área
    lugar = "Guadalajara, Jalisco, Mexico"

    # Descargar solo caminos peatonales
    grafo = ox.graph_from_place(lugar, network_type="walk")

    return grafo

def visualizar_grafo(grafo):
    """
    Muestra el grafo con matplotlib.
    """
    ox.plot_graph(grafo, node_size=5, edge_color="gray")
    
# Este asignador de riesgos es un ejemplo y no refleja datos reales, lo utilice para verificar funcionalidad en versiones pasadas.
def asignar_riesgos_a_grafo(grafo):
    """
    Asigna un nivel de riesgo aleatorio (entre 0 y 1) a cada calle del grafo.
    También actualiza el atributo 'peso' usado por el algoritmo de rutas seguras.
    """
    for u, v, datos in grafo.edges(data=True):
        distancia = datos.get('length', 1)  # usa 1 si no hay longitud
        riesgo = random.uniform(0.0, 1.0)   # riesgo aleatorio entre 0 (seguro) y 1 (peligroso)
        peso = distancia * (1 + riesgo)

        datos['riesgo'] = riesgo
        datos['peso'] = peso

