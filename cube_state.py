class Cube:
    def __init__(self):
        self.faces = {
            'U': [['W'] * 3 for _ in range(3)],
            'D': [['Y'] * 3 for _ in range(3)],
            'F': [['G'] * 3 for _ in range(3)],
            'B': [['B'] * 3 for _ in range(3)],
            'L': [['O'] * 3 for _ in range(3)],
            'R': [['R'] * 3 for _ in range(3)],
        }

    def copy(self):
        new_cube = Cube()
        new_cube.faces = {f: [row[:] for row in face] for f, face in self.faces.items()}
        return new_cube

    def __str__(self):
        return '\n'.join(f"{face}: {self.faces[face]}" for face in self.faces)
