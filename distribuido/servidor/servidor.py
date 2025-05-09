from flask import Flask, request, jsonify
from conversion import convertir_moneda
from data import obtener_tasa_conversion

app = Flask(__name__)

@app.route("/convertir", methods=["GET"])
def convertir():
    monto = float(request.args.get("monto"))
    moneda_destino = request.args.get("moneda_destino")
    tasa_conversion = obtener_tasa_conversion("USD", moneda_destino)
    resultado = convertir_moneda(monto, tasa_conversion, moneda_destino)
    return jsonify({"resultado": resultado})

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5002)
