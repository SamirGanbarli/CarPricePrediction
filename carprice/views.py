from django.shortcuts import redirect, render
from pip import main
from sklearn import linear_model
from tomlkit import value
from .models import output, prediction

# data science imports
import numpy as np
import pandas as pd 
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.preprocessing import scale 
from sklearn.preprocessing import StandardScaler
from sklearn import model_selection
from sklearn.linear_model import LinearRegression
from sklearn import neighbors
from sklearn.svm import SVR 
#=================

# Create your views here.

def index(request):

    predictions = prediction.objects.all()
    outputs = output.objects.all()

    return render(request, "index.html", {"outputs":outputs})


def predict(request):

    if request.method == 'GET':

        return redirect("/")

    elif request.method == "POST":

        title = request.POST.get("title")
        year = request.POST.get("year")
        preprice = request.POST.get("preprice")
        driven = request.POST.get("driven")
        ftype = request.POST.get("ftype")
        stype = request.POST.get("stype")
        trans = request.POST.get("trans")

        newcar = prediction(title = title, year = year, 
        present_price = preprice, driven_km = driven, fuel_type = ftype,
        seller_type = stype, transmission_type = trans)

        # predictions = []
        # predictions.append(newcar)

        newcar.save()

        #===============================
        dataset = pd.read_csv('cardata.csv')
        dataset.replace({'Fuel_Type':{'Petrol':0,'Diesel':1,'CNG':2}}, inplace = True)
        dataset.replace({'Seller_Type':{'Dealer':0,'Individual':1}}, inplace = True)
        dataset.replace({'Transmission':{'Manual':0,'Automatic':1}}, inplace = True)

        X = dataset.drop(['Car_Name','Selling_Price','Owner'], axis=1)
        y = dataset['Selling_Price']
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=2)
        svrtuned = SVR(C = 0.1).fit(X_train, y_train)

        y_pred = svrtuned.predict(X_test)
        # print(np.sqrt(mean_squared_error(y_test, y_pred)))


        main_x = [
        [year,preprice,driven,ftype,stype,trans]]


        o = svrtuned.predict(main_x)

        output1 = output(title = newcar.title, value = o)

        output1.save() 

        print(o)

        return redirect("/")







