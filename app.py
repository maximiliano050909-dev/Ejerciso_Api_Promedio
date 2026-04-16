from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/convertir-temperatura', methods=['POST'])
def convertir_temperatura():
    datos = request.get_json()

    valor = datos['valor']
    escala = datos['escala']

    if escala == "C":
        resultado = (valor * 9/5) + 32
        tipo = "Fahrenheit"
    elif escala == "F":
        resultado = (valor - 32) * 5/9
        tipo = "Celsius"
    else:
        return jsonify({"error": "Escala no válida"}), 400

    return jsonify({
        "valor_original": valor,
        "escala_original": escala,
        "resultado": resultado,
        "escala_convertida": tipo
    })


# 🔥 SIEMPRE AL FINAL
if __name__ == '__main__':
    app.run(debug=True)