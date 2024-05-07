import pickle
import numpy as np
import pandas as pd
from flask import Flask, render_template, request, redirect , url_for
#from flask_sqlalchemy import SQLAlchemy
#from datetime import datetime

app = Flask(__name__)
model = pickle.load(open('liver2.pkl','rb'))
scaler = pickle.load(open('scaler.pkl','rb'))

Status_dict = {
    "C": 0,
    "CL": 1,
    "D": 2
}

Drug_dict = {
    "dpen": 0,
    "placebo": 1
}

Sex_dict = {
    "F": 0,
    "M": 1
}

Ascites_dict = {
    "N": 0,
    "Y": 1
}

Hepatomegaly_dict = {
    "N": 0,
    "Y": 1
}

Spider_dict = {
    "N": 0,
    "Y": 1
}

Edema_dict = {
    "N": 0,
    "S": 1,
    "Y": 2
}

Stage = {
    0: "Histolic Stage 1",
    1: "Histolic Stage 2",
    2: "Histolic Stage 3"
    # 3: "Histolic Stage 4"
}

@app.route('/', methods=['GET','POST'])
def liver_main():
    return render_template('liver_main.html')


@app.route('/liver_main', methods=['GET','POST'])
def index():
    Attributes = []
    return render_template('liver_main.html')


@app.route('/liver_form', methods=['GET','POST'])
def liver_form():
    return render_template('liver_form.html')

@app.route('/liver_pred',methods=['GET','POST'])
def liver_pred():
    Attributes = []
    Ndays = float(request.form["ndays"]) #1
    Attributes.append(Ndays)

    Status = request.form["status"] #2
    Status = float(Status_dict[Status])
    Attributes.append(Status)
    
    drug = request.form["drug"] #3
    drug = float(Drug_dict[drug])
    Attributes.append(drug)

    age = float(request.form["age"])
    age = age*365#4
    Attributes.append(age)


    gender = request.form["gender"] #5
    gender= float(Sex_dict[gender]) # convert to numerical value
    Attributes.append(gender)


    ascites = request.form["ascites"] #6
    ascites= float(Ascites_dict[ascites]) # convert to numerical value
    Attributes.append(ascites)


    Hepatomegaly = request.form["hepatomegaly"] #7
    Hepatomegaly = float(Hepatomegaly_dict[Hepatomegaly]) # convert to numerical value
    Attributes.append(Hepatomegaly)


    Spiders = request.form["spiders"] #8
    Spiders= float(Spider_dict[Spiders])
    Attributes.append(Spiders)


    Edema = request.form["edema"] #9
    Edema = float(Edema_dict[Edema]) # convert to numerical value
    Attributes.append(Edema)


    bilirubin = float(request.form["bilirubin"]) #10
    Attributes.append(bilirubin)


    cholestrol = float(request.form["cholestrol"]) #11
    Attributes.append(cholestrol)


    albumin = float(request.form["albumin"]) #13
    Attributes.append(albumin)


    copper = float(request.form["copper"]) #14
    Attributes.append(copper)


    alk_fos = float(request.form["alk_fos"]) #15
    Attributes.append(alk_fos)
    
    sgot = float(request.form["sgot"]) #15
    Attributes.append(sgot)
    
    Tryglicerides = float(request.form["tryglicerides"]) #15
    Attributes.append(Tryglicerides)
    
    platelets = float(request.form["platelets"]) #15
    Attributes.append(platelets)
    
    Prothrombin = float(request.form["prothrombin"]) #15
    Attributes.append(Prothrombin)

    
    Attribute_arr= np.array([Attributes])
    print(Attribute_arr)
    scaled_attr = scaler.transform(Attribute_arr.reshape(1,-1))
    predict_result = model.predict(Attribute_arr)
  
    prediction = Stage[predict_result[0]]
    print(predict_result[0])
    
    return render_template('liver_form.html',prediction_text = f' {prediction}')


if __name__ == '__main__':
    app.run(debug=True)
