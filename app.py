import pandas as pd
import plotly.express as px
import streamlit as st 

car_data = pd.read_csv('vehicles_us.csv')
print (car_data)

hist_button = st.button('Construir Histograma')
scatter_plot_button = st.button('Construir Gráfico de Dispersión')

if hist_button:
    st.write('Creación de histograma para el conjunto de datos.')
    
    fig = px.histogram(car_data, x="odometer")
    
    st.plotly_chart(fig, use_container_width=True)
    