from flask import Flask, render_template, request
from conversion import convertir_moneda
from data import obtener_tasa_conversion

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    resultado = None
    if request.method == "POST":
        monto = float(request.form["monto"])
        moneda_destino = request.form["moneda_destino"]
        tasa_conversion = obtener_tasa_conversion("USD", moneda_destino)
        resultado = convertir_moneda(monto, tasa_conversion, moneda_destino)
    return render_template("index.html", resultado=resultado)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
