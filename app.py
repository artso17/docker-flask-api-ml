from flask import Flask, request, jsonify
from modules.insurance_model import InsuranceModel
import pandas as pd 
import os 


app = Flask(__name__)

@app.route('/')
def home():
    return f"Flask Web Server is Running on {os.environ.get('RUNNING_ON','Local Machine')}"

@app.route('/predict',methods = ['POST'])
def predict():
    data = request.get_json()
    df = pd.DataFrame(data,index = [0])
    predict_result = InsuranceModel.runModel(data=df, typed= 'single')
    print(predict_result)
    return jsonify({
        'status': 'predicted',
        'result' : predict_result
    })



app.run()

