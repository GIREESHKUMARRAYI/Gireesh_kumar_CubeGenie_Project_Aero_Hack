import tkinter as tk
from cube_state import Cube

COLORS = {
    'W': 'white', 'Y': 'yellow', 'G': 'green',
    'B': 'blue', 'O': 'orange', 'R': 'red'
}

def draw_cube(canvas, cube):
    size = 20
    offset = {
        'U': (3*size, 0), 'L': (0, 3*size), 'F': (3*size, 3*size),
        'R': (6*size, 3*size), 'B': (9*size, 3*size), 'D': (3*size, 6*size)
    }
    for face, grid in cube.faces.items():
        ox, oy = offset[face]
        for i in range(3):
            for j in range(3):
                canvas.create_rectangle(
                    ox + j*size, oy + i*size,
                    ox + (j+1)*size, oy + (i+1)*size,
                    fill=COLORS[grid[i][j]], outline='black'
                )

def launch_gui(cube):
    root = tk.Tk()
    root.title("Rubik's Cube Visualizer")
    canvas = tk.Canvas(root, width=400, height=300)
    canvas.pack()
    draw_cube(canvas, cube)
    root.mainloop()
