import pandas as pd
import streamlit as st
import pickle
import time

st.set_page_config(
        page_title="A.I end sem project",
        page_icon="chart_with_upwards_trend",
        layout='centered',
    )
data=pd.read_csv('data.csv')
data.head()
st.title("A Cute House price predicator app")
st.write("Project by CSE dept: Purva, Mahir, Megha")
if st.button("Make happen a snow fall:)"): 
        st.snow()
st.write("")
st.write("")
st.write("")
st.write("Hi, this is dataframe from our dataset...")

         
st.write(data.head())
st.write("")
st.write("")
st.header("ML Models used with respective accuracy:")

col1, col2, col3 = st.columns(3)
col4, col5, col6 =st.columns(3)
col1.metric("Accuracy", "OLS", "77.23")
col2.metric("Accuracy", "Lasso", "77.33")
col3.metric("Accuracy", "Ridge", "77.23")
col4.metric("Accuracy", "EN", "77.12")
col5.metric("Accuracy", "Bayesian", "77.13")
col6.metric("Accuracy", "RandomForest", "80.98")
st.write("")
st.write("")
st.write("")

st.subheader("$129,300")

st.area_chart(data,x='LotArea',y='SalePrice')

#['LotArea', 'MasVnrArea', 'TotalBsmtSF', '1stFlrSF', 'GrLivArea','GarageArea', 'SalePrice']
d_lotarea=int(data['LotArea'].mean())

def predict_price(LotArea,MasVnrArea,TotalBsmtSF,f1stFlrSF,GrLivArea,GarageArea,model_name):
        #'Linear','Bayesian','Lasso','Ridge','RandomForest','ElasticNet'
        if(model_name == 'Linear'):
                model=pickle.load(open('ols2.pickle','rb'))
        elif(model_name == 'Bayesian'):
                model=pickle.load(open('bayesian.pickle','rb'))
        elif(model_name == 'Lasso'):
                model=pickle.load(open('lasso.pickle','rb'))
        elif(model_name == 'Ridge'):
                model=pickle.load(open('ridge.pickle','rb'))
        elif(model_name == 'RandomForest'):
                model=pickle.load(open('rf.pickle','rb'))
        elif(model_name == 'ElasticNet'):
                model=pickle.load(open('en.pickle','rb'))
        
        #model=pickle.load(open('ols2.pickle','rb'))
        ans=model.predict([[LotArea,MasVnrArea,TotalBsmtSF,f1stFlrSF,GrLivArea,GarageArea]])
        st.write("")
        st.subheader("Processing inputs...")
        progress=st.progress(0)
        for i in range(100):
                time.sleep(0.01)
                progress.progress(i+1)
        st.balloons()
        


        print(ans)
        ans=float(ans)
        st.subheader('$'+str(round(ans,3)))
        global price 
        price=round(ans,3)

st.info('This data takes input in the form of sqfts', icon="ℹ️")
LotArea=st.slider('Select Lot area', int(data['LotArea'].min()), int(data['LotArea'].max()), value=int(data['LotArea'].mean()))
MasVnrArea=st.slider('Select MasVnrArea', int(data['MasVnrArea'].min()), int(data['MasVnrArea'].max()), value=int(data['MasVnrArea'].mean()))
TotalBsmtSF=st.slider('Select Total basement size', int(data['TotalBsmtSF'].min()), int(data['TotalBsmtSF'].max()), value=int(data['TotalBsmtSF'].mean()))
f1stFlrSF=st.slider('Select 1st floor sqft', int(data['1stFlrSF'].min()), int(data['1stFlrSF'].max()), value=int(data['1stFlrSF'].mean()))
GrLivArea=st.slider('Select Ground Living Area', int(data['GrLivArea'].min()), int(data['GrLivArea'].max()), value=int(data['GrLivArea'].mean()))
GarageArea=st.slider('Select GarageArea', int(data['GarageArea'].min()), int(data['GarageArea'].max()), value=int(data['GarageArea'].mean()))


model=st.selectbox("Choose a model for prediction...",('Linear','Bayesian','Lasso','Ridge','RandomForest','ElasticNet'),index=4)



if st.button("Predict the price"):   
        output = predict_price(LotArea,MasVnrArea,TotalBsmtSF,f1stFlrSF,GrLivArea,GarageArea,model)
        st.success('Property price after 7yrs: "${}" at 5.1% annual growth '.format(round(price+(7*(5*price/100))),2))#price + 7yr x 5% of price
        st.write("")
        st.write("")
