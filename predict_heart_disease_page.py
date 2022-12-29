import streamlit as st
import pickle
from PIL import Image

def load_model():
    with open('Hyperparameter_Tuning_Random_Forest_Heart_Diseases.pkl', 'rb') as training_model:
        data = pickle.load(training_model)
    return data

data = load_model()

def convert_str_to_int(input):
    if(input=="Yes"):
        return 1
    elif (input=="No"):
        return 0

def convert_chest_pain_to_int(input):
    if(input=="Atypical Angina"):
        return 1
    elif (input=="Non-Anginal Pain"):
        return 2
    elif (input=="Asymptomatic"):
        return 3
    elif (input=="Typical Angina"):
        return 4


def gender_to_int(input):
    if(input=="Male"):
        return 1
    elif (input=="Female"):
        return 2

def resting_ecg_to_int(input):
    if(input=="Normal"):
        return 1
    elif (input=="ST"):
        return 2
    elif (input=="Left Ventricular Hypertrophy"):
        return 3


def ST_Slope_to_int(input):
    if(input=="Upsloping"):
        return 1
    elif (input=="Flat"):
        return 2
    elif (input=="Downsloping"):
        return 3


def show_predict_heart_disease_page():
    ST_slope_image = Image.open('St_Segment.png')
    st.title("Heart Disease Prediction System")
    st.write("""We will help to determine if you are suffering from heart disease""")
    st.warning("Warning: Please use at your own risk. Result may be inaccurate at certain times. The owner is not liable and won't bear responsibility if anyone suffers damages.")

    answer1 = {
        "No",
        "Yes"
    }
    answer2 = {
        "Atypical Angina", 
        "Non-Anginal Pain", 
        "Asymptomatic", 
        "Typical Angina"
    }
    answer3 = {
        "Male",
        "Female"
    }
    answer4 = {
        "Normal",
        "ST",
        "Left Ventricular Hypertrophy",
    }
    answer5 = {
        "Upsloping", 
        "Flat",
        "Downsloping",
    }
    q1	= st.slider("1. Age",1,121,25)
    q2	= st.selectbox("2. Sex",answer3)
    q3 = st.selectbox("3. What type of chest pain",answer2)
    st.info('Typical Angina has all 3 characteristics: \n' +
    '1. Substernal chest discomfort of characteristic quality and duration\n' +
    '2. Provoked by exertion or emotional stress \n' +
    '3. Relieved by rest and/or nitroglycerine.\n' + 
    'Atypical Angina characteristics: \n' +
    '1. Meets two of typical angina characteristics: \n' +
    'Non-Anginal Pain characteristics: \n' +
    '1. Meets one or none of typical angina characteristics: \n' +
    'Asymptomatic characteristics: \n' +
    '1. Does not show any symptoms')
    q4	= st.slider("4. Resting Blood Pressure",0,200,100)
    q5 = st.slider("5. Cholesterol",0,500,250)
    q6	= st.selectbox("6. Fasting Blood Pressure (Blood Pressure before eating)",answer1)
    q7 = st.selectbox("7. RestingECG", answer4)
    q8 = st.slider("8. Max Heart Rate",0,250,125)
    q9 = st.selectbox("9. Exercise Angina (Pain in the chest during exercise)",answer1)
    q10 = st.slider("10. OldPeak (ST depression induced by exercise relative to rest)",0.0,6.0,1.5)
    q11 = st.selectbox("11. ST Slope (The slope of the peak exercise ST segment based on ECG charts) ",answer5)
    st.info("References between St Slopes")
    st.image(ST_slope_image,width=350)


    Submit = st.button("Submit")

    FastingBS=convert_str_to_int(q6)
    ExerciseAngina=convert_str_to_int(q9)
    ChestPainType=convert_chest_pain_to_int(q3)
    Sex=gender_to_int(q2)
    RestingECG=resting_ecg_to_int(q7)
    ST_Slope=ST_Slope_to_int(q11)

    if Submit:
        predict_heart_disease = data.predict([[q1,Sex,ChestPainType,q4,q5,FastingBS,RestingECG,q8,ExerciseAngina,q10,ST_Slope]])
        if(predict_heart_disease==1):
            st.error("Outcome: You have a high possibility of heart disease")
        elif(predict_heart_disease==0):
            st.success("Outcome: You have no heart disease")
