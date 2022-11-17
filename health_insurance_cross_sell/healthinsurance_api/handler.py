import pandas as pd
import pickle
import os

from flask import Flask, request, Response
from healthinsurance.HealthInsurance import HealthInsurance

app = Flask(__name__)

# Carregamento do modelo de predição
model = pickle.load( open( 'models/model_xgb.pkl', 'rb') )

@app.route('/predict', methods=['POST'])

def health_insurance_classification():
    
    # recebimento da requisição
    test_json = request.get_json()
    
    # verificação para saber se houve recebimento de dados na requisição
    if test_json:
        
        # Unique Example
        if isinstance(test_json, dict):
            test_raw = pd.DataFrame(test_json, index=[0]).copy()
        # Multiple Example
        else:
            test_raw = pd.DataFrame(test_json, columns=test_json[0].keys()).copy()
    
        # Instanciando a classe Health_Insurance
        pipeline = HealthInsurance()

        # Limpeza dos Dados
        df_cleaned = pipeline.data_cleaning(test_raw).copy()

        # feature Engineering
        df_feature_engineering = pipeline.feature_engineering(df_cleaned).copy()

        # Preparação dos Dados
        df_preparation = pipeline.data_preparation(df_feature_engineering).copy()

        # Predicao
        df_response = pipeline.prediction(model, df_preparation, test_raw)
        
        return df_response
    
    else:
        
        return Response('{}', status=200, mimetype='application/json')
    
    
if __name__ == '__main__':
    port = os.environ.get('PORT', '5000')
    app.run(host='0.0.0.0', port=port)     