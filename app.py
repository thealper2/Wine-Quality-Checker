import numpy as np
import pickle
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

model = pickle.load(open("models/rf2.pkl", "rb"))

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    if request.method == "POST":
        a1 = float(request.form.get("fixed-acidity"))
        a2 = float(request.form.get("volatile-acidity"))
        a3 = float(request.form.get("citric-acid"))
        a4 = float(request.form.get("residual-sugar"))
        a5 = float(request.form.get("chlorides"))
        a6 = float(request.form.get("free-sulfur-dioxide"))
        a7 = float(request.form.get("total-sulfur-dioxide"))
        a8 = float(request.form.get("density"))
        a9 = float(request.form.get("ph"))
        a10 = float(request.form.get("sulphates"))
        a11 = float(request.form.get("alcohol"))

        test = np.array([[a1, a2, a3, a4, a5, a6, a7, a8, a9, a10, a11]])
        result = model.predict(test)

    return render_template("index.html", prediction=str(result.item()))

@app.route("/api", methods=["POST"])
def api():
    json = request.get_json(force=True)
    test = np.array(list(json.values()))
    result = model.predict([test])

    output = result.item()
    json["1-result"] = output
    print(json)
    return jsonify(json)

if __name__ == "__main__":
    app.run(port=5000, debug=True)