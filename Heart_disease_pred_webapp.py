# -*- coding: utf-8 -*-
"""
Created on Mon May  6 11:43:13 2024

@author: HP
"""

import numpy as np
import pickle
import streamlit as st

loaded_model = pickle.load(
    open("C:\\Users\\HP\\OneDrive\\Desktop\\HeartPred\\trained_model.sav", "rb")
)


# creating the predictor function
def heart_prediction(input_data):
    input_data = (57, 0, 0, 120, 354, 0, 1, 163, 1, 0.6, 2, 0, 2)
    input_data_as_numpy_array = np.asarray(input_data)
    input_data_reshaped = input_data_as_numpy_array.reshape(1, -1)

    prediction = loaded_model.predict(input_data_reshaped)
    print(prediction)

    if prediction[0] == 0:
        return "Person does not have heart disease"
    else:
        return "Person has heart disease"


def main():

    st.title("Heart Predictor")

    age = st.text_input("Age")

    sex = st.text_input("Gender")

    cp = st.text_input("Chest Pain type")

    trestbps = st.text_input("Resting blood pressure")

    chol = st.text_input("SerumCholesterol")
    fbs = st.text_input("Fasting blood sugar")
    restecg = st.text_input("Resting electrographic results")
    thalach = st.text_input("Maximum heart rate achieved")
    exang = st.text_input("Exercise induced angina")
    oldpeak = st.text_input("ST depression induced by exercise relative to rest")
    slope = st.text_input("Slope of ST segment")
    ca = st.text_input("Number of major vessels colored")
    thal = st.text_input("Defect Type")

    diagnosis = ""

    if st.button("Heart Test Result"):
        diagnosis = heart_prediction(
            [
                age,
                sex,
                cp,
                trestbps,
                chol,
                fbs,
                restecg,
                thalach,
                exang,
                oldpeak,
                slope,
                ca,
                thal,
            ]
        )

    st.success(diagnosis)


if __name__ == "__main__":
    main()
