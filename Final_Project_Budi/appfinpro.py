from flask import Flask, render_template, request
import joblib
import pandas as pd
import numpy as np

app = Flask(__name__)

# halaman home
@app.route('/')
def home():
    return render_template('home.html')

# @app.route('/database', methods=['POST', 'GET'])
# def dataset():
#     pass

@app.route('/visualize', methods=['POST', 'GET'])
def visual():
    return render_template('plot.html')

@app.route('/predict', methods=['POST', 'GET'])
def predict():
    return render_template('predict.html')

@app.route('/result', methods=['POST', 'GET'])
def result():
    if request.method=='POST':
        input = request.form

        df_to_predict = pd.DataFrame({
            'price': [input['price']],
            'uses_ad_boosts': [input['uses_ad_boosts']],
            'retail_price': [input['retail_price']],
            'rating_count': [input['rating_count']],
            'rating': [input['rating']],
            'badge_local_product': [input['badge_local_product']],
            'badge_product_quality': [input['badge_product_quality']],
            'badge_fast_shipping': [input['badge_fast_shipping']],
            'merchant_rating_count': [input['merchant_rating_count']],
            'merchant_rating': [input['merchant_rating']],
        })

        prediksi = model.predict(df_to_predict)
        pred = np.expm1(prediksi)[0].round(2)

        return render_template('result.html', data=input, pred=pred)

if __name__ == '__main__':
    
    filename = 'best_model_fin_pro'
    model = joblib.load(filename)

    app.run(debug=True)