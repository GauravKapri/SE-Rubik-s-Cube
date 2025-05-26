import kociemba
from decode_position import decode_postion


def solve(cube):
    values = ""
    values = values.join(decode_postion(cube))
    solution = kociemba.solve(values)
    print("solution is\n" + solution)
    return solution
