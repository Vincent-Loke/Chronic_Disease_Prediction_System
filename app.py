#--------------------------------------------------------------------------------------------------------------------------------------------------#
####################################################################################################################################################
# Execution of all pages for streamlit                                                                                                             #
# Developer Name: Loke Weng Khay                                                                                                                   #
####################################################################################################################################################
#--------------------------------------------------------------------------------------------------------------------------------------------------#
import streamlit as st

# import all pages
from predict_stroke_page import show_predict_stroke_page
from predict_lung_cancer_page import show_predict_lung_cancer_page
from predict_heart_disease_page import show_predict_heart_disease_page
from Chronic_Diseases import chronic_disease_page,lung_cancer_analysis_page,stroke_analysis_page,heart_disease_analysis_page

page = st.sidebar.selectbox("Explore Different Chronic Disease Prediction System",("Chronic Diseases","Analysis of Lung Cancer","Analysis of Stroke","Analysis of Heart Disease","Predict Lung Cancer","Predict Stroke","Predict Heart Disease"))

# selection page
if page == "Chronic Diseases":
    chronic_disease_page()
elif page == "Analysis of Lung Cancer":
    lung_cancer_analysis_page()
elif page == "Analysis of Stroke":
    stroke_analysis_page()
elif page == "Analysis of Heart Disease":
    heart_disease_analysis_page()
elif page == "Predict Lung Cancer":
    show_predict_lung_cancer_page()
elif page == "Predict Stroke":
    show_predict_stroke_page()
elif page == "Predict Heart Disease":
    show_predict_heart_disease_page()


