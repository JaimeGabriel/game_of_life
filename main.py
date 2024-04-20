from globals import *
from next_generation import *
import numpy as np
import matplotlib.pyplot as plt

grid = np.random.randint(2, size=(width, height))
fig, ax = plt.subplots(figsize = (10, 10))
ax.set_xticks([])
ax.set_yticks([])
image = ax.imshow(grid, cmap='binary', interpolation='nearest')

for i in range(200):

    grid = compute_next_generation(grid)
    image.set_data(grid)
    plt.pause(0.00001)
    fig.canvas.mpl_connect('motion_notify_event', on_mouse_move)


plt.show()
plt.close()

