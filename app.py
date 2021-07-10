import streamlit as st
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from PIL import Image  
import pickle

html_temp = """
    <div style="background-color:#010200;padding:10px">
    <h1 style="color:white;text-align:center;">Safe Prediction</h1>
    </div>
    """    
st.markdown(html_temp,unsafe_allow_html=True)

image = Image.open('image.png') 

st.image(image, use_column_width=True,format='auto')

def user_input_features():
    Te = st.slider('Te', 12, 20)
    Tc = st.slider('Tc', 15, 20)
    Le = st.slider('Le', 112, 116)
    data = {'Te': Te,
            'Tc': Tc,
            'Le': Le}
    features = pd.DataFrame(data, index=[0])
    return features

st.subheader('Please Enter Input Through Slider')
df = user_input_features()     
        
st.subheader('User Input parameters')
st.write(df)

model=pickle.load(open('TK.pkl','rb'))

prediction = model.predict(df)
prediction_proba = model.predict_proba(df)

st.subheader('Prediction Probability')
st.write('Evaporator Coil Choke:',prediction_proba[0][0])
st.write('Condensor Coil Choke:',prediction_proba[0][1])
st.write('Dischage High Line temp:',prediction_proba[0][2])
st.write('Normal Condition:',prediction_proba[0][3])
st.write('Evaporation & Condensor Coil problem:',prediction_proba[0][4])
st.write('Condensor and Dicharge problem:',prediction_proba[0][5])
st.write('Evaporator and Discharge problems:',prediction_proba[0][6])
st.write('All problems:',prediction_proba[0][7])


html_temp1 = """
    <div style="background-color:#010200">
    <p style="color:white;text-align:center;" >Designe & Developed By: <b>Tanvi Kurade</b> </p>
    </div>
    """
st.markdown(html_temp1,unsafe_allow_html=True)

