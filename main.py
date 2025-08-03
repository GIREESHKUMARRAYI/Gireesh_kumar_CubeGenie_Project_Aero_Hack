from cube_state import Cube
from move_engine import apply_move
from beginner_solver import beginner_solve
from gui_visualizer import launch_gui

def main():
    cube = Cube()
    scramble = ['R', 'U', "R'", 'U', 'R', 'U2', "R'"]
    for move in scramble:
        if move.endswith('2'):
            base = move[0]
            apply_move(cube, base)
            apply_move(cube, base)
        else:
            apply_move(cube, move)

    print("Scrambled Cube:")
    print(cube)

    solution = beginner_solve(cube)
    print("\nSolution Moves:", solution)

    launch_gui(cube)

if __name__ == '__main__':
    main()
