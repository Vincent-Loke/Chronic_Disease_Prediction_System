import streamlit as st
import pickle

def load_model():
    with open('Support_Vector_Machine_Lung_Cancer_1.pkl', 'rb') as training_model:
        data = pickle.load(training_model)
    return data

data = load_model()

def convert_str_to_int(input):
    if(input=="Yes"):
        return 2
    elif (input=="No"):
        return 1


def gender_to_int(input):
    if(input=="Male"):
        return 1
    elif (input=="Female"):
        return 0


def show_predict_lung_cancer_page():
    
    st.title("Lung Cancer Prediction System")
    st.write("""We will help to determine if you are suffering from Lung Cancer""")
    st.warning("Warning: Please use at your own risk. Result may be inaccurate at certain times. The owner is not liable and won't bear responsibility if anyone suffers damages.")

    answer1 = {
        'No',
        'Yes'
    }
    answer2 = {
        "Male",
        "Female"
    }
    q1	= st.selectbox("1. Gender",answer2)
    q2	= st.slider("2. Age",1,121,25)
    q3 = st.selectbox("3. Smoking",answer1)
    q4	= st.selectbox("4. Yellow Fingers",answer1)
    q5 = st.selectbox("5. Anxiety",answer1)
    q6	= st.selectbox("6. Peer Pressure",answer1)
    q7	= st.selectbox("7. Chronic Disease (e.g. Diabetes, High Blood Pressure, etc.)",answer1)
    q8	= st.selectbox("8. Fatigue",answer1)
    q9	= st.selectbox("9. Allergy",answer1)
    q10	= st.selectbox("10. Wheezing",answer1)
    q11	= st.selectbox("11. Alcohol Consistency",answer1)
    q12	= st.selectbox("12. Coughing",answer1)
    q13	= st.selectbox("13. Shortness of breath",answer1)
    q14	= st.selectbox("14. Shallowing Discomfort",answer1)
    q15	= st.selectbox("15. Chest Pain",answer1)

    Submit = st.button("Submit")

    # convert string into integers
    gender=gender_to_int(q1)
    smoking=convert_str_to_int(q3)
    yellow_fingers=convert_str_to_int(q4)
    anxiety=convert_str_to_int(q5)
    peer_pressure=convert_str_to_int(q6)
    chronic_disease=convert_str_to_int(q7)
    fatigue=convert_str_to_int(q8)
    allergy=convert_str_to_int(q9)
    wheezing=convert_str_to_int(q10)
    alcohol_consistency=convert_str_to_int(q11)
    coughing=convert_str_to_int(q12)
    shortness_of_breath=convert_str_to_int(q13)
    shallowing_discomfort=convert_str_to_int(q14)
    chest_pain=convert_str_to_int(q15)

    #Converted data is inserted into the machine learning to obtain the result
    if Submit:
        predict_stroke = data.predict([[gender,q2,smoking,yellow_fingers,anxiety,peer_pressure,chronic_disease,
        fatigue,allergy,wheezing,alcohol_consistency,coughing,shortness_of_breath,shallowing_discomfort,chest_pain]])
        if(predict_stroke==1):
            st.error("Outcome: You have high risk of Lung cancer")
        elif(predict_stroke==0):
            st.success("Outcome: You do not have risk of Lung cancer")
