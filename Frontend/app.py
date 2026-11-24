import streamlit as st
import requests

st.title("House Price Prediction")

st.write("Enter the House details  below")

income=st.number_input("Income",min_value=0.0)
age=st.number_input("House Age",min_value=0.0)
rooms=st.number_input("Total Rooms",min_value=1)
bedrooms=st.number_input("Total Bedrooms",min_value=1)
population=st.number_input("Population",min_value=0)

if st.button("Predict House Price"):

    data={
        "income": income,
        "age": age,
        "rooms": rooms,
        "bedrooms": bedrooms,
        "population": population
    }

    try:
        #connect frontend with backend through requests(use POST)..predict is the 
        # endpoint and it is mentioned in the backend code 
        response = requests.post(
            "http://127.0.0.1:5000/predict",
            json=data
        )
        #flask communicate python code using json format
        result=response.json()

        if response.status_code == 200:
            st.success(
                f"Predicted House Price: {result['predicted_price']:.2f}"
            )
        else:
            st.error(result["error"])

    except requests.exceptions.ConnectionError:
        st.error("Flask backend is not running.")
