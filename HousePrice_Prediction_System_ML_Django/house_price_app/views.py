from django.shortcuts import render

import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pylab as plt
from sklearn import metrics
from sklearn.metrics import accuracy_score, mean_absolute_error
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
# Create your views here.
def home(request):
    return render(request, 'home.html')

def predict(request):
    return render(request, 'predict.html')

def result(request):
    df = pd.read_csv(r'C:\Users\Saheed\Desktop\Machine_Learning_Project\csv_files\USA_Housing.csv')
    df = df.drop(['Address'], axis=1)
    X = df.drop(columns='Price', axis=1)
    y = df['Price']
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=45)
    model = LinearRegression()
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)

    v1 = float(request.GET['n1'])
    v2 = float(request.GET['n2'])
    v3 = float(request.GET['n3'])
    v4 = float(request.GET['n4'])
    v5 = float(request.GET['n5'])

    y_pred = model.predict(np.array([v1, v2, v3, v4, v5]).reshape(1, -1))
    y_pred = round(y_pred[0])
    predicted_price = 'Predicted Price: $' + str(y_pred)
    price_dict = {'predicted_price': predicted_price}

    return render(request, 'predict.html', context=price_dict)
