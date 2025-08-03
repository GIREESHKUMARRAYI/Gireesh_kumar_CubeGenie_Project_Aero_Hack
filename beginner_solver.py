from move_engine import apply_move

def beginner_solve(cube):
    moves = []
    for _ in range(4):
        apply_move(cube, 'U')
        moves.append('U')
    return moves
