# vuelos con búsqueda en amplitud

from arbol import Nodo

def buscar_solucion_BFS(conexiones, estado_inicial, solucion):
    solucionado = False
    nodos_visitados = []
    nodos_frontera = []
    
    nodoInicial = Nodo(estado_inicial)
    nodos_frontera.append(nodoInicial)

    while (not solucionado) and len(nodos_frontera) != 0:
        nodo = nodos_frontera.pop(0)
        nodos_visitados.append(nodo)

        if nodo.get_datos() == solucion:
            return nodo
        else:
            dato_nodo = nodo.get_datos()
            lista_hijos = []

            for un_hijo in conexiones.get(dato_nodo, []):
                hijo = Nodo(un_hijo)
                hijo.set_padre(nodo)  # 🔥 IMPORTANTE
                lista_hijos.append(hijo)

                if not hijo.en_lista(nodos_visitados) and not hijo.en_lista(nodos_frontera):
                    nodos_frontera.append(hijo)

            nodo.set_hijos(lista_hijos)

    return None


if __name__ == "__main__":
    conexiones = {
        'Jiloyork': {'Celaya', 'CDMX', 'Queretaro'},
        'Sonora': {'Zacatecas', 'Sinaloa'},
        'Guanajuato': {'Aguascalientes'},
        'Oaxaca': {'Queretaro'},
        'Sinaloa': {'Celaya', 'Sonora', 'Jiloyork'},
        'Celaya': {'Jiloyork', 'Sinaloa'},
        'Zacatecas': {'Sonora', 'Monterrey', 'Queretaro'},  # corregido
        'Monterrey': {'Zacatecas', 'Sinaloa'},
        'Tamaulipas': {'Queretaro'},
        'Queretaro': {'Tamaulipas', 'Zacatecas', 'Sinaloa', 'Jiloyork', 'Oaxaca'}
    }

    estado_inicial = 'Jiloyork'
    solucion = 'Zacatecas'

    nodo_solucion = buscar_solucion_BFS(conexiones, estado_inicial, solucion)

    # mostrar resultado
    resultado = []
    nodo = nodo_solucion

    while nodo.get_padre() is not None:
        resultado.append(nodo.get_datos())
        nodo = nodo.get_padre()

    resultado.append(estado_inicial)
    resultado.reverse()

    print(resultado)