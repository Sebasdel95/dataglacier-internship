import pandas as pd
import pickle
from flask import Flask, jsonify, request


app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'GET':
        home = 'Hello world!!'
        return jsonify({'home': home})

@app.route('/predict/')
def predict():
    """
    Predict with the data entered in the html page.
    """
    with open('model.pkl', 'rb') as f:
        model = pickle.load(f)
    credit_policy = request.args.get('credit_policy')
    int_rate = request.args.get('int_rate')
    installment = request.args.get('installment')
    log_annual_inc = request.args.get('log_annual_inc')
    dti = request.args.get('dti')
    fico = request.args.get('fico')
    days_with_cr_line = request.args.get('days_with_cr_line')
    revol_bal = request.args.get('revol_bal')
    revol_util = request.args.get('revol_util')
    inq_last_6mths = request.args.get('inq_last_6mths')
    delinq_2yrs = request.args.get('delinq_2yrs')
    pub_rec = request.args.get('pub_rec')

    test_df = pd.DataFrame({
        'Credit Policy': [credit_policy],
        'Interest rate': [int_rate],
        'Installment': [installment],
        'Log Annual Income': [log_annual_inc],
        'Debt-to-Income': [dti],
        'FICO': [fico],
        'Days with Credit Line': [days_with_cr_line],
        'Revolving Balance': [revol_bal],
        'Revolving Line Utilization': [revol_util],
        'Inquiries in the last 6 months': [inq_last_6mths],
        'Days past due on a payment': [delinq_2yrs],
        'Derogatory Public Records': [pub_rec]
    })
    prediction = model.predict(test_df)
    if int(round(prediction[0])) == 1:
        return jsonify({
            "Loan Payment Prediction": "The user won't fully pay the loan"
        })
    else:
        return jsonify({
            "Loan Payment Prediction": "The user will fully pay the loan"
        })

if __name__ == "__main__":
    app.run(port=5000, debug=True)


