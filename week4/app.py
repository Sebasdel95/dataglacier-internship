from django.shortcuts import render
import numpy as np
import pickle
from flask import Flask, request, render_template


app = Flask(__name__)
with open('model.pkl', 'rb') as f:
    model = pickle.load(f)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    """
    Predict with the data entered in the html page.
    """
    int_features = [int(x) for x in request.form.values()]
    final_features= [np.array(int_features)]
    prediction = model.predict(final_features)

    if round(prediction[0]) == 0:
        return render_template("index.html", prediction_text="The user will pay the debt")
    else:
        return render_template("index.html", prediction_text="The user won't pay the debt")

if __name__ == "__main__":
    app.run(port=5000, debug=True)