from flask import Flask 
from flask import Flask, request, render_template
import pickle
import numpy
import pandas
import sklearn
from sklearn.preprocessing import MinMaxScaler
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn import tree
from sklearn import preprocessing
from sklearn.tree import DecisionTreeRegressor

app = Flask(__name__, template_folder = 'templates')

@app.route('/', methods = ['POST', 'GET'])

@app.route('/index', methods = ['POST', 'GET'])

def main():
    if request.method == 'GET':
        return render_template('main.html')
    
    if request.method == 'POST':
        with open('pipeline_DecisionTreeRegressor_Width.pkl', 'rb') as f:
            loaded_model_Width = pickle.load(f)
        with open('pipeline_Depth_DecisionTreeRegressor.pkl', 'rb') as f:
            loaded_model_Depth = pickle.load(f)

        IW = float(request.form['IW'])
        IF = float(request.form['IF'])
        VW = float(request.form['VW'])
        FP = float(request.form['FP'])
         # Прогнозируем ширину
        Width_predict = loaded_model_Width.predict([[IW, IF, VW, FP]])
         # Возвращаем результат в шаблон
        #return render_template('main.html', width_result=Width_predict)
        # Прогнозируем глубину
        Depth_predict = loaded_model_Depth.predict([[IW, IF, VW, FP]])
         # Возвращаем результат в шаблон
        #return render_template('main.html', Depth_result=Depth_predict)
        return render_template('main.html', width_result=Width_predict, Depth_result=Depth_predict)
    
if __name__ == '__main__':
    app.run()