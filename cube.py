class RubiksCube:
    def __init__(self):
        # Initialize a solved Rubik's Cube with pieces
        self.pieces = [
            'WBO', 'WB', 'WBR', 'WO', 'WGR', 'WGO',
            'YBO', 'YBR', 'YGR', 'YGO', 'WR', 'WG',
            'YO', 'YR', 'YG', 'YB',
            'GO', 'GR', 'BO', 'BR', 
            'W', 'Y', 'G', 'B', 'O', 'R'
        ]

    def __repr__(self):
        # Provide a string representation of the cube's current state as pieces
        return ' '.join(self.pieces)

    def set_state(self, state_string):
        # Map numbers to colors
        color_map = {
            '0': 'W',  # White
            '1': 'Y',  # Yellow
            '2': 'G',  # Green
            '3': 'B',  # Blue
            '4': 'O',  # Orange
            '5': 'R',  # Red
        }
        
        # Fill the state string with '?' if it's less than 26 characters
        state_string = state_string.ljust(26, '?')
        
        # Update the cube's pieces
        self.pieces = [color_map.get(c, '?') for c in state_string]

    def display(self):
        # Display the cube's current state as pieces
        print("Cube pieces:")
        for piece in self.pieces:
            print(piece)

# Example usage of the RubiksCube class
def main():
    # Create a new Rubik's Cube
    cube = RubiksCube()

    # Display the initial state of the cube
    print("Initial Cube State:")
    print(cube)
    print()

    # Set a new state using a state string
    # Example state string: "01234567890123456789012345"
    # This string should be 26 characters long, each representing a color
    new_state = "01234567890123456789012345"
    cube.set_state(new_state)

    # Display the updated state of the cube
    print("Updated Cube State:")
    print(cube)
    print()

    # Display the cube's pieces
    cube.display()

if __name__ == "__main__":
    main()