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
    
        
        # Define the nested dictionary
        clothing_dict = {
            'tenues_africaines': [
                'Tenu africaine', 'Tenue africaine', 'Boubou africain homme', 'Tenues africaines', 'Tenues africaines hommes',
                'Jallaba', 'Jallabé homme', 'Jallaba homme', 'Jalabba', 'Jallaba + Pantalon', 'Jallabas homme'
            ],
            'vêtements_hommes': [
                'Vêtement homme', 'Chemise décontractée', 'Ensemble homme', 'T-shirt en coton', 'Chemise', 'Chemise homme', 
                'Chemise Giant', 'T-shirt coton', 'Pantalon kaki', 'Ensemble polo pantalon', 'Vêtements homme', 'Pantalons hommes',
                'Pantalons et chemises', 'Polo Lacoste', 'Short', 'Pantalons kaki', 'Vêtements homme', 'Pantalon chic', 
                'Chemises homme', 'Maillots NBA', 'Pantalon Kaki Homme', 'Polo Lacoste homme', 'Pantalon bleu', 'Ensemble homme coton'
            ],
            'vêtements_détente': [
                'T-shirt', 'Tee-shirt coton', 'T-shirt Polo', 'Tee-shirts en coton', 'Débardeur', 'Débardeur homme',
                'Vêtements', 'Vêtements hommes', 'Débardeur coton', 'T-shirt Louis Vuitton', 'T-shirt Essential', 'T-shirt Amiri'
            ],
            'vêtements_chic': [
                'Pantalon jean', 'Chemise en lin', 'Smoking', 'Ensemble costume', 'Pantalon jeans déchiré', 'Veste blazer',
                'Chemise Lin', 'Pantalon + chemise', 'Pantalon kaki homme', 'Chemise Madras homme', 'T-shirt - Moncler',
                'T-shirt - Givenchy', 'Blouson', 'Blouson homme', 'Veste blazer homme'
            ],
            'vêtements_été': [
                'Ensemble t-shirt - short', 'Ensemble short + t-shirt', 'T-shirt polo', 'T-shirt Dior', 'Ensemble Lacoste - Kaki', 
                'Shorts homme', 'Chemise courte manche', 'Ensemble Polo', 'Pantalon Kaki', 'T-shirt Body homme', 'Ensemble Adidas',
                'T-shirt Balenciaga', 'Ensemble Polo + pantalon', 'Short Nike', 'T-shirt - Fear of god', 'T-shirt - Nasa'
            ],
            'vêtements_formels': [
                'Chemise longues manches', 'Chemise courte manche en coton', 'Pantalon jeans homme', 'Chemises Lacoste', 
                'Vêtements homme', 'Ensemble t-shirt - pantalon', 'Ensemble Chemise', 'Chemises Gant', 'Pantalon + Polo',
                'Pantalon jeans', 'Pantalon + t-shirt', 'Polo Lacoste en coton', 'T-shirt Prada', 'T-shirt - Louis Vuitton', 
                'Chemise - pantalon', 'T-shirt - Amiri', 'T-shirt - Gucci', 'T-shirt - Balenciaga'
            ]
        }
        
        # Flatten the nested dictionary
        flat_mapping = {item: main_category for main_category in clothing_dict for item in clothing_dict[main_category]}
        
        # Replace `type_clothes` values using the mapping
        df1['type_clothes'] = df1['type_clothes'].replace(flat_mapping)
        
        # Filter data to keep only mapped categories
        df1_filtered = df1[df1['type_clothes'].isin(flat_mapping.values())]
        
        # Count occurrences of each category
        category_counts = df1_filtered['type_clothes'].value_counts().reset_index()
        category_counts.columns = ['Category', 'Count']
        
        # Create a pie chart using Plotly Express
        fig_pie = px.pie(category_counts, names='Category', values='Count',
                         title='Répartition des Catégories de Vêtements')
        
        # Display the pie chart in Streamlit
        st.title("Analyse des Catégories de Vêtements")
        st.plotly_chart(fig_pie)


with col2:
         # Define the nested dictionary
         clothing_dict = {
         "Girls": {
             "Dresses": [
                 "Robe enfant", "Robe princesse", "Robe fille", "Robe broderie enfant",
                 "Robe pour anniversaire ou cérémonie", "Robe enfant princesse",
                 "Robe de cérémonie enfant", "Robe wax enfant"
             ],
             "Ensembles": [
                 "Ensemble fille", "Ensemble short fille", "Ensemble t-shirt + culotte",
                 "Ensemble 5 pièces", "Ensemble coton fille"
             ],
             "Accessories": [
                 "Boxer slip fille", "Caleçon fille", "Jupe fille", "Slip fille"
             ]
         },
         "Boys": {
             "Ensembles": [
                 "Ensemble garçon", "Ensemble chemise - pantalon enfant",
                 "Ensemble coton garçon", "Ensemble short + t-shirt garçon"
             ],
             "Tops": [
                 "Polo enfant", "Chemise garçon", "T-shirt enfant"
             ],
             "Bottoms": [
                 "Pantalon garçon", "Short Enfant", "Caleçons garçon"
             ]
         }
     }
     
     # Flatten the nested dictionary for "Girls" and "Boys" only
flat_mapping = {}
for main_category in ["Girls", "Boys"]:  # Filter for only Girls and Boys
             subcategories = clothing_dict[main_category]
             for subcategory, items in subcategories.items():
                 for item in items:
                     flat_mapping[item] = f"{main_category} - {subcategory}"
         
         # Replace `type_clothes` values using the filtered mapping
                     df3['type_clothes'] = df3['type_clothes'].replace(flat_mapping)
         
         # Filter data to keep only mapped categories
                     df3_filtered = df3[df3['type_clothes'].isin(flat_mapping.values())]
         
         # Group data by clothing category and calculate average price
                     category_avg_price = df3_filtered.groupby('type_clothes')['price'].mean().reset_index()
         
         # Create a bar plot for average price by clothing category
                     fig_bar = px.bar(
             category_avg_price,
             x='type_clothes',
             y='price',
             color='type_clothes',
             title='Bar Plot of Average Price by Clothing Categories (Girls & Boys)',
             labels={'type_clothes': 'Clothing Categories', 'price': 'Average Price'},
             text='price',  # Add value labels to bars
             template="plotly_white"
         )
    
     # Update layout for better readability
                     fig_bar.update_layout(
         xaxis_tickangle=45,
         xaxis_title="Clothing Categories",
         yaxis_title="Average Price",
     )
    
     # Streamlit App
st.title("Bar Plot of Clothing Categories (Girls & Boys) vs Average Price")
st.plotly_chart(fig_bar)
with col3:    
    
    with col4:
    # Scatter plot for Kids' Clothes (df3)
         fig3_scatter = px.scatter(df3, x="type_clothes", y="price", title="Price vs Kids Type of Clothes")
         st.plotly_chart(fig3_scatter)
    

else:
   components.html("""<iframe src=\"https://ee.kobotoolbox.org/i/kSxcH0CN\" width=\"800\" height=\"600\"></iframe> """, height=600,width=800)
