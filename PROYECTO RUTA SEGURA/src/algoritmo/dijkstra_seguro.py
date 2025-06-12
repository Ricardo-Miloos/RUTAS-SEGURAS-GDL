import networkx as nx

def ruta_mas_segura(grafo, origen, destino):
    """
    Encuentra la ruta más segura entre dos nodos usando Dijkstra,
    minimizando el 'peso' que incluye riesgo.
    
    :param grafo: Objeto networkx.Graph con pesos personalizados
    :param origen: Nodo de inicio
    :param destino: Nodo de fin
    :return: Lista de nodos de la ruta más segura y el costo total
    """
    try:
        ruta = nx.dijkstra_path(grafo, origen, destino, weight='peso')
        costo_total = nx.dijkstra_path_length(grafo, origen, destino, weight='peso')
        return ruta, costo_total
    except nx.NetworkXNoPath:
        return None, float("inf")
