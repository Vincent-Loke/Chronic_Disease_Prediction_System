import streamlit as st
import pandas as pd
import altair as alt
from PIL import Image
import numpy as np
from sklearn.impute import KNNImputer
import matplotlib.pyplot as plt
import seaborn as sns

tabacco_image = Image.open('tobacco_use.jpg')
poor_nutrition_image = Image.open('poor_nutrition.jpg')
physical_activity_image = Image.open('physical_activity.jpg')
alcohol_image = Image.open('alcohol.jpg')
lung_cancer_tumor_image = Image.open('lung_cancer_tumor.jpg')
stroke_image = Image.open('stroke.png')
heart_disease_image = Image.open('heart_disease.jpg')

#--------------------------------------------------------------------------------------------------------------------------------------------------#
####################################################################################################################################################
# Chronic Disease Page                                                                                                                             #
# Developer Name: Loke Weng Khay                                                                                                                   #
####################################################################################################################################################
#--------------------------------------------------------------------------------------------------------------------------------------------------#
def chronic_disease_page():
    st.title("Chronic Diseases")
    st.write("Chronic disease is one of the most common illnesses that affect millions of people around the world. " +
    "This is because, based on a report by World Health Organization, it is estimated that NonCommunicable diseases (NCD), "+ 
    "which are known as Chronic diseases, have accounted for nearly 41 million deaths every year, which represents almost " +
    "71 % of all death globally (Noncommunicable Diseases, 2021).")
    
    st.subheader("Top 3 Chronic Diseases")
    st.markdown("<h4 style='text-align: left; color: white;'>Lung Cancer</h4>", unsafe_allow_html=True)
    with st.container():
        text_col, image_col = st.columns((1,1))
        with text_col:
            st.write("Lung Cancer is the third most common type of cancer and represents the leading cause of " +
                    "death in 2020 based on the World Health Organisation (Cancer, 2022). Lung Cancer happens " +
                    "when cells in the lung are divided uncontrollably, causing a mass or tumour to grow. The life " +
                    "cycle of a cell usually will die at a particular stage to prevent build-up in too many cells in the " +
                    "body (Fred Aleskerov, 2022). But when the cells start to grow too quickly, without dying off, " +
                    "that is where the problem arises.")
        with image_col:
            st.image(lung_cancer_tumor_image,width=350)

    st.write("Based on this, researchers were able to determine the two types " +
            "of lung carcinoma, which are small cell lung cancer (SCLC) and non-small cell lung cancer " +
            "(NSCLC) (Altarawneh, n.d.). SCLC usually represents 13% of lung cancer in the United States, " +
            "while NSCLC represents the rest with 84% of lung cancer in the United States. SCLC is " +
            "deathlier than NSCLC type because SCLC has a higher possibility of spreading to other organs " +
            "(Davis, 2020). This can be fatal if left untreated because cancer spreading uncontrollably to other " +
            "organs can reduce the life expectancy of the patient.")
    

    st.markdown("<h4 style='text-align: left; color: white;'>Stroke</h4>", unsafe_allow_html=True)
    with st.container():
        text_col, image_col = st.columns((1,1))
        with text_col:
            st.write("Strokes occur when a blockage or rupture of blood vessels happens in the brain. This is where some part " +
                    "of the brain is not getting enough blood supply. This causes part of the brain to be damaged or " +
                    "die due to lack of oxygen to the brain. If the patient does not seek treatment, the patient may " +
                    "suffer long-term brain damage, disability, or even death (Setyopranoto et al., 2022). This is " +
                    "important because the brain controls thoughts, actions, and other day-to-day operations. ")
        with image_col:
            st.image(stroke_image,width=300)

    st.write("Based on World Health Organisation, stroke is another chronic disease that is quickly " +
            "growing in the 21st century. It represents the second leading death and the third leading cause of " +
            "disability globally (Dr Poonam Khetrapal Singh, 2021). It is expected that one in four people is " +
            "in danger of having a stroke in their lifetime (Dr Poonam Khetrapal Singh, 2021). Based " +
            "on research, there are two types of stroke which are Ischemic stroke and Hemorrhagic stroke " +
            "(Perna & Temple, 2015). Most strokes are ischemic strokes as it occurs due to blood clot in the " +
            "blood vessels, while Hemorrhagic stroke happens when the blood vessel ruptures and leaks blood " +
            "in the brain (Perna & Temple, 2015).")

    st.markdown("<h4 style='text-align: left; color: white;'>Heart Disease</h4>", unsafe_allow_html=True)
    with st.container():
        text_col, image_col = st.columns((1,1))
        with text_col:
            st.write("Based on the Centres for Disease Control and Prevention (CDC), heart disease is the leading " +
                    "cause of death in the United States. Based on their research, about 697,000 people died in the " +
                    "United States from heart disease in 2020 (Heart Disease Facts, 2022). The term “heart disease” " +
                    "refers to any condition or disease that affects the cardiovascular system, such as blood vessels " +
                    "and the heart. There are many different types of heart diseases.")
        with image_col:
            st.image(heart_disease_image,width=300)
    st.markdown("""
                The following list are the types of heart diseases:
                - Coronary Artery Disease
                - Congenital Heart Defects
                - Arrhythmia
                - Dilated Cardiomyopathy
                - Myocardial Infarction
                - Heart Failure
                - Hypertrophic Cardiomyopathy
                - Mitral Valve Prolapse
                - Aortic Stenosis
                """)

    st.subheader("Causes of Chronic Diseases")
    st.write("Many chronic diseases are caused by :")
    st.write("<h4 color: white;'>1. Exercise tobacco use</h4>", unsafe_allow_html=True)
    st.image(tabacco_image)
    st.markdown("<h4 color: white;'>2. Poor Nutrition</h4>", unsafe_allow_html=True)
    st.image(poor_nutrition_image)
    st.markdown("<h4 color: white;'>3. Physical Inactivity</h4>", unsafe_allow_html=True)
    st.image(physical_activity_image)
    st.markdown("<h4 color: white;'>4. Excessive Alcohol Consumption</h4>", unsafe_allow_html=True)
    st.image(alcohol_image)
    
    st.write(" ")
    st.write(" ")
    st.subheader("References")
    st.write("1. Altarawneh, M. S. (n.d.). Lung Cancer Detection Using Image Processing Techniques Related papers. Retrieved July 25, 2022, from https://www.researchgate.net/publication/265998089")
    st.write("2. Cancer. (2022, February 3). World Health Organization. https://www.who.int/news-room/factsheets/detail/cancer")
    st.write("3. Davis, C. P. (2020). Small Cell Lung Cancer vs. Non-Small Cell Lung Cancer Stages & Survival Rate. Medicine Net. https://www.medicinenet.com/nonsmall_cell_lung_cancer_vs_small_cell/article.htm")
    st.write("4. Dr Poonam Khetrapal Singh. (2021). World Stroke Day. World Health Organization. https://www.who.int/southeastasia/news/detail/28-10-2021-world-stroke-day")
    st.write("5. Fred Aleskerov. (2022). Lung cancer: Symptoms, signs, stages, and more. Medical News Todays. https://www.medicalnewstoday.com/articles/323701")
    st.write("6. Heart Disease Facts. (2022). Cdc.Gov. https://www.cdc.gov/heartdisease/facts.htm")
    st.write("7. Noncommunicable diseases. (2021, April 13). https://www.who.int/news-room/factsheets/detail/noncommunicable-diseases")
    st.write("8. Perna, R., & Temple, J. (2015). Rehabilitation Outcomes: Ischemic versus Hemorrhagic Strokes. Behavioural Neurology, 2015. https://doi.org/10.1155/2015/891651")
    st.write("9. Setyopranoto, I., Upoyo, A. S., Isworo, A., Sari, Y., & Vidyanti, A. N. (2022). Awareness of Being at Risk of Stroke and Its Determinant Factors among Hypertensive Patients in " +
            "Banyumas, Indonesia. Stroke Research and Treatment, 2022. https://doi.org/10.1155/2022/4891134")

#--------------------------------------------------------------------------------------------------------------------------------------------------#
####################################################################################################################################################
# Function: Load Lung Cancer Dataset                                                                                                               #
# Developer Name: Loke Weng Khay                                                                                                                   #
####################################################################################################################################################
#--------------------------------------------------------------------------------------------------------------------------------------------------#
def load_lung_cancer_dataset():
    df1 = pd.read_csv('survey lung cancer.csv')
    df1 = df1.set_axis(['Gender', 'Age', 'Smoking', 'Yellow_Fingers', 'Anxiety',
                    'Peer_Pressure', 'Chronic_Disease', 'Fatigue', 'Allergy', 'Wheezing',
                    'Alcohol_Consumption', 'Coughing', 'Shortness_Of_Breath',
                    'Swallowing_Difficulty', 'Chest_Pain', 'Lung_Cancer'], axis=1)
    return df1

#--------------------------------------------------------------------------------------------------------------------------------------------------#
####################################################################################################################################################
# Function: Load Stroke Dataset                                                                                                                    #
# Developer Name: Loke Weng Khay                                                                                                                   #
####################################################################################################################################################
#--------------------------------------------------------------------------------------------------------------------------------------------------#
def load_stroke_dataset():
    df2 = pd.read_csv('healthcare-dataset-stroke-data.csv')

    df3=df2[(df2['gender']=='Male') | (df2['gender']=='Female')]
    del df3['id']

    df3['gender'] = df3['gender'].map(
        {'Female':1,'Male':0})

    df3['ever_married'] = df3['ever_married'].map(
        {'Yes':1,'No':0})

    df3['work_type'] = df3['work_type'].map(
        {'Never_worked':4,'children':3,'Govt_job':2,'Private':1,'Self-employed':0})

    df3['Residence_type'] = df3['Residence_type'].map(
        {'Urban':1,'Rural':0})

    df3['smoking_status'] = df3['smoking_status'].map(
                    {'Unknown':3,'formerly smoked':2,'smokes':1 ,'never smoked':0})

    imputer = KNNImputer(n_neighbors=5)
    df3 = pd.DataFrame(imputer.fit_transform(df3),columns = df3.columns)

    return df3

#--------------------------------------------------------------------------------------------------------------------------------------------------#
####################################################################################################################################################
# Function: Load Heart Disease Dataset                                                                                                             #
# Developer Name: Loke Weng Khay                                                                                                                   #
####################################################################################################################################################
#--------------------------------------------------------------------------------------------------------------------------------------------------#
def load_heart_disease_dataset():
    
    df4 = pd.read_csv('heart.csv')
    df5 = pd.read_csv('heart2.csv')
    df5 = df5.set_axis(['Age', 'Sex', 'ChestPainType', 'RestingBP', 'Cholesterol',
          'FastingBS', 'RestingECG', 'MaxHR', 'ExerciseAngina', 'Oldpeak',
          'ST_Slope', 'CA', 'THAL','HeartDisease'], axis=1, inplace=False)

    del df5['CA']
    del df5['THAL']

    df5['Sex'] = df5['Sex'].map(
                   {1:'M' ,0:'F'})

    df5['ChestPainType'] = df5['ChestPainType'].map(
                    {0:'TA', 1:'ATA' ,2:'NAP',3:'ASY'})

    df5['RestingECG'] = df5['RestingECG'].map(
                    {0:'Normal' ,1:'ST',2:'LVH'})

    df5['ExerciseAngina'] = df5['ExerciseAngina'].map(
                    {0:'N' ,1:'Y'})

    df5['ST_Slope'] = df5['ST_Slope'].map(
                    {0:'Up' ,1:'Flat',2:'Down'})

    df6 = df4.append(df5)

    df6 = df6.drop_duplicates(keep='first')

    df6['Sex'] = df6['Sex'].map(
                   {'M':1 ,'F':2})

    df6['ChestPainType'] = df6['ChestPainType'].map(
                    {'ATA':1 ,'NAP':2,'ASY':3,'TA':4})

    df6['RestingECG'] = df6['RestingECG'].map(
                    {'Normal':1 ,'ST':2,'LVH':3})

    df6['ExerciseAngina'] = df6['ExerciseAngina'].map(
                    {'N':1 ,'Y':2})

    df6['ST_Slope'] = df6['ST_Slope'].map(
                    {'Up':1 ,'Flat':2,'Down':3})

    df6['Cholesterol']=df6['Cholesterol'].replace(0, np.nan)
    imputer = KNNImputer(n_neighbors=5)
    df6 = pd.DataFrame(imputer.fit_transform(df6),columns = df6.columns)     

    df6.Oldpeak[df6.Oldpeak <0] = 0  
    return df6

#--------------------------------------------------------------------------------------------------------------------------------------------------#
####################################################################################################################################################
# Lung Cancer Analysis Page                                                                                                                        #
# Developer Name: Loke Weng Khay                                                                                                                   #
####################################################################################################################################################
#--------------------------------------------------------------------------------------------------------------------------------------------------#

def lung_cancer_analysis_page():
    df1 = load_lung_cancer_dataset()
    st.title("Analysis of Lung Cancer")

    # Bar Chart 1: Lung Cancer based on Age
    chart_data = df1[["Age","Lung_Cancer"]]
    chart_data['Lung_Cancer'] = chart_data['Lung_Cancer'].map(
                        {"YES":"Lung_Cancer" ,"NO":"No Lung Cancer"})
    color1 = ["orange", "green"]
    box_plot = alt.Chart(chart_data,title = "Age Boxplot").mark_boxplot(extent='min-max').encode(
        x="Age",
        y="Lung_Cancer",
        color=alt.Color("Lung_Cancer", scale=alt.Scale(range=color1))
    ).configure_axisX(labelAngle=0)
    st.altair_chart(box_plot, use_container_width=True)

    st.info("Analysis 1: Based on the figure above, it represents Lung Cancer based on Age in a box plot based on the dataset provided. " +
    "Based on the graph, it can be seen that the common age of the patient that has lung cancer are between 58 years old to 69 years old with " +
    "62.5 years old being the median age. There are some reports of a patient in their 40s being diagnosed with lung cancer, but it is not common. " +
    "The highest age for a patient diagnosed with lung cancer currently stands at 81 years old.")
    st.write("")
    st.write("")

    # Bar Chart 2: Lung Cancer based on Gender
    chart_data1 = df1[["Gender","Lung_Cancer"]]
    chart_data1['Lung_Cancer'] = chart_data1['Lung_Cancer'].map(
                   {"YES":"Lung_Cancer" ,"NO":"No Lung Cancer"})
    chart_data1['Gender'] = chart_data1['Gender'].map(
                   {"M":"Male" ,"F":"Female"})

    bar_chart1 = alt.Chart(chart_data1,title="Lung Cancer based on Gender").mark_bar().encode(
        x='Gender',
        y="count(Gender):Q",
        color=alt.Color("Lung_Cancer", scale=alt.Scale(range=color1)),
    )

    bar_chart1_text = alt.Chart(chart_data1).mark_text(align='center',baseline='top', color='black',dx = 0, fontSize = 13,dy = 3).encode(
        x=alt.X('Gender'),
        y=alt.Y('count(Gender):Q', stack='zero'),
        detail='Lung_Cancer',
        text=alt.Text('count(Gender):Q') 
    )

    final_bar_chart1 = alt.layer(bar_chart1, bar_chart1_text).configure_axisX(labelAngle=0)
    st.altair_chart(final_bar_chart1, use_container_width=True)

    st.info("Analysis 2: Based on the figure above, it represents Lung Cancer based on the Gender in a bar chart based on the lung cancer dataset provided. " +
    "Based on the bar chart, it can be seen that men patients have a higher possibility of getting lung cancer compared to female patients. Many factors cause " +
    "this observation to happen, where it includes several internal and external factors that will have to be observed, such as occupation, age, etc. This is why " +
    "the following data visualization will help to understand why this observation happens where male patients have a higher possibility of lung cancer compared to " +
    "female patients")
    st.write("")
    st.write("")

    # Bar Chart 3: Lung Cancer based on Smoking Status
    chart_data2 = df1[["Smoking","Lung_Cancer"]]
    chart_data2['Lung_Cancer'] = chart_data2['Lung_Cancer'].map(
                   {"YES":"Lung_Cancer" ,"NO":"No Lung Cancer"})
    chart_data2['Smoking'] = chart_data2['Smoking'].map(
                   {2:"Yes" ,1:"No"})

    bar_chart2 = alt.Chart(chart_data2,title="Lung Cancer based on Smoking Status").mark_bar().encode(
        x="Smoking",
        y="count(Smoking):Q",
        color=alt.Color("Lung_Cancer", scale=alt.Scale(range=color1))
    )

    bar_chart2_text = alt.Chart(chart_data2).mark_text(align='center',baseline='top', color='black',dx = 0, fontSize = 13,dy = 3).encode(
        x=alt.X('Smoking'),
        y=alt.Y('count(Smoking):Q', stack='zero'),
        detail='Lung_Cancer',
        text=alt.Text('count(Smoking):Q') 
    )
    final_bar_chart2 = alt.layer(bar_chart2, bar_chart2_text).configure_axisX(labelAngle=0)
    st.altair_chart(final_bar_chart2, use_container_width=True)

    st.info("Analysis 3: Based on the figure above, it represents Lung Cancer based on Smoking Status in a bar chart based on the dataset provided. " +
    "Based on the graph, it can be seen that patients that have smoked have a higher possibility of getting lung cancer compared to non-smoking patients. " +
    "There are reports of non-smoking patients with no smoking history but who are diagnosed with lung cancer. This can be due to secondhand smoking, " +
    "where the patient has a family member that chain-smokes under the same house.")
    st.write("")
    st.write("")

    # Bar Chart 4: Lung Cancer based on Yellow Fingers Status
    chart_data3 = df1[["Yellow_Fingers","Lung_Cancer"]]
    chart_data3['Lung_Cancer'] = chart_data3['Lung_Cancer'].map(
                   {"YES":"Lung_Cancer" ,"NO":"No Lung Cancer"})
    chart_data3['Yellow_Fingers'] = chart_data3['Yellow_Fingers'].map(
                   {2:"Yes" ,1:"No"})

    bar_chart3 = alt.Chart(chart_data3,title="Lung Cancer based on Yellow Fingers Status").mark_bar().encode(
        x="Yellow_Fingers",
        y="count(Yellow_Fingers):Q",
        color=alt.Color("Lung_Cancer", scale=alt.Scale(range=color1))
    )
    
    bar_chart3_text = alt.Chart(chart_data3).mark_text(align='center',baseline='top', color='black',dx = 0, fontSize = 13,dy = 3).encode(
        x=alt.X('Yellow_Fingers'),
        y=alt.Y('count(Yellow_Fingers):Q', stack='zero'),
        detail='Lung_Cancer',
        text=alt.Text('count(Yellow_Fingers):Q') 
    )
    final_bar_chart3 = alt.layer(bar_chart3, bar_chart3_text).configure_axisX(labelAngle=0)
    st.altair_chart(final_bar_chart3, use_container_width=True)
    
    st.info("Analysis 4: Based on the figure above, it represents Lung Cancer based on Yellow Finger Status in a bar chart based on the dataset provided. " +
    "Based on the graph, it can be seen that patients with yellow fingers contribute to the development of lung cancer compared to non-yellow finger patients. " +
    "The yellow finger is caused by excessive alcohol that leads to liver damage which explains the occurrence of yellow fingers.")
    st.write("")
    st.write("")

    # Bar Chart 5: Lung Cancer based on Anxiety Status
    chart_data4 = df1[["Anxiety","Lung_Cancer"]]
    chart_data4['Lung_Cancer'] = chart_data4['Lung_Cancer'].map(
                   {"YES":"Lung_Cancer" ,"NO":"No Lung Cancer"})
    chart_data4['Anxiety'] = chart_data4['Anxiety'].map(
                   {2:"Yes" ,1:"No"})
    bar_chart4 = alt.Chart(chart_data4,title="Lung Cancer based on Anxiety Status").mark_bar().encode(
        x="Anxiety",
        y="count(Anxiety):Q",
        color=alt.Color("Lung_Cancer", scale=alt.Scale(range=color1))
    )
    
    bar_chart4_text = alt.Chart(chart_data4).mark_text(align='center',baseline='top', color='black',dx = 0, fontSize = 13,dy = 3).encode(
        x=alt.X('Anxiety'),
        y=alt.Y('count(Anxiety):Q', stack='zero'),
        detail='Lung_Cancer',
        text=alt.Text('count(Anxiety):Q') 
    )
    final_bar_chart4 = alt.layer(bar_chart4, bar_chart4_text).configure_axisX(labelAngle=0)
    st.altair_chart(final_bar_chart4, use_container_width=True)

    st.info("Analysis 5: Based on the figure above, it represents Lung Cancer based on Anxiety Status in a bar chart based on the dataset provided. " +
    "Based on the graph, it can be seen that patients with anxiety does contribute in the development of lung cancer compared no anxiety patients. " + 
    "Anxiety is commonly associated with depression and stress, which can cause mental and physical health issues in patients.")
    st.write("")
    st.write("")

    # Bar Chart 6: Lung Cancer based on Peer Pressure Status
    chart_data5 = df1[["Peer_Pressure","Lung_Cancer"]]
    chart_data5['Lung_Cancer'] = chart_data5['Lung_Cancer'].map(
                   {"YES":"Lung_Cancer" ,"NO":"No Lung Cancer"})
    chart_data5['Peer_Pressure'] = chart_data5['Peer_Pressure'].map(
                   {2:"Yes" ,1:"No"})
    bar_chart5 = alt.Chart(chart_data5,title="Lung Cancer based on Peer Pressure Status").mark_bar().encode(
        x="Peer_Pressure",
        y="count(Peer_Pressure):Q",
        color=alt.Color("Lung_Cancer", scale=alt.Scale(range=color1))
    )
    
    bar_chart5_text = alt.Chart(chart_data5).mark_text(align='center',baseline='top', color='black',dx = 0, fontSize = 13,dy = 3).encode(
        x=alt.X('Peer_Pressure'),
        y=alt.Y('count(Peer_Pressure):Q', stack='zero'),
        detail='Lung_Cancer',
        text=alt.Text('count(Peer_Pressure):Q') 
    )
    final_bar_chart5 = alt.layer(bar_chart5, bar_chart5_text).configure_axisX(labelAngle=0)
    st.altair_chart(final_bar_chart5, use_container_width=True)

    st.info("Analysis 6: Based on the figure above, it represents Lung Cancer based on Peer Pressure Status in a bar chart based on the dataset provided. " +
    "Based on the graph, it can be seen that patients with peer pressure do contribute to the development of lung cancer compared to a patient with no peer pressure. " +
    "Peer Pressure is commonly associated with increased stress levels, anxiety, and sleep issues which can cause mental and physical health issues in patients.")
    st.write("")
    st.write("")

    # Bar Chart 7: Lung Cancer based on Chronic Disease Status
    chart_data6 = df1[["Chronic_Disease","Lung_Cancer"]]
    chart_data6['Lung_Cancer'] = chart_data6['Lung_Cancer'].map(
                   {"YES":"Lung_Cancer" ,"NO":"No Lung Cancer"})
    chart_data6['Chronic_Disease'] = chart_data6['Chronic_Disease'].map(
                   {2:"Yes" ,1:"No"})
    bar_chart6 = alt.Chart(chart_data6,title="Lung Cancer based on Chronic Disease Status").mark_bar().encode(
        x="Chronic_Disease",
        y="count(Chronic_Disease):Q",
        color=alt.Color("Lung_Cancer", scale=alt.Scale(range=color1))
    )
    
    bar_chart6_text = alt.Chart(chart_data6).mark_text(align='center',baseline='top', color='black',dx = 0, fontSize = 13,dy = 3).encode(
        x=alt.X('Chronic_Disease'),
        y=alt.Y('count(Chronic_Disease):Q', stack='zero'),
        detail='Lung_Cancer',
        text=alt.Text('count(Chronic_Disease):Q') 
    )
    final_bar_chart6 = alt.layer(bar_chart6, bar_chart6_text).configure_axisX(labelAngle=0)
    st.altair_chart(final_bar_chart6, use_container_width=True)

    st.info("Analysis 7: Based on the figure above, it represents Lung Cancer based on Chronic Disease Status in a bar chart based on the dataset provided. " +
    "Based on the graph, it can be seen that patients with chronic disease contribute in the development of lung cancer compared to patients with no chronic diseases. " +
    "Chronic Diseases can include stroke, cancer, and many more, which can affect the patient's overall health and reduce a person's lifespan.")
    st.write("")
    st.write("")

    # Bar Chart 8: Lung Cancer based on Fatigue Status
    chart_data7 = df1[["Fatigue","Lung_Cancer"]]
    chart_data7['Lung_Cancer'] = chart_data7['Lung_Cancer'].map(
                   {"YES":"Lung_Cancer" ,"NO":"No Lung Cancer"})
    chart_data7['Fatigue'] = chart_data7['Fatigue'].map(
                   {2:"Yes" ,1:"No"})
    bar_chart7 = alt.Chart(chart_data7,title="Lung Cancer based on Fatigue Status").mark_bar().encode(
        x="Fatigue",
        y="count(Fatigue):Q",
        color=alt.Color("Lung_Cancer", scale=alt.Scale(range=color1))
    )
    
    bar_chart7_text = alt.Chart(chart_data7).mark_text(align='center',baseline='top', color='black',dx = 0, fontSize = 13,dy = 3).encode(
        x=alt.X('Fatigue'),
        y=alt.Y('count(Fatigue):Q', stack='zero'),
        detail='Lung_Cancer',
        text=alt.Text('count(Fatigue):Q') 
    )
    final_bar_chart7 = alt.layer(bar_chart7, bar_chart7_text).configure_axisX(labelAngle=0)
    st.altair_chart(final_bar_chart7, use_container_width=True)

    st.info("Analysis 8: Based on the figure above, it represents Lung Cancer based on Fatigue Status in a bar chart based on the dataset provided. " +
    "Based on the graph, it can be seen that patients with fatigue contribute to the development of lung cancer compared to patients with no fatigue. " +
    "Fatigue is a feeling of constant tiredness or weakness and can be physical, mental, or a combination of both. It can affect anyone, and most adults " +
    "will experience fatigue at some point in their life.")
    st.write("")
    st.write("")

    # Bar Chart 9: Lung Cancer based on Allergy Status
    chart_data8 = df1[["Allergy","Lung_Cancer"]]
    chart_data8['Lung_Cancer'] = chart_data8['Lung_Cancer'].map(
                   {"YES":"Lung_Cancer" ,"NO":"No Lung Cancer"})
    chart_data8['Allergy'] = chart_data8['Allergy'].map(
                   {2:"Yes" ,1:"No"})
    bar_chart8 = alt.Chart(chart_data8,title="Lung Cancer based on Allergy Status").mark_bar().encode(
        x="Allergy",
        y=alt.Y("count(Allergy):Q",scale=alt.Scale(domain=(5, 200))),
        color=alt.Color("Lung_Cancer", scale=alt.Scale(range=color1))
    )
    
    bar_chart8_text = alt.Chart(chart_data8).mark_text(align='center',baseline='bottom', color='white',dx = 0, fontSize = 13,dy = -2).encode(
        x=alt.X('Allergy'),
        y=alt.Y('count(Allergy):Q', stack='zero'),
        detail='Lung_Cancer',
        text=alt.Text('count(Allergy):Q') 
    )
    final_bar_chart8 = alt.layer(bar_chart8, bar_chart8_text).configure_axisX(labelAngle=0)
    st.altair_chart(final_bar_chart8, use_container_width=True)

    st.info("Analysis 9: Based on the figure above, it represents Lung Cancer based on Allergy Status in a bar chart based on the dataset provided. " +
    "Based on the graph, it can be seen that patients with allergies contribute in the development of lung cancer compared to patients with no allergy. " +
    "An allergy occurs when a person reacts to substances in the environment that are harmless to most people. These substances are known as allergens and are " +
    "found in dust mites, pets, etc.")
    st.write("")
    st.write("")

    # Bar Chart 10: Lung Cancer based on Wheezing Status
    chart_data9 = df1[["Wheezing","Lung_Cancer"]]
    chart_data9['Lung_Cancer'] = chart_data9['Lung_Cancer'].map(
                   {"YES":"Lung_Cancer" ,"NO":"No Lung Cancer"})
    chart_data9['Wheezing'] = chart_data9['Wheezing'].map(
                   {2:"Yes" ,1:"No"})
    bar_chart9 = alt.Chart(chart_data9,title="Lung Cancer based on Wheezing Status").mark_bar().encode(
        x="Wheezing",
        y=alt.Y("count(Wheezing):Q",scale=alt.Scale(domain=(5, 200))),
        color=alt.Color("Lung_Cancer", scale=alt.Scale(range=color1))
    )
    
    bar_chart9_text = alt.Chart(chart_data9).mark_text(align='center',baseline='bottom', color='white',dx = 0, fontSize = 13,dy = -2).encode(
        x=alt.X('Wheezing'),
        y=alt.Y('count(Wheezing):Q', stack='zero'),
        detail='Lung_Cancer',
        text=alt.Text('count(Wheezing):Q') 
    )
    final_bar_chart9 = alt.layer(bar_chart9, bar_chart9_text).configure_axisX(labelAngle=0)
    st.altair_chart(final_bar_chart9, use_container_width=True)

    st.info("Analysis 10: Based on the figure above, it represents Lung Cancer based on Wheezing Status in a bar chart based on the dataset provided. " +
    "Based on the graph, it can be seen that patients with wheezing contribute in the development of lung cancer compared to patients with no wheezing. " +
    "Wheezing is a high-pitched whistling sound made while breathing. It's often associated with difficulty breathing.")
    st.write("")
    st.write("")

    # Bar Chart 11: Lung Cancer based on Alcohol Consumption Status
    chart_data10 = df1[["Alcohol_Consumption","Lung_Cancer"]]
    chart_data10['Lung_Cancer'] = chart_data10['Lung_Cancer'].map(
                   {"YES":"Lung_Cancer" ,"NO":"No Lung Cancer"})
    chart_data10['Alcohol_Consumption'] = chart_data10['Alcohol_Consumption'].map(
                   {2:"Yes" ,1:"No"})
    bar_chart10 = alt.Chart(chart_data10,title="Lung Cancer based on Alcohol Consumption Status").mark_bar().encode(
        x="Alcohol_Consumption",
        y=alt.Y("count(Alcohol_Consumption):Q",scale=alt.Scale(domain=(5, 200))),
        color=alt.Color("Lung_Cancer", scale=alt.Scale(range=color1))
    )
    
    bar_chart10_text = alt.Chart(chart_data10).mark_text(align='center',baseline='bottom', color='white',dx = 0, fontSize = 13,dy = -2).encode(
        x=alt.X('Alcohol_Consumption'),
        y=alt.Y('count(Alcohol_Consumption):Q', stack='zero'),
        detail='Lung_Cancer',
        text=alt.Text('count(Alcohol_Consumption):Q') 
    )
    final_bar_chart10 = alt.layer(bar_chart10, bar_chart10_text).configure_axisX(labelAngle=0)
    st.altair_chart(final_bar_chart10, use_container_width=True)

    st.info("Analysis 11: Based on the figure above, it represents Lung Cancer based on Alcohol Consumption Status in a bar chart based on the dataset provided. " +
    "Based on the graph, it can be seen that patients with alcohol consumption contributes to the development of lung cancer compared to patients with no alcohol consumption. " +
    "High Consumption of alcohol can lead to the development of chronic diseases and other severe problems, including High blood pressure, heart disease, stroke, " +
    "liver disease, and digestive issues.")
    st.write("")
    st.write("")

    # Bar Chart 12: Lung Cancer based on Coughing Status
    chart_data11 = df1[["Coughing","Lung_Cancer"]]
    chart_data11['Lung_Cancer'] = chart_data11['Lung_Cancer'].map(
                   {"YES":"Lung_Cancer" ,"NO":"No Lung Cancer"})
    chart_data11['Coughing'] = chart_data11['Coughing'].map(
                   {2:"Yes" ,1:"No"})
    bar_chart11 = alt.Chart(chart_data11,title="Lung Cancer based on Coughing Status").mark_bar().encode(
        x="Coughing",
        y=alt.Y("count(Coughing):Q",scale=alt.Scale(domain=(5, 200))),
        color=alt.Color("Lung_Cancer", scale=alt.Scale(range=color1))
    )
    
    bar_chart11_text = alt.Chart(chart_data11).mark_text(align='center',baseline='bottom', color='white',dx = 0, fontSize = 13,dy = -2).encode(
        x=alt.X('Coughing'),
        y=alt.Y('count(Coughing):Q', stack='zero'),
        detail='Lung_Cancer',
        text=alt.Text('count(Coughing):Q') 
    )
    final_bar_chart11 = alt.layer(bar_chart11, bar_chart11_text).configure_axisX(labelAngle=0)
    st.altair_chart(final_bar_chart11, use_container_width=True)

    st.info("Analysis 12: Based on the figure above, it represents Lung Cancer based on Coughing Status in a bar chart based on the dataset provided. " +
    "Based on the graph, it can be seen that patients with coughing contribute in the development of lung cancer compared to patients with no coughing. " +
    "Excessive coughing can lead to chronic cough, where the patient will have a cough that doesn't go away after a few weeks.")
    st.write("")
    st.write("")

    # Bar Chart 13: Lung Cancer based on Shortness Of Breath Status
    chart_data12 = df1[["Shortness_Of_Breath","Lung_Cancer"]]
    chart_data12['Lung_Cancer'] = chart_data12['Lung_Cancer'].map(
                   {"YES":"Lung_Cancer" ,"NO":"No Lung Cancer"})
    chart_data12['Shortness_Of_Breath'] = chart_data12['Shortness_Of_Breath'].map(
                   {2:"Yes" ,1:"No"})
    bar_chart12 = alt.Chart(chart_data12,title="Lung Cancer based on Shortness Of Breath Status").mark_bar().encode(
        x="Shortness_Of_Breath",
        y="count(Shortness_Of_Breath):Q",
        color=alt.Color("Lung_Cancer", scale=alt.Scale(range=color1))
    )
    
    bar_chart12_text = alt.Chart(chart_data12).mark_text(align='center',baseline='top', color='black',dx = 0, fontSize = 13,dy = 3).encode(
        x=alt.X('Shortness_Of_Breath'),
        y=alt.Y('count(Shortness_Of_Breath):Q', stack='zero'),
        detail='Lung_Cancer',
        text=alt.Text('count(Shortness_Of_Breath):Q') 
    )
    final_bar_chart12 = alt.layer(bar_chart12, bar_chart12_text).configure_axisX(labelAngle=0)
    st.altair_chart(final_bar_chart12, use_container_width=True)

    st.info("Analysis 13: Based on the figure above, it represents Lung Cancer based on Shortness of Breath Status in a bar chart based on the dataset provided. " +
    "Based on the graph, it can be seen that patients with shortness of breath contribute to the development of lung cancer compared to patients with no shortness of breath. " +
    "Shortness of breath, known as dyspnea, is often described as an intense tightening in the chest, air hunger, difficulty breathing, breathlessness, or a feeling " +
    "of suffocation.")
    st.write("")
    st.write("")

    # Bar Chart 14: Lung Cancer based on Swallowing Difficulty Status
    chart_data13 = df1[["Swallowing_Difficulty","Lung_Cancer"]]
    chart_data13['Lung_Cancer'] = chart_data13['Lung_Cancer'].map(
                   {"YES":"Lung_Cancer" ,"NO":"No Lung Cancer"})
    chart_data13['Swallowing_Difficulty'] = chart_data13['Swallowing_Difficulty'].map(
                   {2:"Yes" ,1:"No"})
    bar_chart13 = alt.Chart(chart_data13,title="Lung Cancer based on Swallowing Difficulty Status").mark_bar().encode(
        x="Swallowing_Difficulty",
        y=alt.Y("count(Swallowing_Difficulty):Q",scale=alt.Scale(domain=(5, 200))),
        color=alt.Color("Lung_Cancer", scale=alt.Scale(range=color1))
    )
    
    bar_chart13_text = alt.Chart(chart_data13).mark_text(align='center',baseline='bottom', color='white',dx = 0, fontSize = 13,dy = -2).encode(
        x=alt.X('Swallowing_Difficulty'),
        y=alt.Y('count(Swallowing_Difficulty):Q', stack='zero'),
        detail='Lung_Cancer',
        text=alt.Text('count(Swallowing_Difficulty):Q') 
    )
    final_bar_chart13 = alt.layer(bar_chart13, bar_chart13_text).configure_axisX(labelAngle=0)
    st.altair_chart(final_bar_chart13, use_container_width=True)

    st.info("Analysis 14: Based on the figure above, it represents Lung Cancer based on Swallowing Difficulty Status in a bar chart based on the dataset provided. " +
    "Based on the graph, it can be seen that patients with swallowing difficulty contribute to the development of lung cancer compared to patients with no swallowing " + 
    "difficulty. Dysphagia or difficulty swallowing is a symptom of many different medical conditions, including nervous system and brain disorders, muscle disorders, " +
    "and physical blockages in the throat.")
    st.write("")
    st.write("")

    # Bar Chart 15: Lung Cancer based on Chest Pain Status
    chart_data14 = df1[["Chest_Pain","Lung_Cancer"]]
    chart_data14['Lung_Cancer'] = chart_data14['Lung_Cancer'].map(
                   {"YES":"Lung_Cancer" ,"NO":"No Lung Cancer"})
    chart_data14['Chest_Pain'] = chart_data14['Chest_Pain'].map(
                   {2:"Yes" ,1:"No"})
    bar_chart14 = alt.Chart(chart_data14,title="Lung Cancer based on Chest Pain Status").mark_bar().encode(
        x="Chest_Pain",
        y="count(Chest_Pain):Q",
        color=alt.Color("Lung_Cancer", scale=alt.Scale(range=color1))
    )
    
    bar_chart14_text = alt.Chart(chart_data14).mark_text(align='center',baseline='top', color='black',dx = 0, fontSize = 13,dy = 3).encode(
        x=alt.X('Chest_Pain'),
        y=alt.Y('count(Chest_Pain):Q', stack='zero'),
        detail='Lung_Cancer',
        text=alt.Text('count(Chest_Pain):Q') 
    )
    final_bar_chart14 = alt.layer(bar_chart14, bar_chart14_text).configure_axisX(labelAngle=0)
    st.altair_chart(final_bar_chart14, use_container_width=True)

    st.info("Analysis 15: Based on the figure above, it represents Lung Cancer based on Chest Pain Status in a bar chart based on the dataset provided. " +
    "Based on the graph, it can be seen that patients with chest pain contribute to the development of lung cancer compared to patients with no chest pain. " +
    "The most common causes of pleuritic chest pain are bacterial or viral infections, pulmonary embolism, and pneumothorax.")
    st.write("")
    st.write("")

#--------------------------------------------------------------------------------------------------------------------------------------------------#
####################################################################################################################################################
# Stroke Analysis Page
# Developer Name: Loke Weng Khay                                                                                                                   #
####################################################################################################################################################
#--------------------------------------------------------------------------------------------------------------------------------------------------#
def stroke_analysis_page():
    df2 =load_stroke_dataset()
    st.title("Analysis of Stroke")

    # Bar Chart 1: Stroke based on Age

    chart_data = df2[["age","stroke"]]
    chart_data['stroke'] = chart_data['stroke'].map(
                   {1:"Stroke" ,0:"No Stroke"})
    color2 = ["#90EE90", "#B22222"]
    box_plot = alt.Chart(chart_data,title = "Stroke based on Age Boxplot").mark_boxplot(extent='min-max').encode(
        x="age",
        y="stroke",
        color=alt.Color("stroke", scale=alt.Scale(range=color2))
    ).configure_axisX(labelAngle=0)
    st.altair_chart(box_plot, use_container_width=True)

    st.info("Analysis 1: Based on the figure above, it represents Stroke based on Age in a box plot based on the Stroke dataset provided. " +
    "Based on the box plot, it can be seen that the common age of a patient that has lung cancer is between 59 years old to 78 years old, with " +
    "71 years old being the median age. Age is the single most important risk factor for stroke. This is because as we get older, our arteries naturally " +
    "become narrower and more challenging. They are also more likely to become clogged with fatty material, known as atherosclerosis.")
    st.write("")
    st.write("")

    # Bar Chart 2: Stroke based on Gender Status
    chart_data3 = df2[["gender","stroke"]]
    chart_data3['gender'] = chart_data3['gender'].map(
                   {1:"Female" ,0:"Male"})
    chart_data3['stroke'] = chart_data3['stroke'].map(
                   {1:"Stroke" ,0:"No Stroke"})
    bar_chart3 = alt.Chart(chart_data3,title="Stroke based on Gender Status").mark_bar().encode(
        x="gender",
        y=alt.Y("count(gender):Q",scale=alt.Scale(domain=(5, 3500))),
        color=alt.Color("stroke", scale=alt.Scale(range=color2))
    )
    
    bar_chart3_text = alt.Chart(chart_data3).mark_text(align='center',baseline='bottom', color='brown',dx = 0, fontSize = 13,dy = -3).encode(
        x=alt.X('gender'),
        y=alt.Y('count(gender):Q', stack='zero'),
        detail='stroke',
        text=alt.Text('count(gender):Q') 
    )
    final_bar_chart3 = alt.layer(bar_chart3, bar_chart3_text).configure_axisX(labelAngle=0)
    st.altair_chart(final_bar_chart3, use_container_width=True)

    st.info("Analysis 2: Based on the figure above, it represents Stroke based on Gender in a bar chart based on the stroke dataset provided. " +
    "Based on the graph, it can be seen that the male or female patient has the same possibility of getting a stroke. A stroke occurs due to the " +
    "habit and lifestyle that is lived by the patients, which explains their current health condition. Without proper management and care of the patient's " +
    "health, there is a high risk of a stroke occurring. Many factors cause this observation to happen, where it includes several internal and external factors " +
    "that will have to be observed, such as occupation, age, etc. This is why the following data visualization will help to understand why this observation happens " +
    "where female patients have a higher possibility of stroke compared to male patients.")
    st.write("")
    st.write("")
    
    # Bar Chart 3: Stroke based on Hypertension Status
    chart_data4 = df2[["hypertension","stroke"]]
    chart_data4['stroke'] = chart_data4['stroke'].map(
                   {1:"Stroke" ,0:"No Stroke"})
    chart_data4['hypertension'] = chart_data4['hypertension'].map(
                   {1:"Yes" ,0:"No"})
    bar_chart4 = alt.Chart(chart_data4,title="Stroke based on Hypertension Status").mark_bar().encode(
        x="hypertension",
        y=alt.Y("count(gender):Q"),
        color=alt.Color("stroke", scale=alt.Scale(range=color2))
    )
    
    bar_chart4_text = alt.Chart(chart_data4).mark_text(align='center',baseline='bottom', color='brown',dx = 0, fontSize = 13,dy = -1).encode(
        x=alt.X('hypertension'),
        y=alt.Y('count(hypertension):Q', stack='zero'),
        detail='stroke',
        text=alt.Text('count(hypertension):Q') 
    )
    final_bar_chart4 = alt.layer(bar_chart4, bar_chart4_text).configure_axisX(labelAngle=0)
    st.altair_chart(final_bar_chart4, use_container_width=True)

    st.info("Analysis 3: Based on the figure above, it represents Stroke based on Hypertension Status in a bar chart based on the dataset provided. " +
    "Based on the graph, it can be seen that patients with hypertension do not contribute much to the development of stroke compared to patients with no " +
    "hypertension. But due to the imbalanced dataset, more research has to be done to understand the relationship between hypertension and stroke and their associations.")
    st.write("")
    st.write("")

    # Bar Chart 4: Stroke based on Heart Disease Status
    chart_data5 = df2[["heart_disease","stroke"]]
    chart_data5['stroke'] = chart_data5['stroke'].map(
                   {1:"Stroke" ,0:"No Stroke"})
    chart_data5['heart_disease'] = chart_data5['heart_disease'].map(
                   {1:"Yes" ,0:"No"})
    bar_chart5 = alt.Chart(chart_data5,title="Stroke based on Heart Disease Status").mark_bar().encode(
        x = alt.X("heart_disease"),
        y = alt.Y("count(heart_disease):Q",scale=alt.Scale(domain=(5, 5500))),
        color=alt.Color("stroke", scale=alt.Scale(range=color2))
    )
    
    bar_chart5_text = alt.Chart(chart_data5).mark_text(align='center',baseline='bottom', color='brown',dx = 0, fontSize = 11,dy = 0).encode(
        x=alt.X('heart_disease'),
        y=alt.Y('count(heart_disease):Q', stack='zero'),
        detail='stroke',
        text=alt.Text('count(heart_disease):Q') 
    )
    final_bar_chart5 = alt.layer(bar_chart5, bar_chart5_text).configure_axisX(labelAngle=0)
    st.altair_chart(final_bar_chart5, use_container_width=True)

    st.info("Analysis 4: Based on the figure above, it represents Stroke based on Heart Disease Status in a bar chart based on the dataset provided. " +
    "Based on the graph, it can be seen that patients with heart disease do not contribute much in the development of stroke compared to patients with no " +
    "heart disease. But due to the imbalanced dataset, more research has to be done to understand the relationship between Heart Disease and stroke and their associations.")
    st.write("")
    st.write("")

    # Bar Chart 5: Stroke based on Marriage Status
    chart_data6 = df2[["ever_married","stroke"]]
    chart_data6['ever_married'] = chart_data6['ever_married'].map(
                   {1:"Yes" ,0:"No"})
    chart_data6['stroke'] = chart_data6['stroke'].map(
                   {1:"Stroke" ,0:"No Stroke"})
    bar_chart6 = alt.Chart(chart_data6,title="Stroke based on Marriage Status").mark_bar().encode(
        x="ever_married",
        y=alt.Y("count(ever_married):Q",scale=alt.Scale(domain=(5, 4000))),
        color=alt.Color("stroke", scale=alt.Scale(range=color2))
    )
    
    bar_chart6_text = alt.Chart(chart_data6).mark_text(align='center',baseline='bottom', color='brown',dx = 0, fontSize = 13,dy = -2).encode(
        x=alt.X('ever_married'),
        y=alt.Y('count(ever_married):Q', stack='zero'),
        detail='stroke',
        text=alt.Text('count(ever_married):Q') 
    )
    final_bar_chart6 = alt.layer(bar_chart6, bar_chart6_text).configure_axisX(labelAngle=0)
    st.altair_chart(final_bar_chart6, use_container_width=True)

    st.info("Analysis 5: Based on the figure above, it represents Stroke based on Marriage Status in a bar chart based on the dataset provided. " +
    "Based on the graph, it can be seen that married patients contribute to the development of stroke compared to patients that did not ever get married. " +
    "This can indicate that married patients have more responsibility and stress when it comes to managing and taking care of the family.")
    st.write("")
    st.write("")

    # Bar Chart 6: Stroke Based on Work Type
    chart_data7 = df2[["work_type","stroke"]]
    chart_data7['work_type'] = chart_data7['work_type'].map(
                    {4:'Never_worked',3:'children',2:'Govt_job',1:'Private',0:'Self-employed'})
    chart_data7['stroke'] = chart_data7['stroke'].map(
                   {1:"Stroke" ,0:"No Stroke"})
    bar_chart7 = alt.Chart(chart_data7,title="Stroke based on Work Type").mark_bar().encode(
        x="work_type",
        y=alt.Y("count(work_type):Q",scale=alt.Scale(domain=(5, 3500))),
        color=alt.Color("stroke", scale=alt.Scale(range=color2))
    )
    
    bar_chart7_text = alt.Chart(chart_data7).mark_text(align='center',baseline='bottom', color='brown',dx = 0, fontSize = 13,dy = -2).encode(
        x=alt.X('work_type'),
        y=alt.Y('count(work_type):Q', stack='zero'),
        detail='stroke',
        text=alt.Text('count(work_type):Q') 
    )
    final_bar_chart7 = alt.layer(bar_chart7, bar_chart7_text).configure_axisX(labelAngle=0)
    st.altair_chart(final_bar_chart7, use_container_width=True)

    st.info("Analysis 6: Based on the figure above, it represents Stroke based on Work Type in a bar chart based on the dataset provided. " +
    "Based on the graph, it can be seen that patients that work in private cooperation or are self-employed have the highest possibility of contributing " +
    "to the development of stroke. Patients who work in government sectors never worked or are children themselves have the lowest probability of getting a stroke. " +
    "This can indicate that private institutions and self-startup employees had to face poor management, demanding and stressful tasks, or long hours which led to " +
    "serious health consequences.")
    st.write("")
    st.write("")

    # Bar Chart 7: Stroke based on Residence Type
    chart_data8 = df2[["Residence_type","stroke"]]
    chart_data8['Residence_type'] = chart_data8['Residence_type'].map(
                    {1:'Urban',0:'Rural'})
    chart_data8['stroke'] = chart_data8['stroke'].map(
                   {1:"Stroke" ,0:"No Stroke"})
    bar_chart8 = alt.Chart(chart_data8,title="Stroke based on Residence Type").mark_bar().encode(
        x="Residence_type",
        y=alt.Y("count(Residence_type):Q",scale=alt.Scale(domain=(5, 3000))),
        color=alt.Color("stroke", scale=alt.Scale(range=color2))
    )
    
    bar_chart8_text = alt.Chart(chart_data8).mark_text(align='center',baseline='bottom', color='brown',dx = 0, fontSize = 13,dy = -2).encode(
        x=alt.X('Residence_type'),
        y=alt.Y('count(Residence_type):Q', stack='zero'),
        detail='stroke',
        text=alt.Text('count(Residence_type):Q') 
    )
    final_bar_chart8 = alt.layer(bar_chart8, bar_chart8_text).configure_axisX(labelAngle=0)
    st.altair_chart(final_bar_chart8, use_container_width=True)

    st.info("Analysis 7: Based on the figure above, it represents Stroke based on Residence Type in a bar chart based on the dataset provided. " +
    "Based on the graph, it can be seen that patients who either work in rural or urban areas do not contribute much to the development of stroke in a patient. " +
    "Although due to the imbalanced dataset, more research has to be done to understand the relationship between Residence Type and stroke and its associations.")
    st.write("")
    st.write("")

    # Bar Chart 8: Stroke Based on Smoking Status
    chart_data9 = df2[["smoking_status","stroke"]]
    chart_data9['smoking_status'] = chart_data9['smoking_status'].map(
                   {3:'Unknown', 2:'formerly smoked', 1:'smokes', 0:'never smoked'})
    chart_data9['stroke'] = chart_data9['stroke'].map(
                   {1:"Stroke" ,0:"No Stroke"})
    bar_chart9 = alt.Chart(chart_data9,title="Stroke Based on Smoking Status").mark_bar().encode(
        x="smoking_status",
        y=alt.Y("count(smoking_status):Q",scale=alt.Scale(domain=(5, 2500))),
        color=alt.Color("stroke", scale=alt.Scale(range=color2))
    )

    bar_chart9_text = alt.Chart(chart_data9).mark_text(align='center',baseline='bottom', color='brown',dx = 0, fontSize = 13,dy = -2).encode(
        x=alt.X('smoking_status'),
        y=alt.Y('count(smoking_status):Q', stack='zero'),
        detail='stroke',
        text=alt.Text('count(smoking_status):Q') 
    )
    final_bar_chart9 = alt.layer(bar_chart9, bar_chart9_text).configure_axisX(labelAngle=0)
    st.altair_chart(final_bar_chart9, use_container_width=True)

    st.info("Analysis 8: Based on the figure above, it represents Stroke based on Smoking Status in a bar chart based on the dataset provided. " +
    "Based on the graph, it can be seen that patients who smoke, formerly smoked, or do not smoke at all, do not contribute much to the development of " +
    "stroke in the patient. Although due to the imbalanced dataset, more research has to be done to understand the relationship between smoking and stroke and its associations.")
    st.write("")
    st.write("")

    color3 = ["#B22222"]
    # Scatter Plot 1: Stroke Based on Age and BMI
    chart_data10 = df2[["age","bmi","stroke"]]
    chart_data11=chart_data10[(chart_data10['stroke']==1)]
    chart_data11['stroke'] = chart_data11['stroke'].map(
                   {1:"Stroke" ,0:"No Stroke"})
    scatter_chart = alt.Chart(chart_data11,title = "Stroke Based on Age and BMI").mark_point(filled=True).encode(
        x="age",
        y="bmi",
        color=alt.Color("stroke", scale=alt.Scale(range=color3))
    ).configure_axisX(labelAngle=0)
    st.altair_chart(scatter_chart, use_container_width=True)

    st.info("Analysis 9: Based on the figure above, it represents Stroke based on Age and BMI in a scatter plot based on the stroke dataset provided. " +
    "Based on the graph, it can be seen that patients with a stroke are more likely to have a higher BMI rating and are older in age. It can be seen that as " +
    "the patient ages and the BMI increases, the possibility of getting a stroke is more significant. This happens due to the unhealthy lifestyle lived by the patients. " +
    "It is recommended to perform regular exercise and reduce bad eating habits to improve the physical and mental health of the patients.")
    st.write("")
    st.write("")

#--------------------------------------------------------------------------------------------------------------------------------------------------#
####################################################################################################################################################
# Heart Disease Analysis Page                                                                                                                      #
# Developer Name: Loke Weng Khay                                                                                                                   #
####################################################################################################################################################
#--------------------------------------------------------------------------------------------------------------------------------------------------#

def heart_disease_analysis_page():
    df3 = load_heart_disease_dataset()

    st.title("Analysis of Heart Disease")
    color4 = ["orange", "green"]

    # Box Plot 1: Heart Disease Based on Age
    chart_data = df3[["Age","HeartDisease"]]
    chart_data['HeartDisease'] = chart_data['HeartDisease'].map(
                   {1:"Heart Disease" ,0:"No Heart Disease"})
    box_plot = alt.Chart(chart_data,title = "Age Boxplot").mark_boxplot(extent='min-max').encode(
        x="Age",
        y="HeartDisease",
        color=alt.Color("HeartDisease", scale=alt.Scale(range=color4))
    ).configure_axisX(labelAngle=0)
    st.altair_chart(box_plot, use_container_width=True)

    st.info("Analysis 1: Based on the figure above, it represents Heart Disease based on the Age in a box plot based on the heart disease dataset provided. " +
    "Based on the graph, it can be seen that the common age of a patient with heart disease are between 49 and 62 years old, with 56 year old being the median age. " +
    "There are reports of a patient at the age of 29 years old that has been diagnosed with heart disease, but it is not common. The highest age of a patient that has " +
    "been diagnosed with heart disease is 77 years old.")
    st.write("")
    st.write("")

    # Scatter Plot 1: Heart Disease Based on Age and Max Heart Rate
    chart_data2 = df3[["Age","MaxHR","HeartDisease"]]
    chart_data2['HeartDisease'] = chart_data2['HeartDisease'].map(
                   {1:"Heart Disease", 0:"No Heart Disease"})
    scatter_chart = alt.Chart(chart_data2,title = "Heart Disease Based on Age and Max Heart Rate").mark_point(filled=True).encode(
        x="Age",
        y="MaxHR",
        color=alt.Color("HeartDisease", scale=alt.Scale(range=color4))
    ).configure_axisX(labelAngle=0)
    st.altair_chart(scatter_chart, use_container_width=True)

    st.info("Analysis 2: Based on the figure above, it represents Heart Disease based on the Age and Max Heart Rate in a scatter plot based on the heart disease " + 
    "dataset provided. Based on the scatter plot, it can be seen that patient that has heart disease are more likely to have a lower maximum heart rate compared to " +
    "non-heart disease patient. Although it is common for the max heart rate to drop as the patient age, it is recommended to perform regular exercise to improve heart " +
    "activity.")
    st.write("")
    st.write("")

    # Bar Chart 2: Heart Disease based on Sex
    chart_data3 = df3[["Sex","HeartDisease"]]
    chart_data3['HeartDisease'] = chart_data3['HeartDisease'].map(
                   {1.0:"Heart Disease" ,0.0:"No Heart Disease"})
    chart_data3['Sex'] = chart_data3['Sex'].map(
                   {1:"Male" ,2:"Female"})

    bar_chart3 = alt.Chart(chart_data3,title = "Heart Disease Based on Sex").mark_bar().encode(
        x=alt.X("Sex"),
        y=alt.Y("count(Sex):Q"),
        color=alt.Color("HeartDisease", scale=alt.Scale(range=color4))
    )
    
    bar_chart3_text = alt.Chart(chart_data3).mark_text(align='center',baseline='top', color='white',dx = 0, fontSize = 13,dy = 3).encode(
        x=alt.X('Sex'),
        y=alt.Y('count(Sex):Q', stack='zero'),
        detail='HeartDisease',
        text=alt.Text('count(Sex):Q') 
    )
    final_bar_chart3 = alt.layer(bar_chart3, bar_chart3_text).configure_axisX(labelAngle=0)
    st.altair_chart(final_bar_chart3, use_container_width=True)

    st.info("Analysis 3: Based on the figure above, it represents Heart Disease based on Sex in a bar chart based on the heart disease dataset provided. " +
    "Based on the bar chart, it can be seen that male patients have a higher risk of getting heart disease compared to female patients. Many factors cause this " +
    "observation to happen, where it includes several internal and external factors that will have to be observed, such as occupation, age, etc. This is why the " +
    "following data visualization will help to understand why this observation happens where male patients have a higher possibility of heart disease compared to " +
    "female patients.")
    st.write("")
    st.write("")

    # Bar Chart 3: Heart Disease Based on ST Slope
    chart_data4 = df3[["ST_Slope","HeartDisease"]]
    chart_data4['HeartDisease'] = chart_data4['HeartDisease'].map(
                   {1.0:"Heart Disease" ,0.0:"No Heart Disease"})
    chart_data4['ST_Slope'] = chart_data4['ST_Slope'].map(
                   {1:"Upsloping" ,3:"Downsloping",2:"Flat"})

    bar_chart4 = alt.Chart(chart_data4,title = "Heart Disease Based on ST Slope").mark_bar().encode(
        x="ST_Slope",
        y="count(ST_Slope):Q",
        color=alt.Color("HeartDisease", scale=alt.Scale(range=color4))
    )
    
    bar_chart4_text = alt.Chart(chart_data4).mark_text(align='center',baseline='top', color='white',dx = 0, fontSize = 13,dy = 3).encode(
        x=alt.X('ST_Slope'),
        y=alt.Y('count(ST_Slope):Q', stack='zero'),
        detail='HeartDisease',
        text=alt.Text('count(ST_Slope):Q') 
    )
    final_bar_chart4 = alt.layer(bar_chart4, bar_chart4_text).configure_axisX(labelAngle=0)
    st.altair_chart(final_bar_chart4, use_container_width=True)

    st.info("Analysis 4: Based on the figure above, it represents Heart Disease based on the type of ST Slope in a bar chart based on the heart disease dataset provided. " +
    "Based on the bar chart, it can be seen that the patients with heartbeats reporting upsloping charts in the EKG charts have a higher possibility of not getting heart " +
    "disease. In contrast, patients with heartbeats reporting flat and downsloping charts in the EKG have a higher probability of getting heart disease. It can be seen " +
    "that the most significant indicator of heart disease can be determined based on the EKG charts. When a patient shows signs of flatting or downsloping EKG charts, " +
    "it can indicate heart disease.")
    st.write("")
    st.write("")

    # Bar Chart 4: Heart Disease based on Fasting Blood Sugar Level
    chart_data5 = df3[["FastingBS","HeartDisease"]]
    chart_data5['HeartDisease'] = chart_data5['HeartDisease'].map(
                   {1:"Heart Disease", 0:"No Heart Disease"})
    chart_data5['FastingBS'] = chart_data5['FastingBS'].map(
                   {1:"More Than 120 mg/dl", 0:"Less Than 120 mg/dl"})
    bar_chart5 = alt.Chart(chart_data5,title = "Heart Disease Based on Fasting Blood Sugar Level").mark_bar().encode(
        x="FastingBS",
        y="count(FastingBS):Q",
        color=alt.Color("HeartDisease", scale=alt.Scale(range=color4))
    )
    
    bar_chart5_text = alt.Chart(chart_data5).mark_text(align='center', baseline='top', color='white',dx = 0, fontSize = 13,dy = 3).encode(
        x=alt.X('FastingBS'),
        y=alt.Y('count(FastingBS):Q', stack='zero'),
        detail='HeartDisease',
        text=alt.Text('count(FastingBS):Q') 
    )
    final_bar_chart5 = alt.layer(bar_chart5, bar_chart5_text).configure_axisX(labelAngle=0)
    st.altair_chart(final_bar_chart5, use_container_width=True)

    st.info("Analysis 5: Based on the figure above, it represents Heart Disease based on Fasting Blood Sugar in a bar chart based on the heart disease dataset provided. " +
    "Based on the graph, it can be seen that the patients with fasting blood sugar levels lower than 120mg/dl have a 50% possibility of getting heart disease. In contrast, " +
    "patients with fasting blood sugar levels of more than 120mg/dl have a 75% possibility of getting heart disease. This measures your blood sugar after an overnight fast " +
    "(not eating). A fasting blood sugar level of 99 mg/dL or lower is average, 100 mg/dl to 125 mg/dl indicates you have prediabetes, and 126 mg/dL or higher indicates " +
    "diabetes. This is important to help determine if the blood vessel is damaged due to high sugar levels in the blood vessels.")
    st.write("")
    st.write("")

    # Bar Chart 5: Heart Disease based on Chest Pain Type
    chart_data6 = df3[["ChestPainType","HeartDisease"]]
    chart_data6['HeartDisease'] = chart_data6['HeartDisease'].map(
                   {1:"Heart Disease" ,0:"No Heart Disease"})
    chart_data6['ChestPainType'] = chart_data6['ChestPainType'].map(
                   {3:"Asymptomatic" ,1:"Atypical Angina",2:"Non-Anginal Pain",4:"Typical Angina"})            
    bar_chart6 = alt.Chart(chart_data6,title = "Heart Disease Based on Chest Pain Type").mark_bar().encode(
        x="ChestPainType",
        y="count(ChestPainType):Q",
        color=alt.Color("HeartDisease", scale=alt.Scale(range=color4))
    )
    
    bar_chart6_text = alt.Chart(chart_data6).mark_text(align='center',baseline='top', color='white',dx = 0, fontSize = 13,dy = 3).encode(
        x=alt.X('ChestPainType'),
        y=alt.Y('count(ChestPainType):Q', stack='zero'),
        detail='HeartDisease',
        text=alt.Text('count(ChestPainType):Q') 
    )
    final_bar_chart6 = alt.layer(bar_chart6, bar_chart6_text).configure_axisX(labelAngle=0)
    st.altair_chart(final_bar_chart6, use_container_width=True)

    st.info("Analysis 6: Based on the figure above, it represents Heart Disease based on the Chest Pain Type in a bar chart based on the heart disease dataset provided. " +
    "Based on the graph, it can be seen that the patients with asymptomatic chest pain still have a 79% possibility of getting heart disease and patients with non-angina " +
    "chest pain still have a 50% possibility of getting heart disease. In comparison, patients with atypical angina and typical angina Chest Pain have the lowest probability " +
    "of getting heart disease, with 30% and 31%, respectively. Chest pain may be caused by angina or a heart attack. Other causes of chest pain can include indigestion, " +
    "reflux, muscle strain, inflammation in the rib joints near the breastbone, and shingles.")
    st.write("")
    st.write("")

    # Scatter Plot 2: Heart Disease based on Age and Cholesterol
    chart_data7 = df3[["Age","Cholesterol","HeartDisease"]]
    chart_data7['HeartDisease'] = chart_data7['HeartDisease'].map(
                   {1:"Heart Disease" ,0:"No Heart Disease"})

    scatter_chart2 = alt.Chart(chart_data7,title = "Heart Disease Based on Age and Cholesterol").mark_point(filled=True).encode(
        x="Age",
        y="Cholesterol",
        color=alt.Color("HeartDisease", scale=alt.Scale(range=color4))
    ).configure_axisX(labelAngle=0)
    st.altair_chart(scatter_chart2, use_container_width=True)

    st.info("Analysis 7: Based on the figure above, it represents Heart Disease based on Age and Cholesterol in a scatter plot based on the heart disease dataset provided. " +
    "Based on the scatter plot, it can be seen that the patients with higher cholesterol level combined with older age has the highest possibility of getting heart disease. " +
    "In comparison, patients with lower cholesterol levels and younger patients have the lowest probability of getting heart disease based on the data provided. " +
    "Your body needs cholesterol to build healthy cells. Still, high cholesterol levels can increase your risk of heart disease due to the build-up of fatty deposits, " +
    "causing difficult for enough blood to flow through your arteries.")
    st.write("")
    st.write("")
    
    # Boxplot 2: Resting Blood Pressure Boxplot
    chart_data9 = df3[["RestingBP","HeartDisease"]]
    chart_data9['HeartDisease'] = chart_data9['HeartDisease'].map(
                   {1:"Heart Disease" ,0:"No Heart Disease"})
    box_plot2 = alt.Chart(chart_data9,title = "Resting Blood Pressure Boxplot").mark_boxplot(extent='min-max').encode(
        x="RestingBP",
        y="HeartDisease",
        color=alt.Color("HeartDisease", scale=alt.Scale(range=color4))
    ).configure_axisX(labelAngle=0)
    st.altair_chart(box_plot2, use_container_width=True)

    st.info("Analysis 8: Based on the figure above, it represents Heart Disease based on Resting Blood Pressure in a box plot based on the heart disease dataset provided. "+
    "Based on the graph, it can be seen that patients with higher blood pressure are more likely to have heart disease. Based on the data, patients with heart disease has "+
    "a blood pressure between 120 to 142 with a median of 130. The maximum blood pressure for a patient with heart disease has reported of 200 for blood pressure. "+
    "High blood pressure can happen because of unhealthy lifestyle choices, such as not getting enough regular physical activity.")
    st.write("")
    st.write("")

    # Boxplot 3: Old Peak Boxplot
    chart_data10 = df3[["Oldpeak","HeartDisease"]]
    chart_data10['HeartDisease'] = chart_data10['HeartDisease'].map(
                   {1:"Heart Disease", 0:"No Heart Disease"})
    box_plot3 = alt.Chart(chart_data10,title = "Old Peak Boxplot").mark_boxplot(extent='min-max').encode(
        x="Oldpeak",
        y="HeartDisease",
        color=alt.Color("HeartDisease", scale=alt.Scale(range=color4))
    ).configure_axisX(labelAngle=0)
    st.altair_chart(box_plot3, use_container_width=True)

    st.info("Analysis 9: Based on the figure above, it represents Heart Disease based on the Old Peak in a box plot based on the heart disease dataset provided. "+
    "Based on the graph, it can be seen that heart disease patients have old peak ratings between 0 to 1.9, with 1 being the median old peak rating. At the same "+
    "time, non-heart disease patients have a rating between 0 to 1.2, with 0.1 being the median old peak rating.")
    st.write("")
    st.write("")

    # Scatter Plot 3: Heart Disease based on Age and Cholesterol
    chart_data11 = df3[["Age","RestingBP","HeartDisease"]]
    chart_data11['HeartDisease'] = chart_data11['HeartDisease'].map(
                   {1:"Heart Disease" ,0:"No Heart Disease"})

    scatter_chart3 = alt.Chart(chart_data11,title = "Heart Disease Based on Age and Resting Blood Pressure").mark_point(filled=True).encode(
        x="Age",
        y="RestingBP",
        color=alt.Color("HeartDisease", scale=alt.Scale(range=color4))
    ).configure_axisX(labelAngle=0)
    st.altair_chart(scatter_chart3, use_container_width=True)

    st.info("Analysis 10: Based on the figure above, it represents Heart Disease based on Age and Resting Blood Pressure in a scatter plot based on the dataset provided. " +
    "Based on the graph, it can be seen that the patients with higher resting blood pressure level combined with old age has the highest possibility of getting heart disease. "+
    "In comparison, patients with lower resting blood pressure levels and younger patients have the lowest probability of getting heart disease.")
    st.write("")
    st.write("")

    chart_data12 = df3[["Cholesterol","HeartDisease"]]
    chart_data12['HeartDisease'] = chart_data12['HeartDisease'].map(
                   {1:"Heart Disease" ,0:"No Heart Disease"})
    box_plot4 = alt.Chart(chart_data12,title = "Cholesterol Boxplot").mark_boxplot(extent='min-max').encode(
        x="Cholesterol",
        y="HeartDisease",
        color=alt.Color("HeartDisease", scale=alt.Scale(range=color4))
    ).configure_axisX(labelAngle=0)
    st.altair_chart(box_plot4, use_container_width=True)

    st.info("Analysis 11: Based on the figure above, it represents Heart Disease based on the Cholesterol in a box plot based on the heart disease dataset provided. "+
    "Based on the box plot, it can be seen that patients with heart disease have reported higher cholesterol levels than non-heart disease patients. It can be seen "+
    "that heart disease patients reported cholesterol levels between 214 to 274, with the median being 242. In contrast, non-heart disease patients reported cholesterol "+
    "levels between 207 to 273, with the median being 236. High cholesterol levels can increase your risk of heart disease due to the build-up of fatty deposits, causing "+
    "difficult for enough blood to flow through your arteries.")
    st.write("")
    st.write("")

    
