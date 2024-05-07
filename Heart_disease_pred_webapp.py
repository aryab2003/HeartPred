import numpy as np
import pickle
import streamlit as st


# Function to load the model
def load_model(model_file):
    loaded_model = pickle.load(model_file)
    return loaded_model


# creating the predictor function
def heart_prediction(loaded_model, input_data):
    input_data_as_numpy_array = np.asarray(input_data).astype(
        float
    )  # Convert input to float
    input_data_reshaped = input_data_as_numpy_array.reshape(1, -1)

    prediction = loaded_model.predict(input_data_reshaped)
    prediction = loaded_model.predict(input_data_reshaped)
    print(prediction)

    if prediction[0] == 0:
        return "Person does not have heart disease"
    if prediction[0] == 0:
        return "Person does not have heart disease"
    else:
        return "Person has heart disease"

        return "Person has heart disease"


def main():
    st.title("Heart Predictor")

    # Allow users to upload model
    model_file = st.file_uploader("Upload Model File (.sav)", type="sav")
    if model_file is not None:
        loaded_model = load_model(model_file)

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

        # Check if input fields are not empty before converting to float
        input_data = [
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
        if all(input_data):
            input_data = [float(x) for x in input_data]

            diagnosis = ""
            if st.button("Heart Test Result"):
                diagnosis = heart_prediction(loaded_model, input_data)

            st.success(diagnosis)
        else:
            st.error("Please fill in all the input fields.")


if __name__ == "__main__":
    main()
