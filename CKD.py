import pickle
import streamlit as st

pickle_in = open("ModelSVM","rb")
Classifier = pickle.load(pickle_in)

expander = st.beta_expander("ABOUT THE PROJECT")
expander.write("This project predicts that the User has Chronic kidney disease are not")
expander.write("The project builds on M.L techniques(Uisng SVM)")
expander.write("We used Streamlit,numpy,pandas,pickle....ETC packages for the project")

try:
  def Predict_authentication(AGE,BP,SG,AL,SU,RBC,PCC,BA,BGR,BU,SOD,POT,HEMO,HTN,DM,CAD,APPET,PE,ANE):
    prediction = Classifier.predict([[AGE,BP,SG,AL,SU,RBC,PCC,BA,BGR,BU,SOD,POT,HEMO,HTN,DM,CAD,APPET,PE,ANE]])
    print(prediction)
    return prediction
  def main():
    html_temp = """
        <style>
         h2 {
        color: white; 
        text-align:center;
         }
        body{
         background-image: url("https://i.pinimg.com/originals/f4/52/a2/f452a2f4b634b3011e065da8eaf0a5c3.gif");  
         border-radius:25px 
         }
        </style>
        <body>
        <h2>Chronic Kidney Disease Prediction Application<h2>
        </body>
        """
    st.markdown(html_temp,unsafe_allow_html=True)
    if st.checkbox('AGREE TERMS AND CONDITIONS,[THIS WAS A PROTO TYPE]'):
         AGE = st.slider('Enter Age', 0.0, 100.0, 0.0)
         BP = st.slider('Enter Blood Pressure', 0.0, 150.0, 0.0)
         BGR = st.slider('Enter Blood Glucose Random', 0.0, 500.0, 0.0)
         BU = st.slider('Enter Blood Urea', 0.0, 400.0, 0.0)
         SOD = st.slider('Enter Sodium Value in body', 100.0, 200.0, 0.0)
         AL = st.select_slider('Enter Albumin Value in body', options=['0.0', '1.0','2.0','3.0','4.0','5.0'])
         SU = st.select_slider('Enter Sugar Value in body', options=['0.0', '1.0','2.0','3.0','4.0','5.0'])
         RBC = st.sidebar.selectbox("Red Blood Cells [Normal:'1',Abnormal:'0']",("1", "0"))
         PCC = st.sidebar.selectbox("Pus Cell Clumps[Notpresent:'1',Present:'0']",("1", "0"))
         BA = st.sidebar.selectbox("Bacteria [Notpresent:'1',Present:'0']",("1", "0"))
         APPET = st.sidebar.selectbox("Appetite [Poor:'1',Good:'0']",("1", "0"))
         PE = st.sidebar.selectbox("Pedal Edema [No:'1',Yes:'0']",("1", "0"))
         HEMO = st.slider('Enter Hemoglobin Value', 0.0, 20.0, 0.0)
         CAD = st.select_slider('Enter Coronary Artery Disease Value', options=['0.0', '1.0'])
         HTN = st.radio("Hypertension [Yes:'1',No:'0']",("1", "0"))
         ANE = st.radio("Anemia [No:'1',Yes:'0']",("1", "0"))
         DM = st.radio("Diabetes Mellitus [No:'1',Yes:'0']",("1", "0"))
         POT = st.text_input("Enter Potassium Value","")
         SG = st.text_input("Enter SG Value","")
         result=""
         if st.button('Predict'):
                  result = Predict_authentication(AGE,BP,SG,AL,SU,RBC,PCC,BA,BGR,BU,SOD,POT,HEMO,HTN,DM,CAD,APPET,PE,ANE)
         if (result==0):
                  st.success("Chance To Have Chronic Kidney Disease")
                  st.info('FOLLOW BELOW THINGS')
                  st.header("Be positive")
                  st.markdown("![Alt Text](https://media.giphy.com/media/ZB7bwN6w31hsiYsOmW/giphy.gif)")
         elif (result==1):
                  st.success("No Chance To Have Chronic Kidney Disease")
                  st.info('Be Happy')
                  st.markdown("![Alt Text](https://i.pinimg.com/originals/2e/e5/e8/2ee5e8254383e3003662f592a93a623d.gif)")
                  
  if __name__=='__main__':
   main()
except:
    st.error("Enter All Values Please")
    st.info('Referesh The APP') 

if st.button('About Me'):
  st.error('SANKARANA CHAKRADHAR NAIDU')
  st.info('B.TEC-VITAP UNIVERSITY')
  """Gmail:"""
  st.code('''chakradhar2307@gmail.com''')
  '''LinkedinID'''
  st.code('''https://www.linkedin.com/in/sankarana-chakradhar-naidu-75144b18b/''')
  st.success('HAPPY CODING \U0001F600 \U0001F600 \U0001F600')
  print('')
                        