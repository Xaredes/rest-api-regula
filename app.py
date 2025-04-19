from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return "API działa poprawnie"

@app.route("/api/v1.0/predict", methods=["GET"])
def predict():
    try:
        num1 = float(request.args.get("num1"))
        num2 = float(request.args.get("num2"))
    except (TypeError, ValueError):
        return jsonify({"error": "Nieprawidłowe dane wejściowe"}), 400

    suma = num1 + num2
    prediction = 1 if suma > 5.8 else 0

    return jsonify({
        "prediction": prediction,
        "features": {
            "num1": num1,
            "num2": num2
        }
    })

if __name__ == "__main__":
    app.run(debug=True)
