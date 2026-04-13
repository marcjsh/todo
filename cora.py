import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import time
st.set_page_config(page_title="Para mi niña ❤️", layout="centered")
# Estilo personalizado para centrar y dar color al fondo
st.markdown("""
    <style>
    .main {
        background-color: #000000;
    }
    </style>
    """, unsafe_allow_html=True)
# Creamos la figura de Matplotlib
fig, ax = plt.subplots(figsize=(7, 8), facecolor='black')
ax.set_facecolor('black')

# Configuración de límites y quitar ejes para que se vea limpio
ax.set_xlim(-2, 2)
ax.set_ylim(-2, 2.5)
ax.set_aspect('equal')
ax.axis('off')

# Preparar los datos
x = np.linspace(-np.sqrt(3), np.sqrt(3), 400)
line, = ax.plot([], [], color='#FF3385', lw=3)
text_crush = ax.text(0, -1.5, "Feliz día mi niña", fontsize=22, 
                     color='#FF7F50', ha='center', va='center', fontfamily='serif')

# Contenedor de Streamlit donde se mostrará el dibujo
placeholder = st.empty()

# Bucle de la animación (el corazón se irá formando/moviendo)
# Usamos un bucle infinito para que el corazón no deje de "latir"
while True:
    for frame in range(0, 100):
        # La fórmula del corazón con el parámetro M variando para el efecto de latido
        M = 45 + 35 * np.sin(frame / 10) 
        y = np.power(np.abs(x), 2/3) + 0.9 * np.sin(M * x) * np.sqrt(3 - x**2)
        
        line.set_data(x, y)
        
        # Dibujar en el contenedor
        placeholder.pyplot(fig)
        
        # Velocidad de la animación
        time.sleep(0.01)
