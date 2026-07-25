from flask import Flask, render_template, request
import pickle
import numpy as np

# ----------------------------
# Load Model and Scaler
# ----------------------------
model = pickle.load(open("ridge.pkl", "rb"))
scaler = pickle.load(open("scaler.pkl", "rb"))

# ----------------------------
# Create Flask App
# ----------------------------
app = Flask(__name__)

# ----------------------------
# Home Page
# ----------------------------
@app.route("/")
def home():
    return render_template("index.html")


# ----------------------------
# Prediction Route
# ----------------------------
@app.route("/predict", methods=["POST"])
def predict():
    try:
        # Get values from form
        temperature = float(request.form["Temperature"])
        rh = float(request.form["RH"])
        ws = float(request.form["Ws"])
        rain = float(request.form["Rain"])
        ffmc = float(request.form["FFMC"])
        dmc = float(request.form["DMC"])
        isi = float(request.form["ISI"])
        fire_class = int(request.form["Classes"])
        region = int(request.form["Region"])

        # Arrange features exactly in training order
        features = np.array([[
            temperature,
            rh,
            ws,
            rain,
            ffmc,
            dmc,
            isi,
            fire_class,
            region
        ]])

        # Scale data
        scaled_features = scaler.transform(features)

        # Predict
        prediction = model.predict(scaled_features)[0]

        # Risk Category
        if prediction < 5:
            risk = "🟢 Very Low Risk"
        elif prediction < 15:
            risk = "🟢 Low Risk"
        elif prediction < 30:
            risk = "🟡 Moderate Risk"
        elif prediction < 45:
            risk = "🟠 High Risk"
        else:
            risk = "🔴 Extreme Risk"

        return render_template(
            "index.html",
            prediction=round(prediction, 2),
            risk=risk
        )

    except Exception as e:
        return render_template(
            "index.html",
            error=str(e)
        )


# ----------------------------
# Run App
# ----------------------------
if __name__ == "__main__":
    app.run(debug=True)