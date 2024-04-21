from globals import *
from next_generation import *
import numpy as np
import matplotlib.pyplot as plt

grid = np.random.randint(2, size=(width, height))
fig, ax = plt.subplots(figsize = (7, 7))
ax.set_xticks([])
ax.set_yticks([])
image = ax.imshow(grid, cmap='binary', interpolation='nearest')

while True:

    grid = compute_next_generation(grid)
    image.set_data(grid) # actualizamos la figura en lugar de generar otra. si no, hay problemas de memorias y la animación se ralentiza
    plt.pause(0.2)
    fig.canvas.mpl_connect('motion_notify_event', on_mouse_move)


plt.show()
plt.close()




""" import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from globals import width, height
from next_generation import compute_next_generation
from tqdm import tqdm

# Inicializar la matriz aleatoria
grid = np.random.randint(2, size=(width, height))

# Configurar la figura y el eje
fig, ax = plt.subplots()
ax.set_xticks([])
ax.set_yticks([])
image = ax.imshow(grid, cmap='binary', interpolation='nearest')

def update(frame):
    global grid
    grid = compute_next_generation(grid)
    image.set_data(grid)
    progress_bar.update(1)

progress_bar = tqdm(total=200, desc="Progress", position=0, leave=True)

# Crear la animación
animation = FuncAnimation(fig, update, frames=range(200), interval=50)

# Guardar la animación en un archivo de video
animation.save('animation.mp4')

plt.show()
 """

#------------------------------------------------------

""" # Crear una matriz de ceros
grid = np.zeros((width, height))

# Coordenadas iniciales del planeador en el centro de la cuadrícula
center_x = width // 2
center_y = height // 2

# Patrón del planeador
glider_pattern = [
    (1, 0),
    (2, 1),
    (0, 2),
    (1, 2),
    (2, 2)
]


# Colocar el patrón del planeador en la cuadrícula
for dx, dy in glider_pattern:
    grid[center_x + dx, center_y + dy + 15] = 1
"""
