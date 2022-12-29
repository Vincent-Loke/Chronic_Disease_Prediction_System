import streamlit as st
import pickle

def load_model2():
    with open('Random_Forest_Stroke_Prediction.pkl', 'rb') as training_model:
        data = pickle.load(training_model)
    return data

data = load_model2()

def convert_str_to_int(input):
    if(input=="Yes"):
        return 1
    elif (input=="No"):
        return 0



def convert_work_type_to_int(input):
    if(input=="Self-employed"):
        return 1
    elif (input=="Private"):
        return 2
    elif (input=="Govt_job"):
        return 3
    elif (input=="children"):
        return 4
    elif (input=="Never_worked"):
        return 5


def gender_to_int(input):
    if(input=="Male"):
        return 1
    elif (input=="Female"):
        return 2

def Residence_type_to_int(input):
    if(input=="Urban"):
        return 1
    elif (input=="Rural"):
        return 2


def smoking_status_to_int(input):
    if(input=="never smoked"):
        return 1
    elif (input=="smokes"):
        return 2
    elif (input=="formerly smoked"):
        return 3
    elif (input=="Unknown"):
        return 4


def show_predict_stroke_page():
    
    st.title("Stroke Prediction System")
    st.write("""We will help to determine if you are suffering from Stroke""")
    st.warning("Warning: Please use at your own risk. Result may be inaccurate at certain times. The owner is not liable and won't bear responsibility if anyone suffers damages.")

    answer1 = {
        "Yes",
        "No"
    }
    answer2 = {
        "Self-employed", 
        "Private", 
        "Govt_job", 
        "children",
        "Never_worked"
    }
    answer3 = {
        "Male",
        "Female"
    }
    answer4 = {
        "Urban",
        "Rural"
    }
    answer5 = {
        "never smoked", 
        "smokes", 
        "formerly smoked",
        "Unknown"
    }
    q1	= st.selectbox("1. Gender",answer3)
    q2	= st.slider("2. Age",1,121,25)
    q3 = st.selectbox("3. Hypertension",answer1)
    q4	= st.selectbox("4. Heart Disease",answer1)
    q5 = st.selectbox("5. Ever Married",answer1)
    q6	= st.selectbox("6. Work Type",answer2)
    q7 = st.selectbox("7. Residence type", answer4)
    q8 = st.slider("8. Average glucose level",0,350,125)
    q9 = st.slider("9. bmi",0,40,20)
    q10 = st.selectbox("10. Smoking status",answer5)

    Submit = st.button("Submit")

    hypertension=convert_str_to_int(q3)
    heart_disease=convert_str_to_int(q4)
    ever_married=convert_str_to_int(q5)
    work_type=convert_work_type_to_int(q6)
    gender=gender_to_int(q1)
    Residence_type=Residence_type_to_int(q7)
    smoking_status=smoking_status_to_int(q10)


    if Submit:
        predict_stroke = data.predict([[gender,q2,hypertension,heart_disease,ever_married,work_type,Residence_type,q8,q9,smoking_status]])
        if(predict_stroke==1):
            st.error("Outcome: You have high risk of stroke")
        elif(predict_stroke==0):
            st.success("Outcome: You do not have risk of stroke")
