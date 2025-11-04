Iris Flower Classification Project

Made By: Sobiya Khan

About This Project

In this project, I used the Iris dataset and created a Machine Learning model to classify the flower species into:

Setosa

Versicolor

Virginica

I used K-Nearest Neighbors (KNN) algorithm and then deployed the model on Streamlit so anyone can enter values and get the prediction.

Files in This Project
File Name	Purpose
model_train.py	Trains the ML model and saves iris-app.pkl
app.py	Streamlit web app for predictions
iris-app.pkl	Saved trained model (auto generated)
README.md	Project explanation
Steps to Run the Project
✅ Step 1: Train the Model

Run this file first:

python model_train.py


This will train the model and save it as iris-app.pkl.

✅ Step 2: Run Streamlit App
streamlit run app.py


A web page will open to enter:

Sepal Length

Sepal Width

Petal Length

Petal Width

Then click Predict Flower Type.
You will get flower name like 🌼 Setosa, 🌿 Versicolor, 🌺 Virginica.

Libraries Used

Python

Pandas

NumPy

Scikit-Learn

Streamlit

Install the packages:

pip install streamlit scikit-learn pandas numpy

Learning Outcome

From this project I learned:

How to load dataset

Train ML model using KNN

Find best K value

Save model using pickle

Deploy ML model in Streamlit

Author

Name: Sobiya Khan
Course: DCA / AIML Practice Project
Purpose: Learning Machine Learning and Deployment

