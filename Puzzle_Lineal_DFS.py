from arbol import Nodo

def buscar_solucion_DFS(estado_inicial, solucion):
    nodos_visitados = []
    nodos_frontera = []

    nodo_inicial = Nodo(estado_inicial)
    nodos_frontera.append(nodo_inicial)

    while len(nodos_frontera) != 0:
        nodo = nodos_frontera.pop()
        nodos_visitados.append(nodo)

        if nodo.get_datos() == solucion:
            return nodo

        dato_nodo = nodo.get_datos()

        # IZQUIERDA
        hijo = [dato_nodo[1], dato_nodo[0], dato_nodo[2], dato_nodo[3]]
        hijo_izquierdo = Nodo(hijo)
        hijo_izquierdo.set_padre(nodo)

        # DERECHA
        hijo = [dato_nodo[0], dato_nodo[1], dato_nodo[3], dato_nodo[2]]
        hijo_derecha = Nodo(hijo)
        hijo_derecha.set_padre(nodo)

        # CENTRAL
        hijo = [dato_nodo[2], dato_nodo[1], dato_nodo[0], dato_nodo[3]]
        hijo_central = Nodo(hijo)
        hijo_central.set_padre(nodo)

        for hijo in [hijo_izquierdo, hijo_central, hijo_derecha]:
            if not hijo.en_lista(nodos_visitados) and not hijo.en_lista(nodos_frontera):
                nodos_frontera.append(hijo)

        nodo.set_hijos([hijo_izquierdo, hijo_central, hijo_derecha])

    return None


def obtener_camino(nodo):
    camino = []
    while nodo is not None:
        camino.append(nodo.get_datos())
        nodo = nodo.get_padre()
    return list(reversed(camino))