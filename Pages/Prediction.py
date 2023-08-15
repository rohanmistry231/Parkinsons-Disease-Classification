import numpy as np
import pickle
import streamlit as st
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split

parkinsons_data = pd.read_csv('R:\\dktop\\final project  DE\\Parkinsson disease.csv')
X = parkinsons_data.drop(columns=['name','status'], axis=1)
Y = parkinsons_data['status']
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=2)
scaler = StandardScaler()
scaler.fit(X_train)

# loading the saved model
loaded_model = pickle.load(open('R:\\dktop\\final project  DE\\final\\trained_model.sav', 'rb'))

# creating a function for Prediction

def parkinsons_prediction(input_data):
    

    # changing the input_data to numpy array
    input_data_as_numpy_array = np.asarray(input_data)

    # reshape the array as we are predicting for one instance
    input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)
    std_data = scaler.transform(input_data_reshaped)
    prediction = loaded_model.predict(std_data)
    print(prediction)

    if (prediction[0] == 0):
      return 'The person has not Parkinsons Disease'
    else:
      return 'The person has Parkinsons Disease'
  
def main():
    
    
    # giving a title
    st.title("Parkinson's Disease Prediction Web App")
    
    # getting the input data from the user
  
    mdvp_fo_hz = st.text_input('MDVP - Fo(Hz)')
    mdvp_fhi_hz = st.text_input('MDVP - Fhi(Hz)')
    mdvp_flo_hz = st.text_input('MDVP - Flo(Hz)')
    mdvp_jitter_hz = st.text_input('MDVP - Jitter(%)')
    mdvp_jitter_abs = st.text_input('MDVP - Jitter(Abs)')
    mdvp_rap = st.text_input('MDVP - RAP')
    mdvp_ppq = st.text_input('MDVP - PPQ')
    jitter_ddp = st.text_input('Jitter - DDP')
    mdvp_shimmer = st.text_input('MDVP - Shimmer')
    mdvp_shimmer_db = st.text_input('MDVP - Shimmer(dB)')
    shimmer_apq3 = st.text_input('Shimmer - APQ3')
    shimmer_apq5 = st.text_input('Shimmer - APQ5')
    mdvp_apq = st.text_input('MDVP - APQ')
    shimmer_dda = st.text_input('Shimmer - DDA')
    nhr = st.text_input('NHR')
    hnr = st.text_input('HNR')
    rpde = st.text_input('RPDE')
    dfa = st.text_input('DFA')
    spread1 = st.text_input('spread1')
    spread2 = st.text_input('spread2')
    d2 = st.text_input('D2')
    ppe = st.text_input('PPE')
    
    # code for Prediction
    diagnosis = ''
    
    # creating a button for Prediction
    
    if st.button('Parkinsons Test Result'):
        diagnosis = parkinsons_prediction([mdvp_fo_hz,mdvp_fhi_hz,mdvp_flo_hz,mdvp_jitter_hz,mdvp_jitter_abs,mdvp_rap,mdvp_ppq,jitter_ddp,mdvp_shimmer,mdvp_shimmer_db,shimmer_apq3,shimmer_apq5,mdvp_apq,shimmer_dda,nhr,hnr,rpde,dfa,spread1,spread2,d2,ppe])
            
    st.success(diagnosis)
       
if __name__ == '__main__':
    main()