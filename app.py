
from pyexpat import features

import numpy as np
import pandas as pd
from flask import Flask, request, jsonify, render_template
import pickle
from sklearn.preprocessing import MinMaxScaler
from sklearn import preprocessing

# from sklearn import preprocessing

# label_encoder object knows how to understand word labels.
# label_encoder = preprocessing.LabelEncoder()
# df = pd.read_csv(".\data\Churn_Modelling.csv")
# categorical_df = df[[ "Surname","Geography","Gender"]]


app = Flask(__name__)
model = pickle.load(open("modelGnb2.pkl", "rb"))


@app.route("/")
def home():
    
    return render_template("index.html")



@app.route("/predict", methods=["POST"])
def predict():
    df = pd.read_csv('data/Churn_Modelling.csv')
    categorical_df = df[[ "Surname","Geography","Gender"]]
    
    # label_encoder object knows how to understand word labels.
    label_encoder = preprocessing.LabelEncoder()

    # use LabelEncoder to encode Categorical Variable
    for label in categorical_df[0:]:
        df[label]= label_encoder.fit_transform(df[label])

    # split dataset into x,y
    X_data = df.drop(columns=['Exited','RowNumber','CustomerId','Surname'],axis=1)
    y = df['Exited']
    # Menangani imbalance dengan oversampling 

    form_data = dict(request.form)
    
    # Create a pandas DataFrame from the dictionary
    data = pd.DataFrame([form_data])

    data_X = data.drop(columns=['CustomerId','Surname'], axis=1)

    categorical_df = ["Geography"]
    
    # label_encoder object knows how to understand word labels.
    label_encoder = preprocessing.LabelEncoder()

    # use LabelEncoder to encode Categorical Variable
    # Convert form data to a dictionary
    data_X[categorical_df]= label_encoder.fit_transform(data_X[categorical_df])

    print("Data as DataFrame:")
    print(form_data)  # Print the DataFrame for debugging
    # for x in request.form.values():
    #     data = []
    #     if (type(x) == str):

    #     data.append(x)
    # for label in categorical_df[0:]:
    #     df[label]= label_encoder.fit_transform(df[label])
    #     df = df.astype({label : 'float'})
    ms = MinMaxScaler()
    X_data = ms.fit_transform(X_data)
    features = ms.transform(data_X)
    prediction = model.predict(features)
    if prediction == 0:
        hasilPrediksi = "Not Churn"
    else:
        hasilPrediksi = "Churn"

    return render_template("index.html", prediction_text = "{}".format(hasilPrediksi))

if __name__ == "__main__":
    app.run(debug=True)