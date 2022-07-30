import streamlit as st
import pandas as pd
import numpy as np
def app(df):
	st.title("View data")
	with st.beta_expander("View Dataset"):
		st.dataframe(df)
	st.subheader("Columns's description")
	if st.checkbox("Show summary"):
		st.write(df.describe())
	col_1,col_2,col_3=st.beta_columns(3)
	with col_1:
		if st.checkbox("Show column names"):
			st.write(df.columns)
	with col_2:
	    if st.checkbox("Show datatypes"):
	        st.write(df.dtypes)
	with col_3:
	    if st.checkbox("Show column data"):
	        col=st.selectbox("Select the column",tuple(df.columns))
	        st.write(df[col])        



