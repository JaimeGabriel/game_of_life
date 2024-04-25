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
    image.set_data(grid) # we update the figure instead of creating a new one. This way, we save memory and the animations won't slow down
    plt.pause(0.1)
    fig.canvas.mpl_connect('motion_notify_event', on_mouse_move)


plt.show()
plt.close()


# ---------- Create animation --------------


""" fig, ax = plt.subplots()
ax.set_xticks([])
ax.set_yticks([])
image = ax.imshow(grid, cmap='binary', interpolation='nearest')

def update(frame):
    global grid
    grid = compute_next_generation(grid)
    image.set_data(grid)
    progress_bar.update(1)

progress_bar = tqdm(total=200, desc="Progress", position=0, leave=True)

animation = FuncAnimation(fig, update, frames=range(200), interval=50)

animation.save('animation.mp4')

plt.show() """

#------------- Create a glider in the center of the screen ------------------


""" grid = np.zeros((width, height))

center_x = width // 2
center_y = height // 2

glider_pattern = [
    (1, 0),
    (2, 1),
    (0, 2),
    (1, 2),
    (2, 2)
]

for dx, dy in glider_pattern:
    grid[center_x + dx, center_y + dy + 15] = 1
 """
