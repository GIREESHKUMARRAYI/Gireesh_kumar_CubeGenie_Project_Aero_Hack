def rotate_face(face):
    return [list(row) for row in zip(*face[::-1])]

def rotate_face_ccw(face):
    return rotate_face(rotate_face(rotate_face(face)))

def apply_move(cube, move):
    f = cube.faces

    def rotate_sides(sides):
        temp = sides[-1]
        for i in reversed(range(1, len(sides))):
            sides[i] = sides[i - 1]
        sides[0] = temp
        return sides

    def rotate_sides_ccw(sides):
        temp = sides[0]
        for i in range(len(sides) - 1):
            sides[i] = sides[i + 1]
        sides[-1] = temp
        return sides

    if move == 'U':
        f['U'] = rotate_face(f['U'])
        f['F'][0], f['R'][0], f['B'][0], f['L'][0] = rotate_sides([f['F'][0], f['R'][0], f['B'][0], f['L'][0]])
    elif move == "U'":
        f['U'] = rotate_face_ccw(f['U'])
        f['F'][0], f['L'][0], f['B'][0], f['R'][0] = rotate_sides_ccw([f['F'][0], f['L'][0], f['B'][0], f['R'][0]])
    elif move == 'D':
        f['D'] = rotate_face(f['D'])
        f['F'][2], f['L'][2], f['B'][2], f['R'][2] = rotate_sides([f['F'][2], f['L'][2], f['B'][2], f['R'][2]])
    elif move == "D'":
        f['D'] = rotate_face_ccw(f['D'])
        f['F'][2], f['R'][2], f['B'][2], f['L'][2] = rotate_sides_ccw([f['F'][2], f['R'][2], f['B'][2], f['L'][2]])
    elif move == 'F':
        f['F'] = rotate_face(f['F'])
        temp = [f['U'][2][i] for i in range(3)]
        for i in range(3):
            f['U'][2][i] = f['L'][2 - i][2]
            f['L'][2 - i][2] = f['D'][0][2 - i]
            f['D'][0][2 - i] = f['R'][i][0]
            f['R'][i][0] = temp[i]
    elif move == "F'":
        f['F'] = rotate_face_ccw(f['F'])
        temp = [f['U'][2][i] for i in range(3)]
        for i in range(3):
            f['U'][2][i] = f['R'][i][0]
            f['R'][i][0] = f['D'][0][2 - i]
            f['D'][0][2 - i] = f['L'][2 - i][2]
            f['L'][2 - i][2] = temp[i]
    elif move == 'B':
        f['B'] = rotate_face(f['B'])
        temp = [f['U'][0][i] for i in range(3)]
        for i in range(3):
            f['U'][0][i] = f['R'][i][2]
            f['R'][i][2] = f['D'][2][2 - i]
            f['D'][2][2 - i] = f['L'][2 - i][0]
            f['L'][2 - i][0] = temp[i]
    elif move == "B'":
        f['B'] = rotate_face_ccw(f['B'])
        temp = [f['U'][0][i] for i in range(3)]
        for i in range(3):
            f['U'][0][i] = f['L'][2 - i][0]
            f['L'][2 - i][0] = f['D'][2][2 - i]
            f['D'][2][2 - i] = f['R'][i][2]
            f['R'][i][2] = temp[i]
    elif move == 'L':
        f['L'] = rotate_face(f['L'])
        temp = [f['U'][i][0] for i in range(3)]
        for i in range(3):
            f['U'][i][0] = f['B'][2 - i][2]
            f['B'][2 - i][2] = f['D'][i][0]
            f['D'][i][0] = f['F'][i][0]
            f['F'][i][0] = temp[i]
    elif move == "L'":
        f['L'] = rotate_face_ccw(f['L'])
        temp = [f['U'][i][0] for i in range(3)]
        for i in range(3):
            f['U'][i][0] = f['F'][i][0]
            f['F'][i][0] = f['D'][i][0]
            f['D'][i][0] = f['B'][2 - i][2]
            f['B'][2 - i][2] = temp[i]
    elif move == 'R':
        f['R'] = rotate_face(f['R'])
        temp = [f['U'][i][2] for i in range(3)]
        for i in range(3):
            f['U'][i][2] = f['F'][i][2]
            f['F'][i][2] = f['D'][i][2]
            f['D'][i][2] = f['B'][2 - i][0]
            f['B'][2 - i][0] = temp[i]
    elif move == "R'":
        f['R'] = rotate_face_ccw(f['R'])
        temp = [f['U'][i][2] for i in range(3)]
        for i in range(3):
            f['U'][i][2] = f['B'][2 - i][0]
            f['B'][2 - i][0] = f['D'][i][2]
            f['D'][i][2] = f['F'][i][2]
            f['F'][i][2] = temp[i]
