from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score,mean_absolute_error,mean_squared_error,mean_squared_log_error
import streamlit as st
import pandas as pd
import numpy as np
@st.cache(suppress_st_warning=True)
def prediction(df,x):
	feat=df.iloc[:,:-1]
	
	x_train,x_test,y_train,y_test=train_test_split(feat,df["price"],train_size=0.70,random_state=42)
	lr=LinearRegression()
	lr.fit(x_train,y_train)
	score=lr.score(x_train,y_train)
	y_pred_user=lr.predict([x])
	y_pred_user=y_pred_user[0]
	y_pred_df=lr.predict(x_test)
	r2score=r2_score(y_test,y_pred_df)
	mae=mean_absolute_error(y_test,y_pred_df)
	mse=mean_squared_error(y_test,y_pred_df)
	rmse=np.sqrt(mse)
	msle=mean_squared_log_error(y_test,y_pred_df)
	return y_pred_user,r2score,mae,mse,rmse,msle,score
def app(df):
	st.markdown("<p style='color:blue;font-size:25px'>This app uses <b>Linear regression</b> to predict the price of a car.", unsafe_allow_html = True)
	st.subheader("Select values")
	cw=st.slider("Select car width",float(df["carwidth"].min()),float(df["carwidth"].max()))
	hp=st.slider("Select car width",float(df["horsepower"].min()),float(df["horsepower"].max()))
	en_s=st.slider("Select car width",float(df["enginesize"].min()),float(df["enginesize"].max()))
	dr=st.radio("Is it a forward drive wheel car.Select 1 yes and 0 for no",(0,1))
	co=st.radio("Is it manufactured by buick.Select 1 yes and 0 for no",(0,1))
	if st.button("Predict"):
		st.subheader("Predicton result")
		pr,r2,m1,m2,m3,m4,score_=prediction(df,[cw,hp,en_s,dr,co])
		st.success(f"The price predicted for car is {pr}.")
		st.info(f"The score of model is{score_:.2f}. ")
		st.info(f"The r2_score of model is{r2:.2f}. ")
		st.info(f"The mean absolute error of model is{m1:.2f}. ")
		st.info(f"The mean squared error of model is{m2:.2f}. ")
		st.info(f"The root mean squared error of model is{m3:.2f}. ")
		st.info(f"The mean squared log error of model is{m3:.2f}. ")





