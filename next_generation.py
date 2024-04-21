import numpy as np

def count_neighbors(matrix, x, y):
    sum = 0
    rows, columns = matrix.shape
    for i in range(-1, 2):
        for j in range(-1, 2):
            sum += matrix[(x + i)%rows, (y + j)%columns]

    return sum - matrix[x, y]

def compute_next_generation(matrix):

    rows, columns = matrix.shape
    new_matrix = np.zeros((rows, columns), dtype=int)

    for x in range(rows):
        for y in range(columns):
            #if x != 0 and y != 0 and x != rows - 1 and y != columns - 1:
            sum_neighbors = count_neighbors(matrix, x, y)
            if matrix[x, y] == 0 and sum_neighbors == 3:
                new_matrix[x, y] = 1
            elif matrix[x, y] == 1 and (sum_neighbors < 2 or sum_neighbors > 3):
                new_matrix[x, y] = 0
            else:
                new_matrix[x, y] = matrix[x, y]
            """ else:
                new_matrix[x, y] = matrix[x, y]
                 """
    return new_matrix
 
def on_mouse_move(event):
    if event.inaxes:
        x = event.xdata
        y = event.ydata
        print(f'Posición del ratón - X: {x}, Y: {y}')
