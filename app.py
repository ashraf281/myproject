# -*- coding: utf-8 -*-
"""
Created on Sat Jan 15 15:49:43 2022

@author: MD ASHRAF SHAMIM
"""

import numpy as np
import pickle
import streamlit as st
#loading the saved model 
loaded_model = pickle.load(open('C:/Users/MD ASHRAF SHAMIM/Downloads/machine learning/myproject/trained_model.sav', 'rb'))

#creating a function for prediction

def diabetes_prediction(input_data):
    

    # changing the input_data to numpy array
    input_data_as_numpy_array = np.asarray(input_data)

    # reshape the array as we are predicting for one instance
    input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)

    prediction = loaded_model.predict(input_data_reshaped)
    print(prediction)

    if (prediction[0] == 0):
      return 'The person is not diabetic'
    else:
      return 'The person is diabetic'
  
    


def main():
    
    #giving a title
    st.title('Diabetes Prediction Web Application')
    
    # getting the input data from the user
    Pregnancies = st.text_input('Number of pregnancies')
    Glucose = st.text_input('Glucose level')
    BloodPressure = st.text_input('Blood pressure level')
    SkinThickness = st.text_input('Skin thickness value')
    Insulin = st.text_input('Insulin level')
    BMI = st.text_input('BMI value')
    DiabetesPedigreeFunction = st.text_input('Diabetes pedigree function')
    Age = st.text_input('Age')
    
    
    #code for prediction
    diagnosis =''
    
    #creating a button for prediction
    
    if st.button('Diabetes Test Result'):
        diagnosis = diabetes_prediction([Pregnancies,Glucose,BloodPressure,SkinThickness,Insulin,BMI,DiabetesPedigreeFunction,Age])
        
        
        
    st.success(diagnosis)
    
    
    
    
if __name__ =='__main__':
    main()
   