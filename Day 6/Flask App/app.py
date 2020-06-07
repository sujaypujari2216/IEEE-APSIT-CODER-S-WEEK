# -*- coding: utf-8 -*-
"""
Created on Sun Jun 7 18:00:10 2020

@author: Sujay
"""


from flask import Flask , render_template ,request
from sklearn.preprocessing import StandardScaler
import pickle

app  = Flask(__name__)
model = pickle.load(open('DTC.pkl','rb'))
sc=StandardScaler()

@app.route('/')
def index():
    return render_template('index.html',data="null")

@app.route('/predict',methods = ['GET','POST'])
def predict():
    if request.method == 'POST':
      gender = request.form['gender']
      age= request.form['age']
      sal= request.form['sal']
      
      data=[[int(gender),int(age),int(sal)]]
      p=model.predict(sc.fit_transform(data))
      if p[0]==1:
          prediction="User will purchase product"
      else:
          prediction="User won't purchase product"

      return render_template('index.html',prediction="Prediction: "+prediction)

if __name__=='__main__':
    app.run(debug=True)