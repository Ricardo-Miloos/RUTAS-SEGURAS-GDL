import folium
import osmnx as ox

def mostrar_ruta_en_mapa(grafo, ruta, nombre_archivo="ruta_segura.html"):
    """
    Muestra la ruta más segura sobre un mapa interactivo y la guarda como HTML.
    :param grafo: grafo de OSMNX con datos espaciales
    :param ruta: lista de nodos que representan la ruta
    :param nombre_archivo: nombre del archivo HTML generado
    """
    # Obtener coordenadas de los nodos de la ruta
    puntos = [(grafo.nodes[n]['y'], grafo.nodes[n]['x']) for n in ruta]
    centro_lat = sum(p[0] for p in puntos) / len(puntos)
    centro_lon = sum(p[1] for p in puntos) / len(puntos)

    # Crear mapa base
    mapa = folium.Map(location=(centro_lat, centro_lon), zoom_start=15)

    # Dibujar ruta
    folium.PolyLine(puntos, color="blue", weight=5, opacity=0.7).add_to(mapa)

    # Marcar inicio y fin
    folium.Marker(puntos[0], popup="Inicio", icon=folium.Icon(color="green")).add_to(mapa)
    folium.Marker(puntos[-1], popup="Destino", icon=folium.Icon(color="red")).add_to(mapa)

    # Guardar como HTML
    mapa.save(nombre_archivo)
    print(f"\n📍 Mapa generado: {nombre_archivo} (puedes abrirlo en tu navegador)")
