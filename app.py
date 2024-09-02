import pandas as pd
import plotly.express as px
import streamlit as st 

car_data = pd.read_csv('C:/Users/USUARIO/Maldonado/Trabajos DA/Ejercicio-sprint-6/vehicles_us.csv')

print (car_data)
st.header('Venta de Vehículos por kilometraje')
hist_button = st.button('Construir Histograma')
scatter_plot_button = st.button('Construir Gráfico de Dispersión')

if hist_button:
    st.write('Creación de histograma para el conjunto de datos.')
    
    fig = px.histogram(car_data, x="odometer", nbins=30)
    
    st.plotly_chart(fig, use_container_width=True)
    
if scatter_plot_button:
    st.write('Creación de gráfico de dispersión para el conjunto de datos.')
    fig_scatter = px.scatter(car_data, x="odometer", y="price")
    st.plotly_chart(fig_scatter, use_container_width=True)

    