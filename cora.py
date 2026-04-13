import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation


fig, ax = plt.subplots(figsize=(7, 8), facecolor='black')
ax.set_facecolor('black')

ax.set_xlim(-2, 2)
ax.set_ylim(-2, 2.5)
ax.set_aspect('equal')

ax.grid(True, which='both', color='gray', linestyle='--', linewidth=0.5, alpha=0.3)
ax.set_xticks(np.arange(-2, 2.1, 0.2))
ax.set_yticks(np.arange(-2, 2.6, 0.2))

ax.set_xticklabels([])
ax.set_yticklabels([])

ax.axhline(0, color='white', linewidth=1)
ax.axvline(0, color='white', linewidth=1)

x = np.linspace(-np.sqrt(3), np.sqrt(3), 2000) 
line, = ax.plot([], [], color='#FF3385', lw=2)

text_crush = ax.text(0, -1.8, "Feliz dia mi niña", fontsize=18, color='#FF7F50', ha='center', va='center', fontfamily='serif')

def init():
    line.set_data([], [])
    return line,

def update(frame):
    M = 45 + 35 * np.sin(frame / 10) 
    
    y = np.power(np.abs(x), 2/3) + 0.9 * np.sin(M * x) * np.sqrt(3 - x**2)
    
    line.set_data(x, y)
    return line,

ani = FuncAnimation(fig, update, frames=np.linspace(0, 2*np.pi*10, 200),
                    init_func=init, blit=True, interval=30)

plt.show()