import numpy as np
import pickle
import streamlit as st

loaded_model = pickle.load(open('trained_model.sav', 'rb'))

# Creating a funvtion for pridiction
def diabetes_pridection(input_data):

	# changing input data into numpy array
	input_data_as_array = np.asarray(input_data)

	# reshaping the array

	input_data_reshaped = input_data_as_array.reshape(1,-1)

	# Standardize the input data

	prediction = loaded_model.predict(input_data_reshaped)
	print(prediction)

	if prediction[0] == 0:
		return "The person is not Diabetic"
	else:
		return "The Person is Diabetic"
	
def main():
	
	
	# Giving a title 
	st.title("Diabetes Pridection System")
	
	# getting the input_data from the user
	
	Pregnancies = st.text_input('No. of Pragnancies')
	Glucose = st.text_input('Glucose Level')
	BloodPressure = st.text_input('Blood Presure Level')
	SkinThickness = st.text_input('Skin Thickness')
	Insulin = st.text_input('Insulin Level')
	BMI = st.text_input('Body Mass Index')
	DiabetesPedigreeFunction = st.text_input('Diabetes Pidegree Function Value')
	Age = st.text_input('Age of the Person')
	
	# Code for pridection
	
	diagnose = ""
	 
	# Creating a button for prediction
	
	if st.button("Diabetes Test Result"):
		diagnosis = diabetes_prediction(Pregnancies, Glucose, BloodPresure, SkinThickness, Insulin, BMI, DiabetesPidegreeFunction, Age)
		
	st.success(diagnosis)
	
	
if __name__=="__main__":
	main()
