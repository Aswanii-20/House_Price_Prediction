from flask import Flask,request,jsonify
import numpy as np
import joblib

 #Create Flask Application
app=Flask(__name__)

#Load Model and Scaler
model=joblib.load('house_price.pkl')
scaler=joblib.load('scaler.pkl')

#Home Route
@app.route("/")
def home():
    return "House Price Prediction API is running!"

#Prediction route
@app.route("/predict",methods=["POST"])
def predict():
    #receive data from frontend and convert the data to dictionary
    data = request.get_json()
    
    # extract input features
    features=[
        data["income"],
        data["age"],
        data["rooms"],
        data["bedrooms"],
        data["population"]
    ]

    #convert into Numpy array
    input_data = np.array(features).reshape(1,-1)

    #scale the input
    input_scaled = scaler.transform(input_data)

    #predict house price
    prediction = model.predict(input_scaled)

    #Return Prediction...covert the data into json format
    return jsonify({
        "predicted_price":float(prediction[0])
    })

# Run Flask application
if __name__=="__main__":
    app.run(debug=True)

