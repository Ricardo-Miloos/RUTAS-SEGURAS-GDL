import networkx as nx

class GrafoSeguro:
    def __init__(self):
        self.grafo = nx.Graph()

    def agregar_nodo(self, id_nodo, coordenadas):
        """
        Agrega un nodo al grafo.
        :param id_nodo: ID único del nodo (puede ser nobmre o número)
        :param coordenadas: (lat, lon) en tupla
        """
        self.grafo.add_node(id_nodo, pos=coordenadas)

    def agregar_arista(self, nodo1, nodo2, distancia, riesgo):
        """
        Agrega una arista entre dos nodos, ponderando la seguridad.
        :param nodo1: ID del primer nodo
        :param nodo2: ID del segundo nodo
        :param distancia: distancia entre los nodos (en metros)
        :param riesgo: índice de riesgo (0 = seguro, 1 = muy peligroso)
        """
        peso_seguridad = distancia * (1 + riesgo)  # penaliza rutas riesgosas
        self.grafo.add_edge(nodo1, nodo2, distancia=distancia, riesgo=riesgo, peso=peso_seguridad)

    def obtener_grafo(self):
        """
        Devuelve el grafo completo (para el algorimo).
        """
        return self.grafo
