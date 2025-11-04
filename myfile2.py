import streamlit as st
import pickle
import numpy as np

# Load saved model
model = pickle.load(open("iris-app.pkl", "rb"))

st.title("🌸 Iris Flower Prediction App")
st.write("Enter flower measurements below to predict species")

# Taking Inputs
sepal_length = st.number_input("Sepal Length (cm)", 0.0, 10.0, 5.1)
sepal_width  = st.number_input("Sepal Width (cm)", 0.0, 10.0, 3.5)
petal_length = st.number_input("Petal Length (cm)", 0.0, 10.0, 1.4)
petal_width  = st.number_input("Petal Width (cm)", 0.0, 10.0, 0.2)

# Species map
species = {0: "Setosa 🌼", 1: "Versicolor 🌿", 2: "Virginica 🌺"}

# Prediction Button
if st.button("Predict Flower Type"):
    input_data = np.array([[sepal_length, sepal_width, petal_length, petal_width]])
    pred = model.predict(input_data)[0]
    st.success(f"### ✅ Prediction: **{species[pred]}**")
