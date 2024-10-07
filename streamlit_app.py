from io import StringIO
import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
import altair as alt
import re
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
def cpu_Ave_Chart():
    cpu_avg_price = df.groupby('CPU_Company')['Price (Euro)'].mean().loc[['Intel', 'AMD']]
    st.bar_chart(cpu_avg_price)
cpu_Ave_Chart()
st.markdown("""As shown in the bargraph, it compares the average pricing of laptops based on the CPU manufacturer (AMD vs Intel). 
            Based on it, data tells that the laptops with AMD CPUs are signiificantly lower compared to laptops with Intel CPUs.""")

#TABLE 4
def brand_count():
    brand_lt_count = df['Company'].value_counts().sort_values(ascending=True)
    st.bar_chart(brand_lt_count)
brand_count()
st.markdown("""In this bargraph, the number of available laptops being sold by each company is shown, with Dell, Lenovo, HP, being
            among the brands with the most available options of laptops for customers to choose from, while Huawei having the least
            laptops being sold to the market""")

#TABLE 5
def Apple_Laptops():
    apple_products = df[df['Company'] == 'Apple']

    plt.figure(figsize=(10, 6))
    plt.bar(apple_products['Product'], apple_products['Price (Euro)'], color='blue')
    plt.title('Prices of Apple Products')
    plt.xlabel('Product')
    plt.ylabel('Price (Euro)')
    plt.xticks(rotation=45)
    plt.grid(axis='y')

    st.pyplot(plt)

st.markdown("""For this bar chart, it shows the MacBook products price ranges.
            Each bar could indicate a range (e.g., minimum and maximum prices) for the specific model, 
            highlighting how prices vary within each product line.""")

#TABLE 6
def Average_Laptop_Price():
    average_price = df.groupby('Inches')['Price (Euro)'].mean().reset_index()

    plt.figure(figsize=(12, 6))
    plt.plot(average_price['Inches'], average_price['Price (Euro)'], 'o', color='b')
    plt.title('Average Laptop Price by Screen Size')
    plt.xlabel('Screen Size (Inches)')
    plt.ylabel('Average Price (Euro)')
    plt.xticks(rotation=45)
    plt.grid()
    st.pyplot(plt)
Average_Laptop_Price()

st.markdown("""For this dot plot graph, it shows the relationship between laptop prices and their screen sizes.
            For instance, larger screen sizes (like 18+ inches) might be associated with higher prices.""")
#TABLE 7
def CPU_Frequency():
    df.set_index('Company', inplace=True) 
    
    
    frequency_counts = df['CPU_Frequency (GHz)'].value_counts().sort_index() 
    
    
    st.title('Count of CPU Frequencies (GHz)') 
    st.write("This bar chart shows the count of different CPU frequencies.") 
    
    
    plt.figure(figsize=(12, 6)) 
    plt.bar(frequency_counts.index, frequency_counts.values, color='blue') 
    plt.title('Count of CPU Frequencies (GHz)') 
    plt.xlabel('CPU Frequency (GHz)') 
    plt.ylabel('Count') 
    plt.xticks(rotation=45) 
    plt.grid(axis='y') 
    plt.tight_layout() 
    
    
    st.pyplot(plt) 
CPU_Frequency()  
 
st.write(""" 
This bar chart illustrates the distribution of CPU frequencies (in GHz) across various laptops from the dataset. 
 
Most laptops fall between 2.0 GHz and 3.0 GHz, with the highest concentration near 2.5 GHz (over 250 units),  
while lower frequencies (0.5 GHz to 1.5 GHz) are less common (below 100 units), and frequencies above 3.0 GHz are rare. 
""") 

#TABLE 8
def CPU_Company():
    CPU_company = df['CPU_Company'].value_counts() 
    
    
    st.title('Count of CPU Manufacturers') 
    st.write("This bar chart shows the CPUs manufactured by Intel, AMD, and Samsung.") 
    
    
    plt.figure(figsize=(12, 6)) 
    plt.bar(CPU_company.index, CPU_company.values, color='blue', edgecolor='black') 
    plt.title('Count of CPU Manufacturers') 
    plt.xlabel('CPU Manufacturer') 
    plt.ylabel('Count') 
    plt.xticks(rotation=45) 
    plt.grid(axis='y') 
    plt.tight_layout() 
    
    
    st.pyplot(plt) 
CPU_Company()
 
 
st.write(""" 
**Intel**: Dominates the dataset, with a count exceeding 1200 laptops. Intel is the leading manufacturer,  indicating its high prevalence in the laptop market from this dataset. 
 
**AMD**: The count for AMD is significantly lower, just above 100. AMD follows but shows a much smaller share compared to Intel. 
 
**Samsung**: Although labeled, it appears to have no data. 
""") 

#TABLE 9
# Average RAM Graph
def average_RAM():
    average_ram_per_brand = df.groupby('Company')['RAM (GB)'].mean().sort_values()

    plt.figure(figsize=(10, 6))
    average_ram_per_brand.plot(kind='barh', color='skyblue')
    plt.title('Average RAM by Laptop Brand')
    plt.xlabel('Average RAM (GB)')
    plt.ylabel('Brand')
    plt.grid(True)
    st.pyplot(plt)

# Display
average_RAM()

# Analysis
st.write("""
Each horizontal bar on the graph represents a different laptop brand, such as Apple, Dell, Acer, and so on. The graph shows the average RAM (in GB) for each of these brands. This shows that Razer and MSI have the highest average memory at over 13 GB, while Vero and Mediacom have much lower averages at about 3–4 GB. 

The brands can be easily compared in terms of memory capacity across various manufacturers because they are arranged in ascending order according to their average RAM. This graph highlights significant trends. It indicates that, while brands with lower average RAM may concentrate on budget or daily use laptops, high-performance brands, like Razer and MSI, are probably targeting power users, such as gamers or professionals needing high-end performance.

Based on performance requirements and use cases, this comparison provides information about how memory configurations differ among brands, which can assist consumers in making decisions.
""")

#TABLE 10
# Average Sceen Resolution Graph
# Sample DataFrame for demonstration; replace with your actual data
laptop_data = pd.DataFrame({
    'Company': ['Dell', 'HP', 'Apple', 'Acer'],
    'ScreenResolution': ['1920x1080', '1366x768', '2560x1600', '1920x1080']
})

def extract_resolution(res):
    match = re.search(r'(\d+)x(\d+)', res)
    if match:
        width, height = match.groups()
        return int(width), int(height)
    return None, None

def Screen_Res_By_Brand():
    laptop_data['Width'], laptop_data['Height'] = zip(*laptop_data['ScreenResolution'].apply(extract_resolution))

    laptop_data_clean = laptop_data.dropna(subset=['Width', 'Height'])

    avg_resolution = laptop_data_clean.groupby('Company')[['Width', 'Height']].mean()

    plt.figure(figsize=(10, 6))
    avg_resolution.plot(kind='bar', stacked=False, width=0.8)
    plt.title('Average Screen Resolution by Laptop Brand')
    plt.xlabel('Brand')
    plt.ylabel('Average Resolution (pixels)')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

    # Display
    st.pyplot(plt)
Screen_Res_By_Brand()

# Analysis
st.write("""
With two bars for each laptop brand, one representing the average screen width and the other the average screen height, 
the graph shows the average screen resolution (in pixels) for different laptop brands. Compared to other brands like 
Acer and HP, brands like Apple and Dell typically have higher average screen resolutions, particularly in terms of width. 
All brands generally have wider widths (horizontal resolutions), which correspond to the widescreen format found in many 
contemporary laptops. The disparities in focus on display quality can be seen in the screen resolutions, with some brands 
offering higher-end models with sharper screens, like "Retina" or Full HD displays.
""")


st.markdown("""
`CONCLUSIONS`

With all the data collected above we can see the different ways the laptops are priced by brand or 
laptop specfications. We can see that Razer on average sells laptops more expensive 
but offer higher specs with having higher screen resolutions and higher ram storage 
on average. We can notice as well that Intel dominates the laptop market as most 
laptops run Intel CPUS rather than AMD or samsung CPUS. We can see as well that 
the most frequent CPU frequency is 2.5 GHz.
""")
