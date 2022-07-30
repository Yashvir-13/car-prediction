import streamlit as st
import numpy as np
import pandas as pd
import home,data,plots,predict
st.set_page_config(page_title="Car price prediction",page_icon=":car:",layout="centered",initial_sidebar_state="auto")
words_dict = {"two": 2, "three": 3, "four": 4, "five": 5, "six": 6, "eight": 8, "twelve": 12}
def num_map(series):
    return series.map(words_dict)
@st.cache()
def load_dataset():
    df=pd.read_csv("car-prices.csv")
    df["car_company"]=pd.Series([i.split(" ")[0] for i in df["CarName"]])
    df.drop("CarName",inplace=True,axis=1)
    df.loc[(df['car_company'] == "vw") | (df['car_company'] == "vokswagen"), 'car_company'] = 'volkswagen'
    df.loc[df['car_company'] == "porcshce", 'car_company'] = 'porsche'
    df.loc[df['car_company'] == "toyouta", 'car_company'] = 'toyota'
    df.loc[df['car_company'] == "Nissan", 'car_company'] = 'nissan'
    df.loc[df['car_company'] == "maxda", 'car_company'] = 'mazda'
    df["doornumber"]=num_map(df["doornumber"])
    df["cylindernumber"]=num_map(df["cylindernumber"])
    df_cat=df.select_dtypes(include="object")
    df_dummy=pd.get_dummies(df_cat,drop_first=True,dtype="int64")
    df.drop(list(df_cat.columns),axis=1,inplace=True)
    df=pd.concat([df,df_dummy],axis=1)
    df.drop(["car_ID"],axis=1,inplace=True)
    final_columns = ['carwidth', 'enginesize', 'horsepower', 'drivewheel_fwd', 'car_company_buick', 'price']
    return df[final_columns]
df=load_dataset()
pages_dict={"Home":home,"View data":data,"Visualisation":plots,"Prediction":predict}
st.sidebar.title("Navigation")
user_selection=st.sidebar.radio("Explore",tuple(pages_dict.keys()))
if user_selection=="Home":
	home.app()
else:
    pages_dict[user_selection].app(df)	

