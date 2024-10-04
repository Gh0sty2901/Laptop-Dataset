from io import StringIO
import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
import altair as alt
from wordcloud import WordCloud
from mpl_toolkits.mplot3d import Axes3D

st.title("GROUP 6 LAPTOP-PRICES DATA SET")
df = pd.read_csv('laptop_price - dataset.csv')
st.markdown("""
    **Dataset Used**, Laptop-Price Dataset(Kaggle) 
            
    https://www.kaggle.com/datasets/ironwolf404/laptop-price-dataset?resource=download
""")
st.write(df)

buffer = StringIO()
df.info(buf=buffer)
df_info_as_string = buffer.getvalue()

st.text(df_info_as_string)

st.write("Null values of the dataset")
st.write(df.isna().sum())

st.write("Descriptive statistics")
st.write(df.describe())

st.markdown("""

`count` How many values are filled out and not null in a column. 
        
`mean:` The average value within a column. 
            
`std (Standard Deviation):` Shows how much deviation or outlier values from the mean(average value).
            
`min:` The minimum or smallest value in a column.
            
`25% (1st Quartile):` Shows the 25 or the lowest values of the set.
            
`50% (Median):` Shows the 50 or the the most frequent and average values.
            
`75% (3rd Quartile):` The 75 or the highest range values in a set.
            
`max:` The highest value in a column.

""")

st.write(pd.crosstab(df['Price (Euro)'], df['Company']))
st.markdown("""In the crosstab before we can see the prices in which each laptop 
            company sells their laptops for, We can notice that Acer sells the cheapest at 174 euro while Razer sells the 
            most expensive at 6099 Euro
""")
#TABLE 1
def laptop_Ave_Chart():
    ave = df.groupby('Company')['Price (Euro)'].mean().reset_index()

    ave = ave.sort_values(by ='Price (Euro)', ascending= True)
    
    st.bar_chart(data=ave, x='Company', y='Price (Euro)', horizontal= True)
    
laptop_Ave_Chart()
st.markdown("""We can observe in this bar graph that Razer sells the most expensive laptops on 
            average while Vero sells the cheapest on average.
            """)

#TABLE 2
st.write(pd.crosstab(df['Price (Euro)'], df['TypeName']))

st.markdown("""In the Crosstab above we can see the price of laptop depending on the type of laptop. We can see that
               the cheapest one being sold is the notebook type while the most expensive one is a gaming laptop
""")

def laptop_Type_Chart():
    ave = df.groupby('TypeName')['Price (Euro)'].mean().reset_index()
    st.bar_chart(data = ave, x='TypeName', y='Price (Euro)', horizontal = True)
laptop_Type_Chart()
st.markdown("""In this bargraph we can observe that the most expensive laptop type on average is actually the workbook 
            while the cheapest type of laptop is the netbook on average. This is likely due to workbooks having more 
            specialized equipment due to needing higher specs to do work while netbooks are merely meant to 
            surf the web.
            """)
    
#TABLE 3

#TABLE 4

#TABLE 5

#TABLE 6

#TABLE 7

#TABLE 8

#TABLE 9

#TABLE 10


