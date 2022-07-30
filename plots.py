import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns

def app(df):
    st.title("Visiualisation")
    st.set_option('deprecation.showPyplotGlobalUse', False)
    st.subheader("Scatterplot")
    x=st.multiselect("Select the values",('carwidth', 'enginesize', 'horsepower', 'drivewheel_fwd', 'car_company_buick'))
    for i in x:
    	st.subheader(f"Scatterplot between {i} and price")
    	plt.figure(figsize=(18,10),dpi=96)
    	sns.scatterplot(df[i],df["price"])
    	st.pyplot()
    st.subheader("Visualisation selector")
    x2=st.multiselect("Select the graph/plot",("Histogram","Boxplot","Correlation heatmap"))
    if "Histogram" in x2:
    	st.subheader("histogram")
    	plt.figure(figsize=(18,10),dpi=96)
    	x_hist=st.selectbox("Select the values",('carwidth', 'enginesize', 'horsepower'))
    	if st.checkbox("Hide bars"):
    	    st.subheader(f"Histogram for {x_hist}")
    	    sns.distplot(df[x_hist],bins="sturges",hist=False)
    	    st.pyplot()
    	else :
    	    st.subheader(f"Histogram for {x_hist}")
    	    sns.distplot(df[x_hist],bins="sturges")
    	    st.pyplot()
    if "Boxplot" in x2:
    	st.subheader("Boxplot")
    	x_box=st.selectbox("Select the value",('carwidth', 'enginesize', 'horsepower'))    
    	st.subheader(f"Boxplot for {x_box}")
    	sns.boxplot(df[x_box])
    	st.pyplot()
    if "Correlation heatmap" in x2:
    	st.subheader("Correlation heatmap")
    	h=sns.heatmap(df.corr(),annot=True)
    	max_t,max_b=h.get_ylim()
    	h.set_ylim(max_t+1,max_b-1)
    	st.pyplot()

     	



    	    

    	    



