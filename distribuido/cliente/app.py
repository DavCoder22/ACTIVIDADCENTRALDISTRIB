from flask import Flask, render_template, request
from cliente import ClienteConversion

app = Flask(__name__)
cliente = ClienteConversion("http://servidor:5002")

@app.route("/", methods=["GET", "POST"])
def index():
    resultado = None
    error = None
    if request.method == "POST":
        monto = float(request.form["monto"])
        moneda_destino = request.form["moneda_destino"]
        resultado = cliente.convertir_moneda(monto, moneda_destino)
        if resultado is None:
            error = "No se pudo obtener la conversión. Verifica que el servidor esté corriendo."
    return render_template("index.html", resultado=resultado, error=error)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5003)
