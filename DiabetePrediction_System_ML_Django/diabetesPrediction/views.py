from django.shortcuts import render
import pandas as pd
import numpy as np
import seaborn as sns
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

def home(request):
    return render(request, 'home.html')

def predict(request):
    return render(request, 'predict.html')

def result(request):

    df = pd.read_csv(r'C:\Users\Saheed\Desktop\Machine_Learning_Project\csv_files\diabetes.csv')
    X = df.drop(['Outcome'], axis=1)
    y = df['Outcome']
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=41)
    model = LogisticRegression()
    model.fit(X_train, y_train)

    v1 = float(request.GET['n1'])
    v2 = float(request.GET['n2'])
    v3 = float(request.GET['n3'])
    v4 = float(request.GET['n4'])
    v5 = float(request.GET['n5'])
    v6 = float(request.GET['n6'])
    v7 = float(request.GET['n7'])
    v8 = float(request.GET['n8'])

    y_pred = model.predict(np.array([v1, v2, v3, v4, v5, v6, v7, v8]).reshape(1, -1))

    result1 = ''
    if y_pred == [1]:
        result1 = 'Positive'
    else:
        result1 = 'Negative'

    result_dict = {'result1': result1}

    return render(request, 'predict.html', context=result1)
