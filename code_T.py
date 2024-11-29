# -*- coding: utf-8 -*-
""" Created on Thu Nov 28 00:24:43 2024
@author: HP-PC
"""

# Import packages

# Import required packages for data scraping, processing, visualization, and Streamlit UI
import numpy as np  # For numerical operations
import streamlit as st  # For building interactive web apps
import pandas as pd  # For data manipulation and analysis
from bs4 import BeautifulSoup as bs  # For web scraping HTML content
import requests  # For making HTTP requests to fetch web pages
import plotly.express as px  # For creating interactive visualizations
import base64  # For encoding binary files to base64 strings
import streamlit.components.v1 as components  # For embedding HTML/JS elements in Streamlit

# Describe the app functions
st.markdown("<h1 style='text-align: center; color: blue;'>DATA COLLECTION APP</h1>", unsafe_allow_html=True)
st.markdown("""
This app allows scraping data using BeautifulSoup, to download scraped data on vetements-hommes, chaussures-hommes, vetements-enfants, and chaussures-enfants.
* **Python libraries:** base64, pandas, streamlit
* **Data source:** 
    - [vetements-homme](https://sn.coinafrique.com/categorie/vetements-homme) 
    - [chaussures-homme](https://sn.coinafrique.com/categorie/chaussures-homme) 
    - [vetements-enfants](https://sn.coinafrique.com/categorie/vetements-enfants) 
    - [chaussures-enfants](https://sn.coinafrique.com/categorie/chaussures-enfants) 
""")

# Function to add background image
def add_background(image_file):
    with open(image_file, "rb") as img_file:
        encoded_string = base64.b64encode(img_file.read()).decode()
        st.markdown(
            f"""<style>
            .stApp {{ background-image: url(data:image/jpeg;base64,{encoded_string}); 
            background-size: cover; background-repeat: no-repeat; background-attachment: fixed; }}
            </style>""", unsafe_allow_html=True)

# Add the background image by specifying the filename
add_background("img_file.jpg")


# Caching function to optimize DataFrame conversion for CSV download
@st.cache_data
def convert_df(df):
    """Convert a dataframe to a CSV format encoded in UTF-8."""
    return df.to_csv().encode('utf-8')

# Function to display data and provide a download button in Streamlit
def load(dataframe, title, key1, key4):
    """Load a Streamlit UI with unique keys for all components."""
    st.markdown("""<style> div.stButton {text-align: center;} </style>""", unsafe_allow_html=True)
    
    if st.button(title, key=key1): # Display button with title
        st.subheader('Display Data Dimension') # Subheader to show data dimensions
        st.write(f'Data dimension: {dataframe.shape[0]} rows and {dataframe.shape[1]} columns.')  # Show data shape
        st.dataframe(dataframe)  # Render the DataFrame in the app
        csv = convert_df(dataframe)  # Convert DataFrame to CSV
        st.download_button(label="Download data as CSV", data=csv, file_name='Data.csv', mime='text/csv', key=key4) # Add download button

def load_Vetements_homme(mul_page):
    df = pd.DataFrame()
    for page in range(1, int(mul_page) + 1):
        url = f'https://sn.coinafrique.com/categorie/vetements-homme?page={page}'
        res = requests.get(url)
        soup = bs(res.text, 'html.parser')
        containers = soup.find_all('div', class_='col s6 m4 l3')
        data = []
        for container in containers:
            try:
                get_info = container.find('p', class_='ad__card-description').text.strip().split()
                type_clothes = get_info[0]
                price = container.find('p', class_='ad__card-price').text.strip().replace('CFA', '').replace(' ', '')
                adress = container.find('p', class_='ad__card-location').span.text
                image_link = container.find('a', class_='card-image ad__card-image waves-block waves-light').img['src']
                data.append({
                    'type_clothes': type_clothes,
                    'price': price,
                    'adress': adress,
                    'image_link': image_link
                })
            except Exception as e:
                print(f"Error scraping data on page {page}: {e}")
        DF = pd.DataFrame(data)
        df = pd.concat([df, DF], axis=0).reset_index(drop=True)
    return df

def load_Chaussures_homme(mul_page):
    df = pd.DataFrame()
    for page in range(1, int(mul_page) + 1):
        url = f'https://sn.coinafrique.com/categorie/chaussures-homme?page={page}'
        res = requests.get(url)
        soup = bs(res.text, 'html.parser')
        containers = soup.find_all('div', class_='col s6 m4 l3')
        data = []
        for container in containers:
            try:
                get_info = container.find('p', class_='ad__card-description').text.strip().split()
                type_shoes = get_info[0]
                price = container.find('p', class_='ad__card-price').text.strip().replace('CFA', '').replace(' ', '')
                adress = container.find('p', class_='ad__card-location').span.text
                image_link = container.find('a', class_='card-image ad__card-image waves-block waves-light').img['src']
                data.append({
                    'type_shoes': type_shoes,
                    'price': price,
                    'adress': adress,
                    'image_link': image_link
                })
            except Exception as e:
                print(f"Error scraping data on page {page}: {e}")
        DF = pd.DataFrame(data)
        df = pd.concat([df, DF], axis=0).reset_index(drop=True)
    return df

def load_Vetements_enfants(mul_page):
    df = pd.DataFrame()
    for p in range(1, int(mul_page) + 1):
        url = f'https://sn.coinafrique.com/categorie/vetements-enfants?page={p}'
        res = requests.get(url)
        soup = bs(res.text, 'html.parser')
        containers = soup.find_all('div', class_='col s6 m4 l3')
        data = []
        for container in containers:
            try:
                get_info = container.find('p', class_='ad__card-description').text.strip().split()
                type_clothes = get_info[0]
                price = container.find('p', class_='ad__card-price').text.strip().replace('CFA', '').replace(' ', '')
                adress = container.find('p', class_='ad__card-location').span.text
                image_link = container.find('a', class_='card-image ad__card-image waves-block waves-light').img['src']
                data.append({
                    'type_clothes': type_clothes,
                    'price': price,
                    'adress': adress,
                    'image_link': image_link
                })
            except Exception as e:
                print(f"Error scraping data on page {p}: {e}")
        DF = pd.DataFrame(data)
        df = pd.concat([df, DF], axis=0).reset_index(drop=True)
    return df

def load_Chaussures_enfants(mul_page):
    df = pd.DataFrame()
    for p in range(1, int(mul_page) + 1):
        url = f'https://sn.coinafrique.com/categorie/chaussures-enfants?page={p}'
        res = requests.get(url)
        soup = bs(res.text, 'html.parser')
        containers = soup.find_all('div', class_='col s6 m4 l3')
        data = []
        for container in containers:
            try:
                get_info = container.find('p', class_='ad__card-description').text.strip().split()
                type_shoes = get_info[0]
                price = container.find('p', class_='ad__card-price').text.strip().replace('CFA', '').replace(' ', '')
                adress = container.find('p', class_='ad__card-location').span.text
                image_link = container.find('a', class_='card-image ad__card-image waves-block waves-light').img['src']
                dic = {
                    'type_shoes': type_shoes,
                    'price': price,
                    'adress': adress,
                    'image_link': image_link
                }
                data.append(dic)
            except Exception as e:
                print(f"Error scraping data on page {p}: {e}")
        DF = pd.DataFrame(data)
        df = pd.concat([df, DF], axis=0).reset_index(drop=True)
    return df

# Sidebar for user input features
st.sidebar.header('User Input Features')
Pages = st.sidebar.selectbox('Pages indexes', list([int(p) for p in np.arange(1,120)]))
Choices = st.sidebar.selectbox(
    'Options',
    ['Scrape data using BeautifulSoup', 'Download scraped data', 'Dashboard of the data', 'Fill the  Form']
)

if Choices == 'Scrape data using BeautifulSoup':
    Vetements_homme_mul_pag = load_Vetements_homme(Pages)
    Chaussures_homme_mul_pag = load_Chaussures_homme(Pages)
    Vetements_enfants_mul_pag = load_Vetements_enfants(Pages)
    Chaussures_enfants_mul_pag = load_Chaussures_enfants(Pages)

    load(Vetements_homme_mul_pag, 'Vetements Homme', '1', '301')
    load(Chaussures_homme_mul_pag, 'Chaussures Homme', '2', '302')
    load(Vetements_enfants_mul_pag, 'Vetements Enfants', '3', '303')
    load(Chaussures_enfants_mul_pag, 'Chaussures Enfants', '4', '304')

elif Choices == 'Download scraped data':
    Vetements_hommes = pd.read_csv('data/vetements_hommes_ws.csv')  
    Chaussures_hommes = pd.read_csv('data/chaussures_hommes_ws.csv')  
    Vetements_enfants = pd.read_csv('data/vetements_enfants_ws.csv')  
    Chaussures_enfants = pd.read_csv('data/chaussures_enfants_ws.csv')  
    
    load(Vetements_hommes, 'Vetements hommes', '1', '301')
    load(Chaussures_hommes, 'Chaussures hommes', '2', '302')
    load(Vetements_enfants, 'Vetements enfants', '3', '303')
    load(Chaussures_enfants, 'Chaussures enfants', '4', '304')


elif Choices == 'Dashboard of the data':
    df1 = pd.read_csv('data/Vetements_hommes_clean.csv')  
    df2 = pd.read_csv('data/Chaussures_hommes_clean.csv') 
    df3 = pd.read_csv('data/Vetements_enfants_clean.csv') 
    df4 = pd.read_csv('data/chaussures_enfants_clean.csv')  
    col1, col2 , col3 , col4, col5 = st.columns(5)
    with col1:
    
        # Scatter plot and Box plot for df1 (Men's clothes)
        fig1_scatter = px.scatter(df1, x="type_clothes", y="price", title="Price vs Men Type of Clothes")
        st.plotly_chart(fig1_scatter)
   
    with col2:
         fig1_box = px.box(df1, x="type_clothes", y="price", title="Price Distribution by Men Type of Clothes")
         st.plotly_chart(fig1_box)
    with col3:    
    # Scatter plot and Box plot for df2 (Men's shoes)
         fig2_scatter = px.scatter(df2, x="type_shoes", y="price", title="Price vs Men Type of Shoes")
         st.plotly_chart(fig2_scatter)
    with col3:
         fig2_box = px.box(df2, x="type_shoes", y="price", title="Price Distribution by Men Type of Shoes")    
         st.plotly_chart(fig2_box)
    with col4:
    # Scatter plot for Kids' Clothes (df3)
         fig3_scatter = px.scatter(df3, x="type_clothes", y="price", title="Price vs Kids Type of Clothes")
         st.plotly_chart(fig3_scatter)
    with col5:
    # Box plot for Kids' Shoes (df4)
         fig4_box = px.box(df4, x="type_shoes", y="price", title="Price Distribution by Kids Type of Shoes")
         st.plotly_chart(fig4_box)

else:
   components.html("""<iframe src=\"https://ee.kobotoolbox.org/i/kSxcH0CN\" width=\"800\" height=\"600\"></iframe> """, height=600,width=800)
