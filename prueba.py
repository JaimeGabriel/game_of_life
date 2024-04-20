import numpy as np
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


