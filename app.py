from flask import Flask, request, jsonify, send_file
from Puzzle_Lineal_DFS import buscar_solucion_DFS, obtener_camino

app = Flask(__name__)

@app.route("/")
def home():
    return send_file("index.html")

@app.route("/resolver", methods=["POST"])
def resolver():
    data = request.json

    estado_inicial = data["inicio"]
    solucion = data["objetivo"]

    nodo = buscar_solucion_DFS(estado_inicial, solucion)

    if nodo:
        camino = obtener_camino(nodo)
        return jsonify({"resultado": camino})
    else:
        return jsonify({"resultado": "No hay solución"})

app.run(debug=True)