import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import time

st.set_page_config(page_title="Para mi niña", layout="centered")

# Configuramos el gráfico
fig, ax = plt.subplots(figsize=(7, 8), facecolor='black')
ax.set_facecolor('black')
ax.set_xlim(-2, 2)
ax.set_ylim(-2, 2.5)
ax.set_aspect('equal')
ax.axis('off') # Quitamos los ejes para que se vea más limpio

x = np.linspace(-np.sqrt(3), np.sqrt(3), 400) # Menos puntos para que sea rápido
line, = ax.plot([], [], color='#FF3385', lw=3)
text_crush = ax.text(0, -1.8, "Feliz día mi niña", fontsize=18, 
                     color='#FF7F50', ha='center', va='center', fontfamily='serif')

# Creamos un contenedor vacío en Streamlit para ir actualizando el gráfico
placeholder = st.empty()

# Bucle de animación
for frame in range(200):
    M = 45 + 35 * np.sin(frame / 10)
    y = np.power(np.abs(x), 2/3) + 0.9 * np.sin(M * x) * np.sqrt(3 - x**2)
    
    line.set_data(x, y)
    
    # Actualizamos el gráfico en el contenedor
    placeholder.pyplot(fig)
    
    # Un pequeño delay para que no vaya demasiado rápido
    time.sleep(0.05)
