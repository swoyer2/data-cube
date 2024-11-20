from typing import Tuple
import random

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
        self.colors = colors
        self.position = position
        self.rotation = rotation

    def get_str(self) -> str:
        info = ''
        for color in self.colors:
            info += str(color)
        info += ' '
        info += str(self.rotation)
        info += ' '
        return info


class RubiksCube:
    def __init__(self):
        self.pieces = {
            'corners': [],
            'edges': []
        }

        # Define the solved state mapping
        self.solved_corner_positions = {
            (0, 2, 1): (0, 2, 2),
            (0, 1, 4): (2, 2, 2),
            (0, 4, 3): (2, 2, 0),
            (0, 3, 2): (0, 2, 0),
            (5, 4, 1): (2, 0, 2),
            (5, 1, 2): (0, 0, 2),
            (5, 2, 3): (0, 0, 0),
            (5, 3, 4): (2, 0, 0)
        }
        self.solved_edge_positions = {
            (0, 1): (1, 2, 2),
            (0, 2): (0, 2, 1),
            (0, 3): (1, 2, 0),
            (0, 4): (2, 2, 1),
            (5, 1): (1, 0, 2),
            (5, 2): (0, 0, 1),
            (5, 3): (1, 0, 0),
            (5, 4): (2, 0, 1),
            (2, 1): (0, 1, 2),
            (1, 4): (2, 1, 2),
            (4, 3): (2, 1, 0),
            (3, 2): (0, 1, 0)
        }

    def __repr__(self):
        color_lookup = {
            0: 'W', 1: 'B', 2: 'R', 3: 'G', 4: 'O', 5: 'Y'
        }
        
        def get_color_by_position(position, color_index):
            for piece_type in ['corners', 'edges']:
                for piece in self.pieces[piece_type]:
                    if piece.position == position:
                        return color_lookup[piece.colors[color_index]]
            return ' '  # Return a space if no piece is found at the position
        
        output = '\n'.join([
            # Top face
            f"{get_color_by_position((0, 2, 0), 0)}{get_color_by_position((1, 2, 0), 0)}{get_color_by_position((2, 2, 0), 0)}",
            f"{get_color_by_position((0, 2, 1), 0)}W{get_color_by_position((0, 2, 2), 0)}",
            f"{get_color_by_position((0, 2, 2), 0)}{get_color_by_position((1, 2, 2), 0)}{get_color_by_position((2, 2, 2), 0)}",
            '',
            # Top mid
            f"{get_color_by_position((0, 2, 2), 2)}{get_color_by_position((1, 2, 2), 1)}{get_color_by_position((2, 2, 2), 1)} "
            f"{get_color_by_position((2, 2, 2), 2)}{get_color_by_position((2, 2, 1), 1)}{get_color_by_position((2, 2, 0), 1)} "
            f"{get_color_by_position((2, 2, 0), 2)}{get_color_by_position((1, 2, 0), 1)}{get_color_by_position((0, 2, 0), 1)} "
            f"{get_color_by_position((0, 2, 0), 2)}{get_color_by_position((0, 2, 1), 1)}{get_color_by_position((0, 2, 2), 1)}",
            # Mid mid
            f"{get_color_by_position((0, 1, 2), 1)}B{get_color_by_position((2, 1, 2), 0)} "
            f"{get_color_by_position((2, 1, 2), 1)}O{get_color_by_position((2, 1, 0), 0)} "
            f"{get_color_by_position((2, 1, 0), 1)}G{get_color_by_position((0, 1, 0), 0)} "
            f"{get_color_by_position((0, 1, 0), 1)}R{get_color_by_position((0, 1, 2), 0)}",
            # Bot mid
            f"{get_color_by_position((0, 0, 2), 1)}{get_color_by_position((1, 0, 2), 1)}{get_color_by_position((2, 0, 2), 2)} "
            f"{get_color_by_position((2, 0, 2), 1)}{get_color_by_position((2, 0, 1), 1)}{get_color_by_position((2, 0, 0), 2)} "
            f"{get_color_by_position((2, 0, 0), 1)}{get_color_by_position((1, 0, 0), 1)}{get_color_by_position((0, 0, 0), 2)} "
            f"{get_color_by_position((0, 0, 0), 1)}{get_color_by_position((0, 0, 1), 1)}{get_color_by_position((0, 0, 2), 2)}",
            '',
            # Bottom face
            f"{get_color_by_position((0, 0, 2), 0)}{get_color_by_position((1, 0, 2), 0)}{get_color_by_position((2, 0, 2), 0)}",
            f"{get_color_by_position((0, 0, 1), 0)}Y{get_color_by_position((2, 0, 1), 0)}",
            f"{get_color_by_position((0, 0, 0), 0)}{get_color_by_position((1, 0, 0), 0)}{get_color_by_position((2, 0, 0), 0)}"
        ])
        
        return output
    
    def get_information(self):
        """Gets the information on how to store the cube"""
        info = ''
        corners = self.pieces['corners']
        edges = self.pieces['edges']
        for _ in range(len(corners) + len(edges)):
            if [1,0,1,0,0,1,0,1,0,0,0,0,1,0,1,0,0,1,0,1][_]:
                info += corners.pop(0).get_str()
            else:
                info += edges.pop(0).get_str()
        return info

    def get_amount_of_pieces(self):
        return len(self.pieces['corners']) + len(self.pieces['edges'])

    def generate_solved_cube(self):
        self.pieces["corners"].clear()
        self.pieces["edges"].clear()
        piece_colors = [
            (0, 3, 2), (0, 3), (0, 4, 3), (0, 2), (0, 4), (0, 2, 1), (0, 1), (0, 1, 4),
            (3, 2), (4, 3), (2, 1), (1, 4),
            (5, 2, 3), (5, 3), (5, 3, 4), (5, 2), (5, 4), (5, 1, 2), (5, 1), (5, 4, 1)
        ]

        for colors in piece_colors:
            self.add_piece(colors, 0)

    def add_piece(self, colors: Tuple[int, int, int], rotation: int):
        piece_to_add = Piece(colors, self.get_next_pos(), rotation)
        if self.next_is_corner():
            self.pieces['corners'].append(piece_to_add)
        else:
            self.pieces['edges'].append(piece_to_add)

    def get_next_pos(self) -> Tuple[int, int, int]:
        """Gets the next position to be added, if the cube is full return [-1, -1, -1]"""
        pos: list[int, int, int] = [-1, -1, -1]
        n_pieces_used: int = len(self.pieces['corners']+self.pieces['edges'])
        if n_pieces_used >= 24:
            return tuple(pos)
        # This gives the coords based on the amount of pieces left starts from top left and snakes around
        pos[0] = [0,1,2,0,2,0,1,2,0,2,0,2,0,1,2,0,2,0,1,2][n_pieces_used]
        pos[1] = [2,2,2,2,2,2,2,2,1,1,1,1,0,0,0,0,0,0,0,0][n_pieces_used]
        pos[2] = [0,0,0,1,1,2,2,2,0,0,2,2,0,0,0,1,1,2,2,2][n_pieces_used]
        return tuple(pos)
    
    def next_is_corner(self) -> bool:
        """Returns true if next piece should be a corner"""
        n_pieces_used: int = len(self.pieces['corners']+self.pieces['edges'])
        return [1,0,1,0,0,1,0,1,0,0,0,0,1,0,1,0,0,1,0,1][n_pieces_used]
    
    def display(self):
        # Display the cube's current state as pieces
        print("Cube pieces:")
        for piece in self.pieces:
            print(piece)

    def get_corner_colors(self) -> list:
        """Returns a list of possible corner colors."""
        return [
            (0, 3, 2), (0, 4, 3), (0, 2, 1), (0, 1, 4),
            (5, 2, 3), (5, 3, 4), (5, 1, 2), (5, 4, 1)
        ]

    def get_edge_colors(self) -> list:
        """Returns a list of possible edge colors."""
        return [
            (0, 3), (0, 2), (0, 4), (0, 1),
            (3, 2), (4, 3), (2, 1), (1, 4),
            (5, 3), (5, 2), (5, 4), (5, 1),
        ]

    def get_used_pieces_colors(self) -> list:
        """Returns a list of tuples of colors for pieces already used in the cube."""
        return [piece.colors for piece in self.pieces['corners'] + self.pieces['edges']]
    
    def get_possible_moves(self) -> list:
        possible_moves = []
        n_pieces_used = len(self.pieces['corners'] + self.pieces['edges'])

        if n_pieces_used >= 20:
            return possible_moves

        is_next_corner = self.next_is_corner()
        corner_colors = self.get_corner_colors()
        edge_colors = self.get_edge_colors()
        used_pieces = self.get_used_pieces_colors()

        if is_next_corner:
            current_rotation_sum = sum(piece.rotation for piece in self.pieces['corners'])

            for colors in corner_colors:
                if colors not in used_pieces:
                    if len(self.pieces['corners']) == 7:
                        required_rotation = (3 - (current_rotation_sum % 3)) % 3
                    else:
                        for rotation in range(3):
                            self.pieces['corners'].append(Piece(colors, self.get_next_pos(), rotation))
                            #if not self.check_permutation_parity():
                            possible_moves.append((colors, rotation))
                            self.pieces['corners'].pop()
                        continue
                    possible_moves.append((colors, required_rotation))
        else:
            for colors in edge_colors:
                if colors not in used_pieces:
                    self.pieces['edges'].append(Piece(colors, self.get_next_pos(), 0))
                    #if not self.check_permutation_parity():
                    possible_moves.append((colors, 0))
                    self.pieces['edges'].pop()

                    self.pieces['edges'].append(Piece(colors, self.get_next_pos(), 1))
                    #if not self.check_permutation_parity():
                    possible_moves.append((colors, 1))
                    self.pieces['edges'].pop()

        return possible_moves

    