
import folium

def mostrar_rutas_comparadas(grafo, ruta_segura, ruta_corta, nombre_archivo="rutas_comparadas.html"):
    '''
    Visualiza en un solo mapa dos rutas:
    - Ruta segura (azul)
    - Ruta más corta (roja)
    '''
    # Obtener el centro del mapa desde el primer punto de la ruta segura
    lat_center = grafo.nodes[ruta_segura[0]]['y']
    lon_center = grafo.nodes[ruta_segura[0]]['x']
    mapa = folium.Map(location=(lat_center, lon_center), zoom_start=15)

    # Coordenadas de ambas rutas
    coords_segura = [(grafo.nodes[n]['y'], grafo.nodes[n]['x']) for n in ruta_segura]
    coords_corta = [(grafo.nodes[n]['y'], grafo.nodes[n]['x']) for n in ruta_corta]

    # Dibujar rutas
    folium.PolyLine(coords_segura, color="blue", weight=5, opacity=0.8, tooltip="Ruta Segura").add_to(mapa)
    folium.PolyLine(coords_corta, color="red", weight=4, opacity=0.6, tooltip="Ruta Más Corta").add_to(mapa)

    # Marcadores de inicio y fin
    folium.Marker(coords_segura[0], popup="Inicio", icon=folium.Icon(color="green")).add_to(mapa)
    folium.Marker(coords_segura[-1], popup="Destino", icon=folium.Icon(color="red")).add_to(mapa)

    mapa.save(nombre_archivo)
    print(f"📍 Mapa comparativo generado: {nombre_archivo}")
