from typing import Tuple
from math import floor

"""
Piece class for creating rubiks cube class
"""
class Piece:
    """
    Initializes the piece class with given parameters

    Params:
    colors Tuple[int, int, int]: the colors in any order of the piece following this rule
                                 0: White
                                 1: Blue
                                 2: Red
                                 3: Green
                                 4: Orange
                                 5: Yellow
    position Tuple[int, int, int]: A valid coordinate for the position ranging from (0-2, 0-2, 0-2)
    rotation int: The rotation value of the piece which can only be either 0, 1 or -1 which '
                  coresponds to no rotation, clockwise rotation, counter clockwise rotation
    """
    def __init__(self, colors: Tuple[int, int, int], position: Tuple[int, int, int], rotation: int):
        color_order = colors.sort()
        position = position
        rotation = rotation


class RubiksCube:
    def __init__(self):
        self.pieces = {
            'corners': [],
            'edges': []
        }

    def __repr__(self):
        # Provide a string representation of the cube's current state as pieces
        return ' '.join(self.pieces)

    def add_piece(self, colors: Tuple[int, int, int], rotation: int):
        piece_to_add = Piece(colors, self.get_next_pos(), rotation)
        if self.next_is_corner():
            self.pieces['corners'].append(piece_to_add)
        else:
            self.pieces['corners'].append(piece_to_add)

    def get_next_pos(self) -> Tuple[int, int, int]:
        """Gets the next position to be added, if the cube is full return [-1, -1, -1]"""
        pos: Tuple[int, int, int] = [-1, -1, -1]
        n_pieces_used: int = len(self.pieces['corners']+self.pieces['edges'])
        if len(n_pieces_used) >= 24:
            return pos
        # This gives the coords based on the amount of pieces left starts from top left and snakes around
        pos[0] = [0,1,2,0,2,0,1,2,0,2,0,2,0,1,2,0,2,0,1,2][n_pieces_used]
        pos[1] = [2,2,2,2,2,2,2,2,1,1,1,1,0,0,0,0,0,0,0,0][n_pieces_used]
        pos[2] = [0,0,0,1,1,2,2,2,0,0,2,2,0,0,0,1,1,2,2,2][n_pieces_used]
        return pos
    
    def next_is_corner(self) -> bool:
        """Returns true if next piece should be a corner"""
        n_pieces_used: int = len(self.pieces['corners']+self.pieces['edges'])
        return [1,0,1,0,0,1,0,1,0,0,0,0,1,0,1,0,0,1,0,1][n_pieces_used]
    
    def display(self):
        # Display the cube's current state as pieces
        print("Cube pieces:")
        for piece in self.pieces:
            print(piece)

# Example usage of the RubiksCube class
def main():
    piece = Piece([0,'white',2], [0, 1, 2], 0)
    # Create a new Rubik's Cube
    cube = RubiksCube()

    # # Display the initial state of the cube
    # print("Initial Cube State:")
    # print(cube)
    # print()

    # # Set a new state using a state string
    # # Example state string: "01234567890123456789012345"
    # # This string should be 26 characters long, each representing a color
    # new_state = "01234567890123456789012345"
    # cube.set_state(new_state)

    # # Display the updated state of the cube
    # print("Updated Cube State:")
    # print(cube)
    # print()

    # # Display the cube's pieces
    # cube.display()

if __name__ == "__main__":
    main()